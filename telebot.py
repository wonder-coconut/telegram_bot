from telegram.ext import Updater
updater = Updater(token='613557360:AAEy2hhuUHbk2ghd1A23E8pGtOtCiIGu_oI', use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#command method execution
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="v5.0\n/start for this message\n/nigga for cute poetry aka BARS\n/bruh for surprise\n/madarchod for haha very nice desi meme\n/caps <text>")

def nigga(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="fuck bitches, get money nigga cat nigga cat")

def bruh(update,context):
    i=0
    st1="bruh"
    st2="moment"
    while(i<20):
        str=st1+8*(i%5)*' '+st2
        context.bot.send_message(chat_id=update.effective_chat.id, text=str)
        i=i+1
    context.bot.send_message(chat_id=update.effective_chat.id, text="F in the chat")

def madarchod(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="mai madarchod hoon jo isme aaya")



#commands
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

nigga_handler = CommandHandler('nigga',nigga)
dispatcher.add_handler(nigga_handler)

bruh_handler = CommandHandler('bruh',bruh)
dispatcher.add_handler(bruh_handler)

madarchod_handler = CommandHandler('madarchod',madarchod)
dispatcher.add_handler(madarchod_handler)



#echoes messages
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text=update.message.text)

from telegram.ext import MessageHandler, Filters

#echo_handler = MessageHandler(Filters.text,echo)
#dispatcher.add_handler(echo_handler)

#filter crap

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

#def neural(update, context):
    #context.bot.send_message(chat_id=update.effective_chat.id, text="mkc do I look like a neural network to you")

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)


updater.start_polling()