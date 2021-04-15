import requests
import json
import sys

with open('\\apikeys.json') as fi:
    apikeys = json.load(fi)

key = apikeys["OpenWeather"]

URL = 'http://api.openweathermap.org/data/2.5/weather'

if len(sys.argv) == 2:
    zip = sys.argv[1]
else:
    print("GIMME A ZIP")
    exit()

weather_query = {
    "appid": key,
    "zip": zip,
    "units": "imperial"
}

resp = requests.get(URL, weather_query)

# print(resp.text)

wdata = json.loads(resp.text)

# print(wdata["name"])

city = wdata["name"]
descr = wdata["weather"][0]["description"]
temp = wdata["main"]["temp"]

print(f"The weather in {city} is {descr} and it is {temp:.0f} degrees")
