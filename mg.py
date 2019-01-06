import requests as req
from bs4 import BeautifulSoup
import lxml
import re
import datetime

keyword = input()
hit = req.get('https://www.google.co.jp/search?num=20&q= '+keyword)

soup = BeautifulSoup(hit.text,"lxml")
prdate = soup.select('.s > .st')
strdate = "".join(map(str,prdate))
predate2 = strdate.replace('class="st">',' ')
predate2 = predate2.replace(' ','\n')

a = predate2.splitlines()
a_in = [s for s in a if '年' in s ]
a_in = [s for s in a_in if '月' in s ]
a_in = [s for s in a_in if '日' in s ]
print(a_in)

year = []
month = []
day = []
for i in range(len(a_in)):
    b = int(i)
    a_in_str = "".join(map(str,a_in[b]))
    if(len(a_in_str)>=9 and len(a_in_str)<=11):
        a_in_d = datetime.datetime.strptime(a_in_str,'%Y年%m月%d日')
        year.append(a_in_d.year)
        month.append(a_in_d.month)
        day.append(a_in_d.day)
#全てを日付に変換
sumall = sum(year)*365+sum(month)*30+sum(day)
uru = sumall/(365*4)
print(uru)
#閏年を踏まえた日付の総和
sum_ymd = sumall-uru
sum_ymd = sum_ymd/len(year)
#年数を365で割りだす
year2 = round(sum_ymd/365,0)
sum_md = sum_ymd%365
#同様に月、日をだす
month2 = round(sum_md/30,0)
day2 = round(sum_md%30,0)

print(year2,month2,day2)

#それぞれの平均値を出す
ave_y = round(sum(year)/len(year),0)
ave_m = round(sum(month)/len(month),0)
ave_d = round(sum(day)/len(day),0)
print(ave_y,ave_m,ave_d)


