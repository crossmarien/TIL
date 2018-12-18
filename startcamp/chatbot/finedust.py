import requests
from bs4 import BeautifulSoup

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey={}&sidoName=서울&pageNo=3'.format(key)
response = requests.get(url).text
soup = BeautifulSoup(response, 'xml')
gn = soup('item')[7]
location = gn.stationName.text
time = gn.dataTime.text

# 얘가 중요한 것!
dust = int(gn.pm10Value.text)

print('{0} 기준: 서울시 {1}의 미세먼지 농도는 {2} 입니다.'.format(time, location, dust))

# 그래서 지금 공기가 어느정도로 안좋은건데..?
if dust>150:
    print("매우나쁨")
elif 80<dust<=150:
    print("나쁨")
elif 30<dust<=80:
    print("보통")
else:
  print("좋음")