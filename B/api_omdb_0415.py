import logging
import requests
import json
from pprint import pformat
import sys

with open('\\apikeys.json') as fi:
    apikeys = json.load(fi)

key = apikeys["OMDB"]

URL = 'http://www.omdbapi.com/'

t = ' '.join(sys.argv[1:])

movie_query = {
    "apikey": key,
    "t": t
}

resp = requests.get(URL, movie_query)

# print(resp.text)

mdata = json.loads(resp.text)

title = mdata["Title"]
year = mdata["Year"]
rated = mdata["Rated"]
plot = mdata["Plot"]
rating = mdata["imdbRating"]
otherRatings = mdata["Ratings"]
poster = mdata["Poster"]

print(f"TITLE:\t{title}")
print(f"YEAR:\t{year}")
print(f"RATED:\t{rated}")
print(f"RATING:\t{rating}")
print(f"PLOT:")
print(plot)

print("OTHER RATINGS")
for r in otherRatings:
    print(f" * {r['Source']} -- {r['Value']}")

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
