from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html=urlopen("http://en.wikipedia.org"+articleUrl)
    bs0bj=BeautifulSoup(html)
    return bs0bj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
links=getLinks("/wiki/kevin_Bacon")
while len(links)>0:
    newArticule=links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticule)
    links=getLinks(newArticule)
