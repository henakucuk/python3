
from bs4 import BeautifulSoup
import requests

adres="http://www.gokhansu.com/"

kaynak=requests.get(adres).text

soup=BeautifulSoup(kaynak, "html.parser")

resimler=soup.find_all("img")

for resim in resimler:
    print(resim["src"])