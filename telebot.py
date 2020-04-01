from telegram.ext import Updater
updater = Updater(token='613557360:AAEy2hhuUHbk2ghd1A23E8pGtOtCiIGu_oI', use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#command method execution
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="v11.0"
    "\n/start for this message"
    "\n/nigga for cute poetry aka BARS"
    "\n/bruh for surprise"
    "\n/madarchod for haha very nice desi meme"
    "\n/caps <text>"
    "\nsay the word \"idiot\" for a strongly worded copypasta"
    "\n/gay for the gayest picture you can ever find\n/bop for a bop"
    "\n/wonder for a retarded fuck portrait"
    "\npigeon for something"
    "\nbe horny"
    "\n/engage to remove the big guns")

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

def gay(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="please be patient you imbecile")
    context.bot.send_voice(chat_id=update.effective_chat.id, voice=open('/home/wondercoconut/Downloads/robbers.mp3', 'rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('/home/wondercoconut/Downloads/gay.jpg','rb'))

def bop(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="please be patient you imbecile")
    context.bot.send_voice(chat_id=update.effective_chat.id, voice=open('/home/wondercoconut/Downloads/bebop.mp3', 'rb'))

def wonder(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="please be patient you imbecile")
    context.bot.send_voice(chat_id=update.effective_chat.id, voice=open('/home/wondercoconut/Downloads/wonder.mp3', 'rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('/home/wondercoconut/Downloads/randi.jpg','rb'))

def boomer(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="ok boomer")

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

gay_handler = CommandHandler('gay',gay)
dispatcher.add_handler(gay_handler)

wonder_handler = CommandHandler('wonder',wonder)
dispatcher.add_handler(wonder_handler)

bop_handler = CommandHandler('bop',bop)
dispatcher.add_handler(bop_handler)

engage_handler = CommandHandler('engage',boomer)
dispatcher.add_handler(engage_handler)

def pigeon(update,context):
    word=(update.message.text).split()
    f=0
    i=0
    while(True):
        try:
            if(word[i].lower()=='gopika'):
                f=1
            if(word[i].lower()=='pigeon'):
                f=2
            elif(word[i].lower()=='sex' or word[i].lower()=='sexy'):
                f=3
            elif(word[i].lower()=='idiot'):
                f=4
            
            i=i+1
        except:
            break
    
    if f==1:
        context.bot.send_message(chat_id=update.effective_chat.id, text="gopika randi")
    elif f==2 :
        
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('/home/wondercoconut/Downloads/pigeon.jpg','rb'))
        context.bot.send_message(chat_id=update.effective_chat.id,text='gang shit')
    elif f==3:
        context.bot.send_message(chat_id=update.effective_chat.id, text="you're gonna die a virgin you incel fuck")
    elif f==4:
        context.bot.send_message(chat_id=update.effective_chat.id, text="okbuddyretard")  

#filters

from telegram.ext import MessageHandler, Filters

pigeon_handler = MessageHandler(Filters.text,pigeon)
dispatcher.add_handler(pigeon_handler)

#boomer_handler = MessageHandler(Filters.photo,boomer)
#dispatcher.add_handler(boomer_handler)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)



updater.start_polling()