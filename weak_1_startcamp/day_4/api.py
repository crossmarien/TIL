import requests
url1='http://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=NWU2ODY4YTUyNzQ5NzVjOTNiOTI0OTRhMzE4YzAyOWI=&itmId=CCC+&objL1=01+06+09+&objL2=&objL3=&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=Y&newEstPrdCnt=1&loadGubun=2&orgId=375&tblId=DT_37501N_001'
response1=requests.get(url1)
data=response1.json()

salary=[]
for key, value in data.items():
    if 'DT' in key:
        salary.append(value)
print (salary)