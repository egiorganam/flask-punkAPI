from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get('https://api.punkapi.com/v2/beers/').json()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/beers/')
def beers():
    return render_template('beers.html', beers=response)


@app.route('/random-beer/')
def random_beer():
    random = requests.get('https://api.punkapi.com/v2/beers/random').json()
    return render_template('random-beer.html', beer=random)
