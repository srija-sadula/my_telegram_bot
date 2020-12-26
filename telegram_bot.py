!pip3 install adafruit.io
from Adafruit_IO import RequestError, Client, Feed
from Adafruit_IO import Data
username = "Shivani_Pulluru"                   
code = "aio_CByY93NqbkAZqnFP938Svaup22Wc"   
aio = Client(username,code)
!pip install python-telegram-bot

def on(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'light is turning on'
    pic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Green_sphere.svg/1024px-Green_sphere.svg.png'
    bot.send_message(chat_id,txt)
    bot.send_photo(chat_id,pic)
    value = Data(value=1)
    value_send = aio.create_data('lit',value)
    
def off(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'light is turning off'
    pic = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTuueKIndqjMG0rlzPZrO0UUFP6ts8b_CrUIQ&usqp=CAU'
    bot.send_message(chat_id,txt)
    bot.send_photo(chat_id,pic)
    value = Data(value=0)
    value_send = aio.create_data('lit',value)
    u = Updater('1409120167:AAGu_pP6ntFkck-Y7FtxBkbLBrIqQmQiu5M')  
dp = u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()  
