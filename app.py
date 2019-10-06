
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'h1>Hello World</h1><a href="/kauplisti/">kauplisti</a> <a href="/Karfa/">Karfa</a>'

@app.route('Karfa')
def Karfa()
    return '<h3>halló</h3>'

@app.route('Kauplisti')
def Kauplisti()
    return '<h1>'<input type="submit" value = "Kaupa" />'</h1>'

if __name__ == "__main__":
	app.run(debug=True)
