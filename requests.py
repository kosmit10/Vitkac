import requests
from bs4 import BeautifulSoup

def fetch_products():
    url = 'https://www.vitkac.com/pl/sklep/sale/mezczyzni'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.find_all('div', class_='product-item')

    return [{"name": prod.find('p', class_='brand-name').text.strip(),
             "link": prod.find('a')["href"]} for prod in products if prod.find('p', class_='brand-name')]

new_products = fetch_products()
print(new_products)
