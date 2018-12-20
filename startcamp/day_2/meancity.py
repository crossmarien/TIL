#3:도시별 온도 평균

import statistics
cities_temperature= {'서울': [-6,-10,5],
'대전':[-3,-5,2],
'광주':[0,-5,10],
'구미':[2,-2,9]
}
#정답
#방법 1
for city in cities_temperature:
    temperatures=cities_temperature[city]
    avg_temperature=round(sum(temperatures)/len(temperatures), 2)
    print('{0}: {1}'.format(city, avg_temperature))
#or
    print (city,avg_temperature)
    print(city + ': ' +str (avg_temperature))
#방법2
for key, value in cities_temperature.items():
    avg_temperature = round(sum(value)/len(value), 2)
    print (key, avg_temperature)
    print (key+ ': ' + str(avg_temperature))


