from flask import Flask, render_template, request
from weather import getCurrentWeather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
@app.route('/weather')
def getWeather():
    city = request.args.get('city')
    weather_data = getCurrentWeather(city)

    # city is not found by API
    if not weather_data['cod'] == 200:
        return render_template("city_not_found.html")
    return render_template (
        'weather.html',
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp = f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}")

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)