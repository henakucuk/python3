
from bs4 import BeautifulSoup
import requests

adres="https://www.cumhuriyet.com.tr/"

kaynak=requests.get(adres).text

soup=BeautifulSoup(kaynak, "html.parser")

images=soup.find_all("img")

for img in images[:5]:
    print(img["src"])