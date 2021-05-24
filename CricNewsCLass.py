import os
import telebot
import selenium
import requests 
from bs4 import BeautifulSoup
class cricNewsCLass:
    
    def CricNews():
        message=[]
        URL='https://www.cricbuzz.com/cricket-news/latest-news'
        r=requests.get(URL)
        soup=BeautifulSoup(r.content,'html5lib')
        table=soup.find_all('div', attrs={'class':'cb-col cb-col-100 cb-lst-itm cb-pos-rel cb-lst-itm-lg'})
       
        for div in table:
            news=div.text.strip()
            
            link=div.find('a',attrs={'class':'cb-nws-hdln-ancr text-hvr-underline'})
            if(link.has_attr('href')):
                message.append("cricbuzz.com"+link['href'])
        return message
