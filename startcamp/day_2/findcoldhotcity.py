#도시중에 가장 추웠던곳, 더웠던곳 표기하기

cities_temperature= {
    '서울': [-6,-10,5],
    '대전':[-3,-5,2],
    '광주':[0,-5,10],
    '구미':[2,-2,9]
    }

#혼자 생각해보기
seoul_temperature=(cities_temperature["서울"])
daejun_temperature=(cities_temperature["대전"])
gwangju_temperature=(cities_temperature["광주"])
gumi_temperature=(cities_temperature["구미"])

alltemperature=seoul_temperature+daejun_temperature+gwangju_temperature+gumi_temperature

if max(alltemperature) in seoul_temperature:
    print ('가장 더운도시는 서울')
elif max(alltemperature) in daejun_temperature:
    print ('가장 더운도시는 대전')
elif max(alltemperature) in gwangju_temperature:
    print ('가장 더운도시는 광주')
else:
    print('가장 더운도시는 구미')

if min(alltemperature) in seoul_temperature:
    print ('가장 추운도시는 서울')
elif min(alltemperature) in daejun_temperature:
    print ('가장 추운도시는 대전')
elif min(alltemperature) in gwangju_temperature:
    print ('가장 추운도시는 광주')
else:
    print('가장 추운도시는 구미')

# 똑똑하게 풀어보기

n=0
hot = ''

for key, value in cities_temperature.items():
    maxvalue = max(value)
    if maxvalue > n:
        n = maxvalue
        hot= key

print ('가장 더운도시는',hot,n)

n=0
cold = ''

for key, value in cities_temperature.items():
    minvalue = min(value)
    if minvalue < n:
        n = minvalue
        cold = key

print ('가장 추운 도시는',cold,n)

#정답 (내가 처음에 한걸 훨씬 기술적으로 해주심 ㅎ)
#all_temp에 모든 기온 모으기
all_temp=[]
for key,value in cities_temperature.items():
    all_temp += value    

print (all_temp)
#all_temp의 최대/최소찾기
highest = max(all_temp)
lowest = min (all_temp)
#cities_temp 에서 highest/lowest가 속한 도시를 찾는다.
hottest= []
coldest= []
for key,value in cities_temperature.items():
    if highest in value:
        hottest.append(key)
    if lowest in value:
        coldest.append(key)    
    
print (hottest, coldest)