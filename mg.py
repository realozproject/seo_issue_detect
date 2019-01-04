import requests as req
from bs4 import BeautifulSoup
import lxml
import pyquery as pq
keyword = input()
hit = req.get('https://www.google.co.jp/search?num=2&q= '+keyword)
date1 = hit.headers['Date']
if(date1):
    print(date1)


#soup = BeautifulSoup(hit.text,"lxml")
#date = soup.select('.s > .st')
#print(date)
