import requests
from bs4 import BeautifulSoup
import time

URL = 'https://www.amazon.in/dp/B074V23F28/ref=sr_1_2?linkCode=sl2&ie=UTF8&qihd=1566472976&s=dealfromindiadesire&zerotag=amazonindia&ascutog=indiadesire&tag=indiadesirebanner-21'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51'}

page = requests.get(URL, headers = headers)

# print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
# price = soup.find(id="priceblock_dealprice").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
print(price)
