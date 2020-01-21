import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/temp', methods = ['GET', 'POST'])
def home():
	new_city = request.form['city']
	r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+new_city+'&units=metric&appid=70aea3443f94204bfc4c559b45f12876')
	json_obj = r.json()

	weather = {
		'city' : new_city,
		'temperture': r['main']['temp'],
		'description': r['weather'][0]['description'],
		'icon': r['weather'][0]['icon'],
	}

	return render_template('weather.html', weather = weather)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug = True)