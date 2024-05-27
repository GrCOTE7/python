import requests

from bs4 import BeautifulSoup

# url = "https://www.gov.uk/search/news-and-communications"
# html = requests.get(url)

html = """<html>
    <head>
        <title>Les chiens les plus mignons</title>
    </head>
    <body>
        <p class="title"><b>Les meilleures races de chiens</b></p>
        <p class="chiens">
            <a href="http://exemple.com/labradoodle" class="race" id="lien1">LabraDoodle</a>,
            <a href="http://exemple.com/retriever" class="race" id="lien2">Golden Retriever</a> et
            <a href="http://exemple.com/carlin" class="race" id="lien3">Carlin</a>
        </p>
    </body>
</html>
"""

# print(html.content)
# print(html.text)

soup = BeautifulSoup(html, "html.parser")

print("Titre: ", soup.title.string)
print()
print(soup.find_all("a"))
print()
print(soup.find(id="lien1"))
print()
print(soup.find_all("p", class_="title"))

print("-" * 68)

print(html)
