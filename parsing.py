import urllib.request
import time
from bs4 import BeautifulSoup
import re

t = time.localtime()
year = str(t.tm_year)
month = str(t.tm_mon).zfill(2)
dayn = t.tm_mday

url = urllib.request.urlopen("http://stu.dje.go.kr/sts_sci_md00_001.do?schulCode=G100000170&schulCrseScCode=4&schulKndScCode=04&schYm="+year+month)
soup = BeautifulSoup(url, 'html.parser')

dsm = soup.find_all('td')
week = []
daily = []
day = []

for a in dsm:
    week.append(str(a).replace('<br/>', '\n'))
for a in week:
    daily.append(a.split('<td><div>'))
for a in daily :
    day.append(''.join(a).replace('[','SPL[').split('SPL'))

    
def br() : return day[dayn][1]
def lu() : return day[dayn][2]
def di() : return day[dayn][3]
def tod() : return day[dayn][1]+'\n'+day[dayn][2]+'\n'+day[dayn][3]

def tb() : return day[dayn+1][1]
def tl() : return day[dayn+1][2]
def td() : return day[dayn+1][3]
def tom() : return day[dayn+1][1]+'\n'+day[dayn+1][2]+'\n'+day[dayn+1][3]

def tt() :return day[dayn+2][1]+'\n'+day[dayn+2][2]+'\n'+day[dayn+2][3]
