#real number 가져오는법
import requests 

my_numbers = pick_lotto()
def pick_lotto():
    numbers=random.sample((range(1,46)),6)
    my_numbers:sort()
    my_numbers=set(my_numbers)
    
real_numbers=get_lotto()
result=am_i_lucky (my_numbers,real_numbers)

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

realnumber=[2,25,28,30,33,45]
import random
a=(range(1,46))
attempt=random.sample(a,6)
bonus_number = 7
n=0
for value in realnumber:
    if value in attempt:
        n=n+1

if n==5 and 7 in attempt:
    print ('2등입니다 당청금 100억')
elif n==6:
    print ('1등입니다 당첨금 500억')
elif n==5:
    print('3등입니다')
elif n==4:
    print('4등입니다')
elif n==3 :
    print('5등입니다')
elif n==2:
    print ('4등입니다')
else:
    print('꽝')


my_numbers=set([1,2,3,4,5,8])
real_numbers=set([1,2,3,4,5,6])
bonus=7

match_count=len(my_numbers & real_numbers)
print (match_count)

if match_count ==6:
    print('1등')
elif match_count ==5 and bonus in my_numbers:
    print('2등')
