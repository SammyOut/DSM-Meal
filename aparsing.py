import urllib.request
import time
from bs4 import BeautifulSoup
import re

t = time.localtime()
year = str(t.tm_year)
month = str(t.tm_mon).zfill(2)

url = urllib.request.urlopen("http://stu.dje.go.kr/sts_sci_md00_001.do?schulCode=G100000170&schulCrseScCode=4&schulKndScCode=04&schYm="+year+month)
murl = urllib.request.urlopen("http://stu.cne.go.kr/sts_sci_md00_001.do?schulCode=N100000893&schulCrseScCode=4&schulKndScCode=04&schYm="+year+month)
durl = urllib.request.urlopen("http://stu.cne.go.kr/sts_sci_md00_001.do?schulCode=N100000154&schulCrseScCode=4&schulKndScCode=04&schYm="+year+month)
hurl = urllib.request.urlopen("http://stu.cne.go.kr/sts_sci_md00_001.do?schulCode=N100000269&schulCrseScCode=4&schulKndScCode=04&schYm="+year+month)
surl = urllib.request.urlopen("http://stu.cne.go.kr/sts_sci_md00_001.do?schulCode=N100000181&schulCrseScCode=4&schulKndScCode=04&schYm="+year+month)
jurl = urllib.request.urlopen("http://stu.cne.go.kr/sts_sci_md00_001.do?schulCode=N100000157&schulCrseScCode=4&schulKndScCode=04&schYm="+year+month)

soup = BeautifulSoup(url, 'html.parser')
msoup = BeautifulSoup(murl, 'html.parser')
dsoup = BeautifulSoup(durl, 'html.parser')
hsoup = BeautifulSoup(hurl, 'html.parser')
ssoup = BeautifulSoup(surl, 'html.parser')
jsoup = BeautifulSoup(jurl, 'html.parser')

dsm = soup.find_all('td')
myeoncheon = msoup.find_all('td')
dangjin = dsoup.find_all('td')
hoseo = hsoup.find_all('td')
seoya = ssoup.find_all('td')
jeongbo = jsoup.find_all('td')

week = []
mweek = []
dweek = []
hweek = []
sweek = []
jweek = []

daily = []
mdaily = []
ddaily = []
hdaily = []
sdaily = []
jdaily = []

day = []
mday = []
dday = []
hday = []
sday = []
jday = []

for a in dsm:
    week.append(str(a).replace('<br/>', '\n').replace('</div></td>',''))
for a in week:
    daily.append(a.split('<td><div>'))
del daily[0:3]
for a in daily :
    day.append(''.join(a).replace('[','SPL[').split('SPL'))
  
for a in myeoncheon:
    mweek.append(str(a).replace('<br/>', '\n').replace('</div></td>',''))
for a in mweek:
    mdaily.append(a.split('<td><div>'))
for a in mdaily :
    mday.append(''.join(a).replace('[','SPL[').split('SPL'))
    
for a in dangjin:
    dweek.append(str(a).replace('<br/>', '\n').replace('</div></td>',''))
for a in dweek:
    ddaily.append(a.split('<td><div>'))
for a in ddaily :
    dday.append(''.join(a).replace('[','SPL[').split('SPL'))

for a in hoseo:
    hweek.append(str(a).replace('<br/>', '\n').replace('</div></td>',''))
for a in hweek:
    hdaily.append(a.split('<td><div>'))
for a in hdaily :
    hday.append(''.join(a).replace('[','SPL[').split('SPL'))

for a in seoya:
    sweek.append(str(a).replace('<br/>', '\n').replace('</div></td>',''))
for a in sweek:
    sdaily.append(a.split('<td><div>'))
for a in sdaily :
    sday.append(''.join(a).replace('[','SPL[').split('SPL'))

for a in jeongbo:
    jweek.append(str(a).replace('<br/>', '\n').replace('</div></td>',''))
for a in jweek:
    jdaily.append(a.split('<td><div>'))
for a in jdaily :
    jday.append(''.join(a).replace('[','SPL[').split('SPL'))

SchoolMeal = [day,dday,hday,sday,jday, mday]

def bab(school, dayn, meal) :
    if (meal == 0) : return SchoolMeal[school][dayn][1]+'\n'+SchoolMeal[school][dayn][2]+'\n'+SchoolMeal[school][dayn][3]
    else : return SchoolMeal[school][dayn][meal]
