import os
import telebot
import selenium
import requests 
from bs4 import BeautifulSoup
from CricNewsCLass import cricNewsCLass

c=cricNewsCLass
news=c.CricNews()

API_KEY='1834421047:AAFM_dDrQuJOeC7pjY5UYy09pRuvnFGoMuU'
bot=telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['news'])

def send(message):
    for i in news:
        bot.send_message(message.chat.id,i)

bot.polling()

