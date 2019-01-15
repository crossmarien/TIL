#최대공약수 1
num1 = 20
num2 = 8
yaksu=0
number=[]
while  yaksu != min(num1,num2):
    yaksu= yaksu + 1
    number.append(yaksu)

cd1=[]
cd2=[]
assemblecd=[]
for i in number:
    if num1 % i ==0:
        cd1.append(i)
for i in number:
    if num2 % i == 0:
        cd2.append(i)
        
for i in cd1:
    if i in cd2 :
        assemblecd.append(i)
gcd= max (assemblecd)
print (gcd)    

#두번쨰 방법
# num1 = 21
# num2 = 14
# numbers = [num1] + [num2]
# a= min (numbers)
# cd=[]
# n=1
# while n<= a:
#     if num1 % n ==0 and num2 % n ==0:
#         cd.append(n)
#         n=n+1
#     else:
#         n=n+1
# print (max (cd))