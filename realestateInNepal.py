from bs4 import BeautifulSoup
import requests
import re
from csv import writer

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
r = requests.get(
    'https://www.realestateinnepal.com/search/?location=', headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')
lists = soup.find_all('div', class_="shadow border-bottom border-primary mb-4")

with open('realestateInNepal.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Price', 'Image']
    thewriter.writerow(header)

    for list in lists:
        title = list.find(
            'a', class_="text-white").text.replace('\n', '')
        location = list.find(
            'span', class_="locationko text-white").text.split()[-1].replace('\n', '')
        priceOne = list.find(
            'div', class_="bg-white p-3").text.split()[+9].replace('\n', '')
        image = list.find(
            'img')['src']
        price = re.sub('[^0-9]', '', priceOne)
        info = [title, location, price, image]
        thewriter.writerow(info)
