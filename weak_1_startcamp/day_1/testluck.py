realnumber=[2,25,28,30,33,45]

import random
a=(range(1,46))
attempt=random.sample(a,6)

n=0
for value in realnumber:
    if value in attempt:
        n=n+1

if n==6:
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