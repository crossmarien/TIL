import requests
from bs4 import BeautifulSoup
a=requests.get('https://finance.naver.com/').text
soup=BeautifulSoup(a,'html.parser')
kospi=soup.select_one('.num')
print(kospi.text)