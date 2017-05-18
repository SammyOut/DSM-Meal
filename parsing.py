import urllib.request
import time
from bs4 import BeautifulSoup
import re

t = time.localtime()
year = str(t.tm_year)
month = str(t.tm_mon).zfill(2)
day = t.tm_mday

url1 = urllib.request.urlopen("http://stu.dje.go.kr/sts_sci_md00_001.do?schulCode=G100000170&schulCrseScCode=4&schulKndScCode=04&schYm="+year+month)
url2 =urllib.request.urlopen("http://dsm2015.cafe24.com")
hurl = urllib.request.urlopen("http://stu.cne.go.kr/sts_sci_md00_001.do?schulCode=N100000269&schulCrseScCode=4&schulKndScCode=04&schYm="+year+month)
durl = urllib.request.urlopen("http://stu.cne.go.kr/sts_sci_md00_001.do?schulCode=N100000154&schulCrseScCode=4&schulKndScCode=04&schYm="+year+month)


soup1 = BeautifulSoup(url1, 'html.parser')
soup2 = BeautifulSoup(url2, 'html.parser')
hsoup = BeautifulSoup(hurl, 'html.parser')
dsoup = BeautifulSoup(durl, 'html.parser')

tomo = (str(soup1.findAll('tbody')[0]).replace('<br/>', '\n').replace('</div></td>','\n').replace('<tbody>', '').replace('<tr>', '').replace('<td>', '').replace('<td class="last">', '').replace('</tr>', '')).split('<div>')
today = soup2.find_all("p","menu")

h = (str(hsoup.findAll('tbody')[0]).replace('<br/>', '\n').replace('</div></td>','\n').replace('<tbody>', '').replace('<tr>', '').replace('<td>', '').replace('<td class="last">', '').replace('</tr>', '')).split('<div>')
d = (str(dsoup.findAll('tbody')[0]).replace('<br/>', '\n').replace('</div></td>','\n').replace('<tbody>', '').replace('<tr>', '').replace('<td>', '').replace('<td class="last">', '').replace('</tr>', '')).split('<div>')

del tomo[0]
del h[0]

def breakfast() :
    breakfast = re.sub('[0-9]','',str(today[0]).replace('<p class="col-9 menu">', '\n[조식]\n').replace('</p>', '').replace('.', '').replace(', ','\n'))+'\n'
    return breakfast
def lunch() :
    lunch = re.sub('[0-9]','',str(today[1]).replace('<p class="col-9 menu">', '\n[중식]\n').replace('</p>', '').replace('.', '').replace(', ','\n'))+'\n'
    return lunch
def dinner() :
    dinner = re.sub('[0-9]','',str(today[2]).replace('<p class="col-9 menu">', '\n[석식]\n').replace('</p>', '').replace('.', '').replace(', ','\n'))+'\n'
    return dinner
def tomorrow() :
    tomorrow = re.sub('[0-9]','',tomo[day+1].replace('.', '').replace('*', '').replace('[중식]', '\n[중식]').replace('[석식]', '\n[석식]'))
    return tomorrow
def day2() :
    day2 = re.sub('[0-9]','',tomo[day+2].replace('.', '').replace('*', '').replace('[중식]', '\n[중식]').replace('[석식]', '\n[석식]'))
    return day2 
def htoday () :
    htoday = re.sub('[0-9]','',h[day].replace('.', '').replace('*', '').replace('[중식]', '\n[중식]').replace('[석식]', '\n[석식]'))
    return htoday
def htomo () :
    htomo = re.sub('[0-9]','',h[day+1].replace('.', '').replace('*', '').replace('[중식]', '\n[중식]').replace('[석식]', '\n[석식]'))
    return htomo

def dtoday() :
    dtoday = re.sub('[0-9]','',d[day].replace('.', '').replace('*', '').replace('[중식]', '\n[중식]').replace('[석식]', '\n[석식]'))
    return dtoday
def dtomo () :
    dtomo = re.sub('[0-9]','',d[day+1].replace('.', '').replace('*', '').replace('[중식]', '\n[중식]').replace('[석식]', '\n[석식]'))
    return dtomo
