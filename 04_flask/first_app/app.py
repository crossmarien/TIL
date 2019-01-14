from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index(): #/이걸 root라고 그러고 컴퓨터의 최상단. 여기서는 그냥 domain만 치고 들어올 경우 ex:naver.com
    return 'Hi'

@app.route('/ssafy')
def ssafy():
    return 'ssafy'

@app.route('/hi/<string:name>')
def hi(name):
    return(f'hi {name}')


@app.route("/dobak")
def dobak():
    yournumber=[2,25,28,30,33,45]
    number=sorted(random.sample(range(1,46),6))
    bonus_number = 7
    n=5
    for value in yournumber:
        if value in number:
            n=n-1
    rank=n
    return jsonify(rank)

@app.route('/dictionary/<string:word>')
def dictionary(word):
    dictionary={
        'apple':'사과',
        'banana':'바나나',
        'watermelon':'수박'
    }
    if word in dictionary.keys():
        translatedword=dictionary[word]
        return (f'{word} 은(는) {translatedword}!' )
    else: 
        return (f'{word}은(는) 나만의 단어장에 없는 단어입니다!')


app.run(debug=True)