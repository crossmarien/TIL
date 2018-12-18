import requests
from bs4 import BeautifulSoup
response=requests.get('https://finance.naver.com/marketindex/?tabSel=exchange')
doc=response.text
soup=BeautifulSoup(doc,'html.parser')
dataset=soup.select('.value')
print ('USD')
print(dataset[0].text)
print ('Yen')
print (dataset[1].text)