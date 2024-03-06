
from bs4 import BeautifulSoup
import requests

adres="http://www.gokhansu.com/"

kaynak=requests.get(adres).text

soup=BeautifulSoup(kaynak, "html.parser")

links=soup.find_all("a")

for link in links:
    if "zam" in link["href"]:
        print(link["href"])