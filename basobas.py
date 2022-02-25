from bs4 import BeautifulSoup
import requests
from csv import writer

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Dnt": "1",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-5ee7bae0-82260c065baf5ad7f0b3a3e3"
}
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
