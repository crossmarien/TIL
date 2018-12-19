# 181218 수업정리

## 1.프로그램 리스트

* chocolatey 

  * widows package manager

* python -v 3.6.7

* git

*  visual studio code

  ## 2.visual studio code

  ### default setting

  ctr+shi+p, select default shell,  gitbash 후 ctrl `

  ### 명령어

  cd=change directory

  cd/c/users/student 이런식으로 파일 찾아들어감.

  cd ~ 또는  cd만 치면 저장된 파일(student)로 감

  cd / 내 pc로감 

  cd ~/TIL/ student의 TIL 폴더로 들어감

  mkdir day_1 day_2 day_3 day_4 day-5

  rmdir remove directory

  ## 3.python coding

* typecasting방법 int('123')이라고 하면 123이된다.

#### dictionary

```python
dust={"강남구":58,"서초구":40}

print(dust["강남구"])
```

#### list

```python
a=[1,2,3]

dust[0]
```

#### if 문

```python
if dust>50:

	print("50초과")

else:

	print("50이하")
```

#### while 문

```python
n=0  

while n<3:

명령어

n=n+1
```

#### for  문

```python
dust=[59,24,102]

for i in dust:  

print(i)
```



###  4. list 활용법

```numbers=list(range(1,16))
numbers=list(range(1,16))
```

```python
#변수이름을 남들이 보기쉽게 짓자.
numbers=[1,3,5]
family = ['mom',1.2,'dad',1.5]
school={"han":'gent',"fu":'korea',"juntae":'sorbonne'}
mcu=[
    [1,2,3],
    [10,11,12],
    [20,21,23]
    ]
    # 이렇게 써놓으면 사람이 이해하기 편하다.
type(mcu),
#집합안의 집합을 꺼내려면 mcu[x][y]식으로 하면 된다.
numbers=list(range(1,16))
```

list에 새로운 항목 추가하는법

```python
numbers= numbers+[1]
numbers+=1
#위 두개수식은 같은뜻
```

제거하는법

```python
del team[1:3]
del team [1]
```

###  5.dictionary 활용법

```python
staffmember = [
    {
        'name':'antoine',
        'email':'jhantoine96@gmail.com'
    },
    {
        'name':'juntae',
        'naver':'crossmarien@naver.com',
        'google1':'ggcmgg@gmail.com',
        'google2':'krparkjuntae@gmail.com',
        'google3':'ggcmgg1.gmail.com'
    },
    {
        'name':'siho',
        'gmail':'cuse0414@gmail.com'
    }
]

print(staffmember[1]["google1"])
```

### 6. function

자주 쓰이는 function

```python
scores=[1,2,3,4,5]
max(scores) #최댓값
round (1.8) round (1.4) #반올림
min(scores) 
sorted (x) #작은것부터 큰것,
sorted (x, reverse=True) #큰것부터 작은것
print 
len
type

```



### python 출처 

python "f(x)" documentation (공식문서) 

help (f(x)) 쓰면 공식문서에서 가져다줌

stack overflow

w3schools



### method란

object에 속해있는 function : 즉 메서드는 함수다 (주어)(동사)의 형식으로 이루어지며, (주어)자리에 오는 object들이 할 수 있는 (함수)이다.

예를들어 str class의 오브젝트인 'x'를 hello로 정의했다.

```
x='hello'
```

여기서 .capitalize라는 method 를 쓰면

```python
x.capitalize()
Hello
```

자주쓰는 method

.sort ()

.replace ()

.append ()



| str   | int   | bool |      |
| ----- | ----- | ---- | ---- |
| 'sdf' | 0,1,2 | True |      |

| str  | asd  | df   |
| ---- | ---- | ---- |
|      |      |      |





Web 긁어오는법

우선 pip install requests로 requests 를 가져옴

```python
import requests 
url= 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'
#블로그에서 api를 긁어오고 맨뒤에 횟차를 칩력함
response=requests.get(url, verify=False)
#url 에서 api를 받는데 마지막에 verify=false가 인증서를 무시하는 명령(나눔로또에 인증서가 만료된상태였음)
print (response.text)
#.text를 붙여줘야 원하는 정보를 겟.
```



darksky에서 api 긁어왔는데 보기힘드니 json viewer chrome을 깔아보자



