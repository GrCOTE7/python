import requests
from bs4 import BeautifulSoup

page = "shop.html"

with open(page, "r", encoding="utf-8") as html_file:
    html = html_file.read()

# page='https://c57.fr'
# response = requests.get(page)
# html = response.content

soup = BeautifulSoup(html, "html.parser")

# print(soup.title)
# print(soup.title.string)


def generate_products_in_list():
    tables = soup.find_all("table")
    products = []
    for table in tables:
        for tr in table.find_all("tr")[1:]:
            td = tr.find_all("td")
            name = td[0].text
            description = td[1].text
            price = td[2].text
            quantity = td[3].text
            products.append(
                {
                    "name": name,
                    "description": description,
                    "price": price,
                    "quantity": quantity,
                }
            )
    return products


def generate_products_by_generator():
    for table in soup.find_all("table"):
        for tr in table.find_all("tr")[1:]:
            td = tr.find_all("td")
            name = td[0].text
            description = td[1].text
            price = td[2].text
            quantity = td[3].text
            yield {
                "name": name,
                "description": description,
                "price": price,
                "quantity": quantity,
            }


products1 = generate_products_in_list()
print(products1, flush=True)

print()

products = generate_products_by_generator()
all_products = []
for product in products:
    # print(product, flush=True)

    all_products.append(product)
print(all_products)
