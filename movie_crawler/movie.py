import requests
movie_code=['20184105', '20176251', '20189463', '20180290', '20183915', '20185485', '20184574', '20186281', '20170658', '20175547', '20183785', '20184187', '20182421', '20168773', '20183479', '20183238', '20177552', '20179230', '20183375', '20189843', '20182082', '20178825', '20183745', '20177538', '20184481', '20181905', '20176814', '20183073', '20181171', '20183007', '20182966', '20183050', '20182935', '20182669', '20186822', '20170513', '20189869', '20174981', '20010291', '20179006', '20181404', '20180523', '20182693']

movie_name_ko=[]
movie_name_en=[]
movie_name_og=[]
prdt_year=[]
showtime=[]
genres=[]
directors=[]
watch_grade_nm=[]
actor1=[]
actor2=[]
actor3=[]



for code in movie_code:
    url='http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=d4b4c2ebec2c5f60e74c449ef17c5a0a&movieCd='+code
    response = requests.get(url).json()['movieInfoResult']['movieInfo']
    movie_name_ko.append(response['movieNm'])
    movie_name_en.append(response['movieNmEn'])
    movie_name_og.append(response['movieNmOg'])
    prdt_year.append(response['openDt'])
    showtime.append(response['showTm'])
    genres.append(response['genres'][0]['genreNm'])
    directors.append(response['directors'][0]['peopleNm'])
    watch_grade_nm.append(response['audits'][0]['watchGradeNm'])
    if len(response['actors']) < 1:
        actor1.append('')
    else:
        actor1.append(response['actors'][0]['peopleNm'])   
    if len(response['actors']) < 2 :
        actor2.append('')
    else:
        actor2.append(response['actors'][1]['peopleNm'])
    if len(response['actors']) < 3 : 
        actor3.append('')
    else: 
        actor3.append(response['actors'][2]['peopleNm'])


for i in range(43):
    print(movie_code[i], movie_name_ko[i], movie_name_en[i], movie_name_og[i], prdt_year[i], showtime[i], genres[i], directors[i], watch_grade_nm[i], actor1[i], actor2[i], actor3[i])




               



