import requests
import json
import sys

# print(sys.argv)
# sys.exit()

with open('\\apikeys.json') as fi:
    apikeys = json.load(fi)

key = apikeys["OpenWeather"]
zip = sys.argv[1]

query = {
    "zip": zip,
    "appid": key,
    "units": "imperial"
}

resp = requests.get("https://api.openweathermap.org/data/2.5/weather", params=query)

# print(resp.text)

wdata = json.loads(resp.text)

city = wdata["name"]
desc = wdata["weather"][0]["description"]
temp = wdata["main"]["temp"]

print(f"The weather in {city} is {desc} and the temp is {temp:.0f} degrees")


