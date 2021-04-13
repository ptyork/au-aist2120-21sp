import requests
import bs4

URL = 'https://automatetheboringstuff.com/2e/chapter12/'

response = requests.get(URL)

if response.ok == False:
    print(f"ERROR {response.status_code}")
    exit()

# soup = bs4.BeautifulSoup(response.text)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

# print(soup)
# print(soup.text)

elems = soup.select('h2')
# print(len(elems))
# print(elems)

title_elem = elems[0]
title = title_elem.text
print(title)

print()
print("TABLE OF CONTENTS")

tocs = soup.select('h3')
for toc_elem in tocs:
    print(f" * {toc_elem.text}")


codes = soup.select('.programs')
for code_elem in codes:
    print('='*80)
    print(f"{code_elem.text}")
    

