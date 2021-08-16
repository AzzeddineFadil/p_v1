import configparser
import telepot
from datetime import datetime
import time
import numpy
from botsupre import getinfo

config = configparser.ConfigParser()
config.read("config.ini")
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
bot_token = str(config["Telegram"]["bot_token"])

bot = telepot.Bot(bot_token)

def handle(msg):
    user_name = msg["from"]["first_name"] + " " + msg["from"]["last_name"]
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == "text":
        my_command = msg["text"]
        if "/start" in my_command:
            bot.sendMessage(chat_id, "Welcome "+user_name+" in your new bot!" )
        elif "/help" in my_command:
            bot.sendMessage(chat_id, "No help!" )
        elif "hi bot how are you" in my_command:
            bot.sendMessage(chat_id, "I am fen "+user_name+"\n"+" and you" ) 
        elif "give me sr coin" in (my_command).lower():
            
            bot.sendMessage(chat_id,"ok sure : \ngive me name coin and interval :\nexe : BTCUSDT 15m ....")
  
        else:
            li = list(my_command.split(" "))
            message =  getinfo.get_SR(str(li[0]).upper(),str(li[1]).lower())

            bot.sendMessage(chat_id, message[0]+' \n'+message[1] )
           
            

bot.message_loop(handle)

while True:
    time.sleep(20)
