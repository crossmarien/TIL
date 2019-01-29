import requests
from bs4 import BeautifulSoup
response=requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
doc=response.text
soup=BeautifulSoup(doc,'html.parser')
dataset=soup.select('.title')
print (dataset)