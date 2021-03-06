import telebot
from PIL import Image
import data
import os


bot = telebot.TeleBot(data.TOKEN)

@bot.message_handler(commands=['команды','помощь','help'])
def help(message):
    bot.send_message(message.chat.id, '/дз - выводить список домашнего задания на следующий учебный день, /дистант - выводит список ближайших дистанционных занятий, /пары - выводит расписани на следующий учебный день')

@bot.message_handler(commands=['Расписание','уроки','что завтра','пары'])
def allles(message):
    allles = open('files/schedule.txt')
    bot.send_message(message.chat.id, allles)


@bot.message_handler(commands=['Уроки','зум','дистант','Дистант'])
def les(message):
    les = open('files/lessons.txt')
    bot.send_message(message.chat.id, les)


@bot.message_handler(commands=['start','дз','ДЗ','Дз'])
def hw(message):
    hw = open('files/hw.txt','r')
    
    bot.send_message(message.chat.id, hw)

    files = os.listdir(path="files")
    if len(files) >= 4:
        hwi = open('files/photo.jpg', 'rb')
        bot.send_photo(message.chat.id, hwi)
        hwi.close

    if len(files) >= 5:
        hwi = open('files/photo2.jpg', 'rb')
        bot.send_photo(message.chat.id, hwi)
        hwi.close

    if len(files) >= 6:
        hwi = open('files/photo3.jpg', 'rb')
        bot.send_photo(message.chat.id, hwi)
        hwi.close    

    if len(files) >= 7:
        hwi = open('files/photo4.jpg', 'rb')
        bot.send_photo(message.chat.id, hwi)
        hwi.close



bot.polling(none_stop=True)
