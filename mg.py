import requests as req
from bs4 import BeautifulSoup
keyword = input()
url = req.get('https://www.google.co.jp/search?num=1&q=' +keyword)
soup = BeautifulSoup(url.text,"html.parser")
print(soup.html)

