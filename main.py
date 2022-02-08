from bs4 import BeautifulSoup
import requests
from csv import writer

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
r = requests.get(
    'https://www.realestateinnepal.com/top-listing/', headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')
lists = soup.find_all('div', class_="shadow border-bottom border-primary mb-4")

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Price']
    thewriter.writerow(header)

    for list in lists:
        title = list.find(
            'a', class_="text-white").text.replace('\n', '')
        location = list.find(
            'small').text.replace('\n', '')
        price = list.find(
            'h4').text.replace('\n', '')

        info = [title, location, price]
        thewriter.writerow(info)
