import requests 
url= 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'
response=requests.get(url, verify=False)
lotto_data = response.json()
real_numbers=[]
# for key in data:
#     if 'drwtNo' in key:
#         real_numbers.append(data[key])
# print (real_numbers)

for key, value in lotto_data.items():
    if 'drwtNo'in key:
        real_numbers.append(value)



import random
a=(range(1,46))
b=random.sample(a,6)

if real_numbers == b:
    print ('우승!!!!'
    )
else
print ('실패하셨습니다.')
