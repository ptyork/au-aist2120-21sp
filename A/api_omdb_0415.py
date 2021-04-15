import requests
import json
import sys

with open('\\apikeys.json') as fi:
    apikeys = json.load(fi)

key = apikeys["OMDB"]

stitle = ' '.join(sys.argv[1:])

query = {
    "apikey": key,
    "t": stitle
}

resp = requests.get("http://www.omdbapi.com/", params=query)

# print(resp.text)

movdata = json.loads(resp.text)

title = movdata["Title"]
year = movdata["Year"]
rated = movdata["Rated"]
plot = movdata["Plot"]
rating = movdata["imdbRating"]
poster = movdata["Poster"]

print(f"TITLE:\t{title}")
print(f"YEAR:\t{year}")
print(f"RATED:\t{rated}")
print(f"RATING:\t{rating}")
print(f"PLOT:\n{plot}")

FILE_NAME = f"{title}.jpg"
try:
    response = requests.get(poster)
    response.raise_for_status()
    with open(FILE_NAME, 'wb') as output_file:
        for chunk in response.iter_content(100000):
            output_file.write(chunk)
except requests.HTTPError as ex:
    logging.error(f'Unable to retrieve requested resource: {ex}')
except Exception as ex:
    logging.error(f'An unexpected error has occurred: {ex}')

