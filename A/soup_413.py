import requests
import bs4

URL = 'https://automatetheboringstuff.com/2e/chapter12/'

response = requests.get(URL)
# print(response)
if response.ok == True:
    # Process response
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    # print(soup)
    elems = soup.select('h2')
    # print(len(elems))
    title = elems[0]
    print(title.text)

    print("TABLE OF CONTENTS")
    elems = soup.select('h3')
    for elem in elems:
        print(f'\t{elem.text}')

    print()
    print("CODE SAMPLES ON THIS PAGE")
    # elems = soup.select('.codestrong1')
    elems = soup.select('.programs')
    for elem in elems:
        print()
        # print(f'{elem.text}')
        # EACH ELEMENT IS A "SUB-SOUP" AND CAN BE SEARCHED
        elems2 = elem.search('span')
        for e2 in elems2:
            print(e2.text)

else:
    print(f'ERROR: {response.status_code}')
