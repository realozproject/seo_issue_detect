import requests as req
from bs4 import BeautifulSoup
import lxml
import re
import datetime
import math

def M(m,y):
    MO  = [31,28,31,30,31,30,31,31,30,31,30,31]
    uru = [31,29,31,30,31,30,31,31,30,31,30,31]
    s=0
    if y%4:
        for i in range(m-1):
            s+=MO[i]
    else:
        for i in range(m-1):
            s+=uru[i]
    return s



def setM(m,y):
    MO  = [31,28,31,30,31,30,31,31,30,31,30,31]
    uru = [31,29,31,30,31,30,31,31,30,31,30,31]
    b=m
    if((y%4==0 and y%100) or y%400!=0):
        for i in  range(len(uru)):
            b-=uru[i]
            if(b<uru[i]):
                return (i+2)
    else:
        for i in  range(len(MO)):
            b-=MO[i]
            if(b<uru[i]):
                return (i+2)

def setY(s):
    return (math.floor(s/365.2425),math.floor(s%365.2425))

keyword = input()
hit = req.get('https://www.google.co.jp/search?num=15&q= '+keyword)
soup = BeautifulSoup(hit.text,"lxml")

prdate = soup.select('.s > .st')
strdate = "".join(map(str,prdate))
predate2 = strdate.replace('class="st">',' ')
predate2 = predate2.replace(' ','\n')
predate2 = predate2.replace('.','\n')
predate2 = predate2.replace('、','\n')
predate2 = predate2.replace(':','\n')


a = predate2.splitlines()
a_in = [s for s in a if '年' in s ]
a_in = [s for s in a_in if '月' in s ]
a_in = [s for s in a_in if '日' in s ]
#print(a_in)
k=0
sumall=0
for i in range(len(a_in)):
    b = int(i)
    a_in_str = "".join(map(str,a_in[b]))
    if(len(a_in_str)>=9 and len(a_in_str)<=11):
        a_in_d = datetime.datetime.strptime(a_in_str,'%Y年%m月%d日')
        sumall+=365.2425*a_in_d.year+M(a_in_d.month,a_in_d.year)+a_in_d.day
        k+=1

sum_ymd = math.floor(sumall/k)
year2,sum_md = setY(sum_ymd)
month2= math.floor(setM(sum_md,year2))
day2 = math.floor(sum_md%30)
print(year2,month2,day2)




