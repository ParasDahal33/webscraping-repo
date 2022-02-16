from bs4 import BeautifulSoup
import requests
from csv import writer

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
r = requests.get(
    'https://basobaas.com/search?q=', headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')
lists = soup.find_all(
    'div', class_="padding-right-remove col-lg-6 col-md-6 col-xl-3")

with open('basobas.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Price']
    thewriter.writerow(header)

    for list in lists:
        title = list.find(
            'h5', class_="title").text.replace('\n', '')
        location = list.find(
            'small').text.split()[-1].replace('\n', '')
        price = list.find(
            'span', class_="price").text.split()[+9].replace('\n', '')

        info = [title, location, price]
        thewriter.writerow(info)
