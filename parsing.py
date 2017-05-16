import urllib.request
from bs4 import BeautifulSoup
import re

url = urllib.request.urlopen("http://dsm2015.cafe24.com")
soup = BeautifulSoup(url, 'html.parser')
menu = soup.find_all("p","menu")

def breakfast() :
    breakfast = re.sub('[0-9]','',str(menu[0]).replace('<p class="col-9 menu">', '아침 : ').replace('</p>', '').replace('.', ''))
    return breakfast
def lunch() :
    lunch = re.sub('[0-9]','',str(menu[1]).replace('<p class="col-9 menu">', '점심 : ').replace('</p>', '').replace('.', ''))
    return lunch
def dinner() :
    dinner = re.sub('[0-9]','',str(menu[2]).replace('<p class="col-9 menu">', '저녁 : ').replace('</p>', '').replace('.', ''))
    return dinner
