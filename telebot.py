from telegram.ext import Updater,CommandHandler,MessageHandler, Filters 
import logging

def getToken():
    tokenFile = open('/home/wondercoconut/python3/botshit/token.txt','r')
    tokentxt = tokenFile.read()
    Token = tokentxt.split('\n')
    return Token[0]

#methods for all the wack shit the bot actually does

def getwoke(update, context):
    update.message.reply_text("v16.0"
    "\npress F to pay respects"
    "\n/getwoke for this message"
    "\n/nigga for cute poetry aka BARS"
    "\n/bruh for surprise"
    "\n/madarchod for haha very nice desi meme"
    "\n/caps <text>"
    "\nsay the word \"idiot\" for a strongly worded copypasta"
    "\n/gay for the gayest picture you can ever find\n/bop for a bop"
    "\n/wonder for a retarded fuck portrait"
    "\npigeon for something"
    "\nbe horny"
    "\n/engage to remove the big guns"
    "\n/art for a personification of the internet"
    "\nnice for a ceaser"
    "\nmuda"
    "\nask him what bear is best"
    "\nwhat what what what"
    "\nbible time ezekiel boy")

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

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

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

def art(update,context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo= open('/home/wondercoconut/Downloads/art.png','rb'))

def pigeon(update,context):
    word=(update.message.text).split()
    f=0
    i=0
    while(True):
        try:
            s=word[i].lower()
            if (s=='f'):
                f=10
            if(s=='gopika'):
                f=1
            if(s=='pigeon'):
                f=2
            if(s=='sex' or s=='sexy'):
                f=3
            if(s=='idiot'):
                f=4
            if(s=='nice'):
                f=5
            if(s=='muda'):
                f=6
            if(s=='ora'):
                f=7
            if(s=='what'):
                f=8
            if(s=='righteous'):
                f=9
            i=i+1
        except:
            break
    if f==10:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('/home/wondercoconut/Downloads/raspi.jpg','rb'))
        context.bot.send_message(chat_id=update.effective_chat.id, text='F')
    if f==1:
        context.bot.send_message(chat_id=update.effective_chat.id, text="gopika randi")
    if f==2 : 
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('/home/wondercoconut/Downloads/pigeon.jpg','rb'))
        context.bot.send_message(chat_id=update.effective_chat.id,text='gang shit')
    if f==3:
        context.bot.send_message(chat_id=update.effective_chat.id, text="you're gonna die a virgin you incel fuck")
    if f==4:
        context.bot.send_message(chat_id=update.effective_chat.id, text="okbuddyretard")  
    if f==5:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('/home/wondercoconut/Downloads/ceaser.jpg','rb'))
    if f==6:
        context.bot.send_message(chat_id=update.effective_chat.id, text="ora")
    if f==7:
        context.bot.send_message(chat_id=update.effective_chat.id, text="muda")
    if f==8:
        context.bot.send_message(chat_id=update.effective_chat.id, text="SAY WHAT AGAIN I DARE YA I DOUBLE DARE YA MOTHERFUCKER SAY WHAT ONE MORE GODDAMN TIME")
    if f==9:
        s='''ezekiel 25:17
        the path of the righteous man is 
        beset on all sides by the inequities 
        of the selfish
        and the tyranny of evil men
        blessed is he
        who
        in the name of charity and goodwill
        shepherds the weak through the valley 
        of darkness
        for he is truly his brother's keeper
        and the finder
        of lost children
        And I will strike down upon thee 
        with 
        great vengeance 
        and 
        furious anger
        those who attempt to 
        poison 
        and 
        destroy 
        my brothers
        and you will know
        my name is the LORD
        when I lay my vengeance
        upon Thee.'''
        context.bot.send_message(chat_id=update.effective_chat.id, text=s)

#commands
def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    updater = Updater(token = getToken(), use_context=True)
    dispatcher = updater.dispatcher

    getwoke_handler = CommandHandler('getwoke', getwoke)
    dispatcher.add_handler(getwoke_handler)

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

    art_handler = CommandHandler('art',art)
    dispatcher.add_handler(art_handler)

    pigeon_handler = MessageHandler(Filters.text,pigeon)
    dispatcher.add_handler(pigeon_handler)

    boomer_handler = MessageHandler(Filters.photo,boomer)
    dispatcher.add_handler(boomer_handler)

    caps_handler = CommandHandler('caps', caps)
    dispatcher.add_handler(caps_handler)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()








