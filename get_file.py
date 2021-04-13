import requests
import logging

# Sample code to download and save a resource from the web
URL = "https://www.augusta.edu/faculty/directory/images/faculty/pyork1.jpg"
FILE_NAME = "me.jpg"

# Note that you can often "compute" the file name from the URL, which
# can be useful in situations where you are retrieving the URL from
# <img> or <a> elements on the page itself.
FILE_NAME = URL.split('/')[-1]  # split on "/" and take last string from the list

print(f"Getting {FILE_NAME}...")

try:
    response = requests.get(URL)
    response.raise_for_status()
    with open(FILE_NAME, 'wb') as output_file:
        for chunk in response.iter_content(100000):
            output_file.write(chunk)
except requests.HTTPError as ex:
    logging.error(f'Unable to retrieve requested resource: {ex}')
except Exception as ex:
    logging.error(f'An unexpected error has occurred: {ex}')

