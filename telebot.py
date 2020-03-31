from telegram.ext import Updater
updater = Updater(token='613557360:AAEy2hhuUHbk2ghd1A23E8pGtOtCiIGu_oI', use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#command method execution
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="v6.9\n/start for this message\n/nigga for cute poetry aka BARS\n/bruh for surprise\n/madarchod for haha very nice desi meme\n/caps <text>\nsay the word \"idiot\" for a strongly worded copypasta\n/gay for the gayest picture you can ever find")

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
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('/home/wondercoconut/Downloads/gay.jpg','rb'))

def bop(update,context):
    context.bot.send_voice(chat_id=update.effective_chat.id, voice=open('/home/wondercoconut/Downloads/bebop.mp3', 'rb'))

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

bop_handler = CommandHandler('bop',bop)
dispatcher.add_handler(bop_handler)


def idiot(update, context):
    word=(update.message.text).split()
    f=0
    i=0
    while(True):
        try:
            if(word[i]=="idiot"):
                f=1
            i=i+1
        except:
            break
    
    if(f):
        context.bot.send_message(chat_id=update.effective_chat.id,text="What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills.I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words.You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands.Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue.But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it.You’re fucking dead, kiddo.")

from telegram.ext import MessageHandler, Filters

idiot_handler = MessageHandler(Filters.text,idiot)
dispatcher.add_handler(idiot_handler)

#filter crap


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)



updater.start_polling()