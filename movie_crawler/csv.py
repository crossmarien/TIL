import csv
f = open('ss3.csv', 'a+', encoding='utf-8')
# ss3.csv를 w+읽고쓰기가 가능한 모드로 encoding해서 열꺼야.
writer = csv.writer(f)

for i in range(7):
    writer.writerow([i,i,i,i])
f.close()

f_r = open('ss3.csv','r', encoding='utf-8')
reader=csv.reader(f_r)
for line in reader:
    print(type(line), line)