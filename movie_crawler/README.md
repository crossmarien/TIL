README

# movie -crawler기본 설계도

## 1. 이용한 api

### 1.영화진흥위원회 오픈 API(주간/주말 박스오피스 데이터)

#### api 받는방법

http://www.kobis.or.kr/kobisopenapi/homepg/main/main.do

위 도메인에들어가서 주간박스오피스 api를 받는다.



#### api요청 URL

http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.**json**?key="yourkey"&targetDt="yourdate"&weekGb="0"

윗줄 주소는 고정이고

입력해야할 값들은: 

1.key값 : api 이용신청을 하면 보급되는 개인 key값을 이용하면 된다.

2.날짜정보 : 조회하고 싶은 날짜정보

3.주간/일간: 명세서를 따라 주간(월~일)정보를 받기위해 weekGb에 0값을 준다.



### 2.영화진흥위원회 오픈 API(영화 상세정보)

### 3.네이버 영화 검색 API

## 2. csv파일

### boxoffice.csv

1.우선 dates라는 리스트안에 2019년01월13일부터 2018년11월11일까지의 일요일 날짜를 넣어주었다.(총 10주,역순)

2. for 문을 돌며 매주 영화순위 top10의 api를 dictionary형태로 받아온다.
3. top 10의 제목,영화코드,누적관객수,누적관객수측정날짜를 각각 리스트에 추가한다.
4. 나머지 주간을 돌며 새로 top10에 추가된 영화들의 정보들만 각 리스트에 추가한다.(중복제거, 누적관객수 최대값만 저장. 누적관객수는 줄어들지 않는다는점을 이용.)
5. 제목,영화코드,누적관객수,누적관객날짜에는 각각 43개의 영화의 해당하는 정보가 들어있다.이를 for문을 사용해 영화코드-제목-누적관객수-날짜순으로 print 했다.



p.s. 어떤 날짜를 입력하면 그주를 기준으로 10주전까지 데이터를 출력하는 프로그램을 구현해보자!

### movie.csv

### movie_naver.csv



















['말모이', '내안의 그놈', '주먹왕 랄프 2: 인터넷 속으로', '아쿠아맨', '극장판 공룡메카드: 타이니소어의 섬', '보헤미안 랩소디', '그린 북', '범블비', 'PMC: 더 벙커', '스윙키즈', '점박이 한반도의 공룡2 : 새로운 낙원', '언니', '그린치', '마약왕', '극장판 짱구는 못말려: 아뵤! 쿵후 보이즈 ~라면 대란~', '스파이더맨: 뉴 유니버스', '국가부도의 날', '도어락', '극장판 포켓몬스터 모두의 이야기', '호두까기 인형과 4개의 왕국', '부탁 하나만 들어줘', '모털 엔진', '런닝맨 : 풀룰루의 역습', '완벽한 타인', '성난황소', '후드', '신비한 동물들과 그린델왈드의 범죄', '베일리 어게인', '바울', '거미줄에 걸린 소녀', '투 프렌즈', '번 더 스테이지: 더 무비', '출국', '툴리', '너의 췌장을 먹고 싶어', '동네사람들', '해피 투게더', '창궐', '해리포터와 마법사의 돌', '여곡성', '벽 속에 숨은 마법시계', '스타 이즈 본', '구스범스: 몬스터의 역습']

['20184105', '20176251', '20189463', '20180290', '20183915', '20185485', '20184574', '20186281', '20170658', '20175547', '20183785', '20184187', '20182421', '20168773', '20183479', '20183238', '20177552', '20179230', '20183375', '20189843', '20182082', '20178825', '20183745', '20177538', '20184481', '20181905', '20176814', '20183073', '20181171', '20183007', '20182966', '20183050', '20182935', '20182669', '20186822', '20170513', '20189869', '20174981', '20010291', '20179006', '20181404', '20180523', '20182693']

['1185368', '765383', '1342315', '4920735', '289873', '9785643', '99569', '1553491', '1665204', '1462874', '521053', '172340', '543815', '1787838', '259753', '628327', '3723915', '1546002', '86997', '408425', '87501', '262070', '180709', '5270621', '1567264', '276658', '2403686', '78439', '229837', '25172', '20419', '298402', '71407', '24325', '48910', '445625', '15745', '1588443', '259733', '55997', '211233', '458917', '21400']

['20190113', '20190113', '20190113', '20190113', '20190113', '20190113', '20190113', '20190113', '20190113', '20190113', '20190106', '20190106', '20190106', '20181230', '20181230', '20181230', '20181223', '20181223', '20181223', '20181216', '20181216', '20181216', '20181216', '20181216', '20181209', '20181209', '20181209', '20181202', '20181202', '20181202', '20181202', '20181125', '20181125', '20181125', '20181125', '20181118', '20181118', '20181111', '20181111', '20181111', '20181111', '20181111', '20181111']
































