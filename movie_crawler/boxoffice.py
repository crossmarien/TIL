import requests
# key = 'd4b4c2ebec2c5f60e74c449ef17c5a0a'
# url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt=20190113'
Dates=['20190113','20190106','20181230','20181223','20181216','20181209','20181202','20181125','20181118','20181111']
movie_code= []
title= []
audience= [] 
recorded_at= []
listapi=[]
for date in Dates:
    url='http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=d4b4c2ebec2c5f60e74c449ef17c5a0a&targetDt='+date +'&weekGb=0'
    response = requests.get(url).json()['boxOfficeResult']['weeklyBoxOfficeList']
    for i in response:
        for key in i:
            if 'movieNm' in key and i[key] not in title:
                title.append(i[key])
                movie_code.append(i['movieCd'])
                audience.append(i['audiAcc'])
                recorded_at.append(date)

for i in range(43):
    print(movie_code[i], title[i], audience[i], recorded_at[i])




        


    
    
# result = []
# movie_info= {}
# for movie in movies:
#     data_set = requests.get(url+ movie, headers=headers).json()
#     movie_info['link'] = data_set['items'][0]['link']
#     movie_info['image'] = data_set ['items'][0]['image']
#     movie_info['name'] = data_set['items'][0]['image']
#     result.append(movie_info)



# urlweekly = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=d4b4c2ebec2c5f60e74c449ef17c5a0a&targetDt=20190113'

# movierank_data = response.json()
# WeeklyBoxOfficeList = movierank_data['boxOfficeResult']['WeeklyBoxOfficeList']
# print (WeeklyBoxOfficeList)

# moviecode=[]
# title = []
# audience =[]
# recorded_at= []









# http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=d4b4c2ebec2c5f60e74c449ef17c5a0a&movieCd=20185485

# https://openapi.naver.com/v1/search/movie.json?query=