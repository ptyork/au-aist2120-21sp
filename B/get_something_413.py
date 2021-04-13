import requests

URL = 'https://automatetheboringstuff.com/2e/chapter12/'
# URL = 'https://automatetheboringstuff.com/2e/chapter120/'

response = requests.get(URL)
# print(response)
# print(response.content)
print(response.text)
print(response.status_code)

FILE_NAME = "something.html"
# if response.status_code != 200:
if response.ok == False:
    print(f"ERROR {response.status_code}")
    exit()

with open(FILE_NAME, 'wb') as output_file:
    for chunk in response.iter_content(100000):
        output_file.write(chunk)
