student= {'python':80, 'algorithm':99, 'django':89, 'flask': 83}
mean=student["python"],student["algorithm"],student["django"],student["flask"]
a=0
for i in mean:
    a=a+i
result = a/4
print (result)

blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
count_a=0
count_b=0
count_o=0
count_ab=0
for i in blood_types:
    if i=='A':
        count_a +=1
    elif i=='B':
        count_b +=1
    elif i=='O':
        count_o +=1
    else:
        count_ab+=1
listblood=[count_a,count_b,count_o,count_ab]
print (listblood)
