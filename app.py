from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.projectH4


## HTML 화면 보여주기
@app.route('/')
def showHtml():
    return render_template('index.html')

@app.route('/movie.html')
def showMovie():
    return render_template('movie.html')

@app.route('/picture.html')
def showPicture():
    return render_template('picture.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)