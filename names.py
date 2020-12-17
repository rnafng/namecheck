import requests
from bs4 import BeautifulSoup

names = []

for a in range(97, 97+26):
    for b in range(97, 97 + 26):
        for c in range(97, 97 + 26):
            names.append(chr(a) + chr(b) + chr(c))

for n in names:
    URL = 'https://lolnames.gg/en/na/'+ n
    page = requests.get(URL)
    soup = str(BeautifulSoup(page.content, 'html.parser'))
    if "Cleanup date (if inactive):" not in soup or "It is available for new accounts." in soup:
        print(n)

