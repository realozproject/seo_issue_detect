import requests as req
from bs4 import BeautifulSoup
import lxml
import pyquery as pq
import re
keyword = input()
hit = req.get('https://www.google.co.jp/search?num=3&q= '+keyword)
date1 = hit.headers['Date']
if(date1):
    print(date1)

soup = BeautifulSoup(hit.text,"lxml")
date = soup.select('.s > .st')
strdate = "".join(map(str,date))
predate2 = strdate.replace('class="st">',' ')
predate2 = predate2.replace(' ','\n')

a = predate2.splitlines()
a_in = [s for s in a if '年' in s ]
a_in = [s for s in a_in if '月' in s ]
a_in = [s for s in a_in if '日' in s ]
print(a_in)


