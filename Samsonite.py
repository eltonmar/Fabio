import requests
from bs4 import BeautifulSoup
import pandas as pd

# Listas para armazenar os dados
product_names = []
prices = []
links = []

# Loop para percorrer as páginas
for page in range(1, 6):
    url = f"https://www.samsonite.com.br/collections/mala-de-viagem?page={page}"

    # Fazer a requisição HTTP
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar todos os produtos na página
    products = soup.find_all('div', class_='tw-group tw-relative tw-z-0 tw-flex tw-max-w-xs tw-flex-col tw-gap-3.5 tw-p-2 tw-transition-shadow tw-duration-300 hover:tw-shadow-lg sm:tw-p-5')

    for product in products:
        # Nome do produto
        name_tag = product.find('span', class_='tw-typ-body-3')
        if name_tag:
            product_names.append(name_tag.text.strip())
        else:
            product_names.append("N/A")

        # Preço do produto
        price_tag = product.find('span', class_='tw-text-brand-primary-accent')
        if price_tag:
            prices.append(price_tag.text.strip())
        else:
            prices.append("N/A")

        # Link do produto
        link_tag = product.find('a', href=True)
        if link_tag:
            links.append(f"https://www.samsonite.com.br{link_tag['href']}")
        else:
            links.append("N/A")

# Criar um DataFrame do Pandas
df = pd.DataFrame({
    'Product Name': product_names,
    'Price': prices,
    'Link': links
})

# Exportar para Excel
df.to_excel('samsonite_products.xlsx', index=False)

print("Dados exportados para 'samsonite_products.xlsx'")
