import requests
import json
from flask import Flask

app = Flask(__name__)
#weather api key = c7135aba3e647339518f4b3096d32f38



@app.route("/")
def hello():
    city_name = "Atlanta"
    url = "https://samples.openweathermap.org/data/2.5/weather?q={}&appid=c7135aba3e647339518f4b3096d32f38".format(city_name)
    res = requests.get(url)
    content = json.loads(res.content)
    weather = content.get("weather")[0]
    main_condition = weather.get("main")
    description = weather.get("description")
    stats = content.get("main")
    temp = stats.get("temp")
    humidity = stats.get("humidity")
    data = {"main":main_condition, "description":description, "temp":temp, "humidity":humidity}
    return json.dumps(data)
    



