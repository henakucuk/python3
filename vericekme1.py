
from bs4 import BeautifulSoup

kaynak="""<html><head><title>gifted</title></head><body>
    <p>hena
    <a href="#">hena link</a>
    </p><p>toprak</p><p class="red">ada</p></body></html>"""

soup=BeautifulSoup(kaynak,"html.parser")

#print(soup.prettify())
#print(soup.a.text)
liste=soup.find_all("p",attrs={"class":"red"})
for eleman in liste:
    print(eleman.text)
