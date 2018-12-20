# #real number 가져오는법
import requests 
import random
def pick_lotto():
    numbers=random.sample(range(1,46), 6)
    numbers.sort()
    # numbers=set(numbers)
    return numbers
my_numbers = pick_lotto()
print(my_numbers)
# # 
def get_lotto(draw_num):
    url= 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+str(draw_num)
    response=requests.get(url)
    lotto_data = response.json()
    numbers=[]
    bonus_number = lotto_data['bnusNo']
    for key, value in lotto_data.items():
        if 'drwtNo'in key:
            numbers.append(value)
    return {"number":numbers, "bonus":bonus_number}
numbers=get_lotto(837)
# print (numbers)
print (numbers["number"])
# #
# # 

# my_numbers = pick_lotto()
# numbers=get_lotto(837)
# def am_i_lucky(my_numbers,numbers):
#     n=0
#     for value in my_numbers:
#         if value in numbers["number"]:
#             n=n+1
#     if n==6:
#         return 'ranking=1'
#     # elif n==5 and bonus_number in my_numbers
#     #     ranking=2
#     elif n==5:
#         return 'ranking=3'
#     elif n==4:
#         return 'ranking=4'
#     elif n==3:
#         return 'ranking=5'
#     elif n==2:
#         return 'ranking=6'
#     else:
#         return 'ranking=7'

# rank= am_i_lucky(my_numbers,numbers)
# print(rank)

#정답

def am_i_lucky(pick,draw):
    match =set(pick) & set(draw["number"])
    if len(match)== 6:
        return('1등')
    elif len(match)==5 and draw['bonus_number'] in pick:
        return('3등')
    elif len(match)==4:
        return('4등')
    elif len(match)==3:
        return('5등')
    else:
        return('꽝')
result=am_i_lucky(pick_lotto(),get_lotto(837))
print (result)