import urllib.request
import fbchat
import getpass
from bs4 import BeautifulSoup
import re

url = urllib.request.urlopen("http://dsm2015.cafe24.com")
soup = BeautifulSoup(url, 'html.parser')
menu = soup.find_all("p","menu")

breakfast = re.sub('[0-9]','',str(menu[0]).replace('<p class="col-9 menu">', '아침 : ').replace('</p>', '').replace('.', ''))
lunch = re.sub('[0-9]','',str(menu[1]).replace('<p class="col-9 menu">', '점심 : ').replace('</p>', '').replace('.', ''))
dinner = re.sub('[0-9]','',str(menu[2]).replace('<p class="col-9 menu">', '저녁 : ').replace('</p>', '').replace('.', ''))
client = fbchat.Client("sm3721@nate.com", getpass.getpass('PW : '))

sent = client.send(input('페이스북 친구 uid : '), breakfast+'\n'+lunch+'\n'+dinner)
