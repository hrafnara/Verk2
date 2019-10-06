import random
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello World</h1> <a href="/dice/">teningar</a> <a href="/hrafn/">hrafn</a>'
@app.route('/hrafn/')
def hrafn():
	return '<h3>halló</h3>'
@app.route('/dice/')
def dice():
	return '<h1>' + str(random.randint(1,6)) + '</h1>'

if __name__ == "__main__":
	app.run(debug=True)
