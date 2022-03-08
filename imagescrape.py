from bs4 import BeautifulSoup
import requests
import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
r = requests.get(
    'https://www.realestateinnepal.com/search/?location=', headers=headers).text

soup = BeautifulSoup(r, "lxml")
images = soup.find_all("img", class_="img-fluid w-100 owl-lazy")
number = 0
for image in images:
    image_src = image["src"]
    print(image_src)
    urllib.request.urlretrieve(image_src, str(number))
    number += 1
