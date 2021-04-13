# download a resource

import requests

URL = 'https://automatetheboringstuff.com/2e/chapter12/'
FILE_NAME = 'unknown.html'

response = requests.get(URL)
# print(response)
if response.ok == True:
    # Process response
    # print(response.content)
    with open(FILE_NAME, 'wb') as output_file:
        for chunk in response.iter_content(100000):
            output_file.write(chunk)
else:
    print(f'ERROR: {response.status_code}')
