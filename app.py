import requests
from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config[SQLALCHEMY_DATABASE_URI] = 'sqlite:///C:\\sqlite\\weather.db'
# db = SQLAlchemy(app)

# class city(db.model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	name = db.Column(db.String(50), nullable = False)


@app.route('/')
def home():
	url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=70aea3443f94204bfc4c559b45f12876'
	city = 'Las Vegas'

	r = requests.get(url.format(city)).json()
	print(r)

	weather = {
		'city': city,
		'temperture': r['main']['temp'],
		'description': r['weather'][0]['description'],
		'icon': r['weather'][0]['icon'],
	}

	print(weather)

	return render_template('weather.html', weather = weather)

if __name__ == "__main__":
	app.run(debug = True)