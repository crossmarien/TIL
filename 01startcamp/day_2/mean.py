#평균을 구하시오 (sas 는 proc means 한방이면 끝나는데...슈불)
import statistics
my_score=[79,88,66,93]
my_average=statistics.mean(my_score)
print ('my score is',my_average)

#dictionary 의 평균
your_score={
    'maths':79,
    'korean':88,
    'english':66,
    'ethic':93
}
#모르고 풀어보기
dictlist=[your_score
    ['maths'],
    your_score
    ['korean'],
    your_score
    ['english'],
    your_score
    ['ethic']
]
average=statistics.mean(dictlist)
print('your score is',average)

#댕청하게 짧은 견문으로 했으니 빠르고 똑똑한 방법을 써보자
shortlist=your_score.values()
result=statistics.mean(shortlist)
print('your result is',result)