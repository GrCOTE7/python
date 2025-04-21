import requests

url = "https://c57.fr"
response = requests.get(url)
html = response.content

print(html)

