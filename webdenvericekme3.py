
from bs4 import BeautifulSoup
import requests

adres="https://www.cumhuriyet.com.tr/"

kaynak=requests.get(adres).text

soup=BeautifulSoup(kaynak, "html.parser")

basliklar=soup.find_all("h3", attrs={"class":"haber-baslik"})

for baslik in basliklar:
    print(baslik.text.strip())