import requests
movies = ['말모이', '주먹왕 랄프', '보헤미안 렙소디']
url='https://openapi.naver.com/v1/search/movie.json?query='
client_id = '9FTo9hcNJwnAmo0VmwQX'
client_secret = 'r7xRLo20h1' 
headers = {
    'X-Naver-Client-Id': client_id,
 'X-Naver-Client-Secret':client_secret
 }

# res = requests.get(url + movies[0], headers=headers)
# data=res.json()
# print()


result = []
movie_info= {}
for movie in movies:
    data_set = requests.get(url+ movie, headers=headers).json()
    movie_info['link'] = data_set['items'][0]['link']
    movie_info['image'] = data_set ['items'][0]['image']
    movie_info['name'] = data_set['items'][0]['image']
    result.append(movie_info) 