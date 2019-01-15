import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID={}".format(key)

data = requests.get(url).json()
weather = data['weather'][0]['description']
temp = float(data['main']['temp'])-273.15
temp_min = float(data['main']['temp_min'])-273.15
temp_max = float(data['main']['temp_max'])-273.15

print("""서울의 오늘 날씨는 [{}] 이며, 섭씨 {:.1f}도 입니다.
최저/최고 온도는 {:.1f}/{:.1f}도 입니다.
""".format(weather, temp, temp_min, temp_max)
)