from flask import Flask,jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', lunch=lunch)
    import requests
    from bs4 import BeautifulSoup
    response=requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
    doc=response.text
    soup=BeautifulSoup(doc,'html.parser')
    dataset=soup.select('.title')
    for i in dataset[0:11]:
        print(i.text)