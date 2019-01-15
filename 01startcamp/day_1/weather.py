import requests
url='https://api.darksky.net/forecast/7ba3c554758a244d1964875521c4cd0c/37.5013068,127.037471'
res=requests.get(url)
data=res.json()
print(data['currently']['summary'])


from darksky import forecast
multicampus= forecast('7ba3c554758a244d1964875521c4cd0c', 37, 127)
print (multicampus['currently']['temperature'])