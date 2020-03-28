import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather/', methods=['POST'])
def getdata():
    city = request.form['city']
    data = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a4eb37937d05b86de85a79703099545c'
    ).content
    weather_dict = json.loads(data)
    if (weather_dict['cod'] == 200):
        temprature = weather_dict['main']['temp']
        discription = weather_dict['weather'][0]['description']
        wind = weather_dict['wind']['speed']
        humidity = weather_dict['main']['humidity']
        icon = weather_dict['weather'][0]['icon']

        print(data)

        context = {
            'temp': '%0.2f' % (temprature - 273),
            'disc': discription,
            'wind': wind,
            'humidity': humidity,
            'icon': icon
        }

        return render_template('index.html', weather=context, city=city)
    else:
        return render_template('index.html', city=city)


if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("localhost", 5000, app, use_debugger=True, use_reloader=True)