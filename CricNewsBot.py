import os
import telebot
import selenium
import requests 
from bs4 import BeautifulSoup
from CricNewsCLass import cricNewsCLass

c=cricNewsCLass
news=c.CricNews()

API_KEY='YOUR_API_KEY ###' #from environment variables
bot=telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['news'])

def send(message):
    for i in news:
        bot.send_message(message.chat.id,i)

bot.polling()

