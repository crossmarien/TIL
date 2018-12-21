yournumber=[2,25,28,30,33,45]
import random
number1=(range(1,46))
number=random.sample(number1,6)
bonus_number = 7
n=5
for value in yournumber:
    if value in number:
        n=n-1
print (n)
