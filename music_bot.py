import requests
from bs4 import BeautifulSoup
import re
import telebot
import urllib.request as urllib2


Token = '869525203:AAGe6c7GLHcDulwD48mzhAGERH_6QME80B8'

bot = telebot.TeleBot(Token)


@bot.message_handler(content_types=['text'])
def handle_start(message):
    def save():
        url = 'https://zaycev.net/search.html?query_search=' + str(message.text)
        page = requests.get(url).text
        soup = BeautifulSoup(page, "html.parser")
        match1 = soup.find_all('a', class_="musicset-track__link")
        match1 = str(match1[1])
        match1 = re.findall(r'/\w+/\w+/\w+.\w+', match1)
        match1 = "https://zaycev.net" + match1[0]
        url = str(match1)
        page = requests.get(url).text
        soup = BeautifulSoup(page, "html.parser")
        match2 = soup.find_all('a', class_="button-download__link")
        match2 = str(match2)
        match2 = match2.split()
        print(match2)
        match2 = match2[3]
        match2 = re.split(r'"', match2)
        match2 = match2[1]
        match2 = str(match2)
        return match2
    urllib2.urlretrieve(save(), message.text)
    img = open(message.text, 'rb')
    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_audio(message.from_user.id, img)
    img.close()


bot.polling(none_stop=True)