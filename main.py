import telebot
import shutil
import instaloader
from instaloader import Profile, Post
import os
from deep_translator import GoogleTranslator
import sqlite3
from gtts import gTTS
import time
import random
import wikipedia as wiki
import requests
import qrcode
import cv2
from pyzbar import pyzbar
from flask import Flask, request

secret = '3h2g2g32hj3g232g3j2gj1g3j12g3j2h3g2hg3'
url = 'https://mikeykun.pythonanywhere.com/' + secret
token = '6188240649:AAGo4f0_BGg8JCXTZhIlWD4V6BHT7sJKmpo'

wiki.set_lang("uz")

bot = telebot.TeleBot(token, threaded = False)
bot.remove_webhook()
bot.set_webhook(url = url)

app = Flask(__name__)

@app.route('/' + secret, methods = 'POST')
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "ok", 200

global bad_says
bad_says = ['dnx', 'pwnx', 'pashol nax', 'pawol nax', 'idi nax', 'xarp', 'harp', 'harip', 'xarip']

button = telebot.types.ReplyKeyboardMarkup(True)
button.row("Qr Scanning", "Animes")
button.row("Commands", "Docs")

button2 = telebot.types.ReplyKeyboardMarkup(True)
button2.row("5", "10", "20")
button2.row("25", "30", "40")
button2.row("45", "50", "60")
button2.row("65", "70", "80")
button2.row("back")


@bot.message_handler(commands = ['start'])
def start_message(message):
    if message.chat.type == 'private':
        bot.reply_to(message, '02', reply_markup = button)
    else:
        bot.reply_to(message, '02')


@bot.message_handler(content_types = ['new_chat_members'])
def send_message(message):
    bot.send_message(message.chat.id, f'Hello <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> Welcome to group!', parse_mode = 'HTML')
    bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(content_types = ['left_chat_member'])
def send_message(message):
    bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(content_types = ['new_chat_title'])
def send_message(message):
    bot.delete_message(message.chat.id, message.message_id)

# @bot.message_handler(func=lambda m: m.entities is not None and m.chat.id == m.chat.id)
# def delete_links(m):
#     member = bot.get_chat_member(m.chat.id, m.from_user.id)
#     if member.status == 'administrator':
#         bot.send_chat_action(m.chat.id, action = 'typing')
#     else:
#         for entity in m.entities:
#             if entity.type in ["url", "text_link"]:
#                 return bot.delete_message(m.chat.id, m.message_id)


@bot.message_handler(content_types = ['text'])
def send_message(message):
    if message.text.lower() == '02':
        bot.send_message(message.chat.id, ".")

    elif message.text.lower() == "v :: 02":
        bot.send_message(message.chat.id, "version: 23.5")

    elif message.text.lower() in bad_says:
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower() == ".commands":
        bot.send_message(message.chat.id, "Commands,\n\nInstagram reel downloading - .d\nText to audio en/ru - ..rc/.rc <your text>\nVersion info - v :: 02\nGroup/user id - ..id/.id\nPinning messages - .pin/.unpin")

    elif message.text.lower() == "commands":
        bot.send_message(message.chat.id, "Commands,\n\nhttps://telegra.ph/Zero-Two--123-07-26")

    elif message.text.lower() == "docs":
        bot.send_message(message.chat.id, "Documentation:\n\nhttps://telegra.ph/Zero-Two--123-07-26")

    elif message.text.lower() == "group managing":
        bot.send_message(message.chat.id, "Developing yet...")

    elif message.text.lower() == "<=":
        bot.send_message(message.chat.id, "Animes", reply_markup = button)

    elif message.text.lower() == "?:: i'm right?":
        bot.send_message(message.chat.id, "Yes! you right!")
        time.sleep(10)
        bot.send_message(message.chat.id, "That's why you geniy 😂")
        time.sleep(5)
        bot.send_message(message.chat.id, "#joke")

    elif message.text.lower() == "?:: 0 0":
        bot.send_chat_action(message.chat.id, action = 'typing')
        time.sleep(10)
        bot.send_message(message.chat.id, "i'm jokeed o o")

    elif message.text.lower() == ".da":
        bot.send_message(message.chat.id, "da jonim")
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower() == "pfff":
        bot.send_chat_action(message.chat.id, action = 'typing')
        time.sleep(10)
        bot.send_message(message.chat.id, "0 <")

    elif message.text.lower() == ".xiii":
        bot.send_chat_action(message.chat.id, action = 'typing')
        bot.send_message(message.chat.id, "😁")
        # bot.delete_message(message.chat.id, message.message_id) 

    elif message.text.lower() == ".0 0":
        bot.send_chat_action(message.chat.id, action = 'typing')
        bot.send_message(message.chat.id, "0 0")
        bot.delete_message(message.chat.id, message.message_id) 

    elif message.text.lower() == ".02hack":
        bot.send_chat_action(message.chat.id, action = 'typing')
        bot.send_message(message.chat.id, "02 is hacked from @mikey_im x @code_idea check your security")
        bot.delete_message(message.chat.id, message.message_id) 

    elif message.text.lower() == ".kick":
        bot.send_message(message.chat.id, f"{message.from_user.first_name} is kicked -> {message.reply_to_message.from_user.first_name}")
        # bot.delete_message(message.chat.id, message.message_id) 

    elif message.text.lower() == ".five":
        bot.send_message(message.chat.id, f"{message.from_user.first_name} is gived five -> {message.reply_to_message.from_user.first_name}")
        # bot.delete_message(message.chat.id, message.message_id) 

    elif message.text.lower().startswith('.nqr '):
        img = qrcode.make(message.text[4:])
        img.save('qrcode.png')

        bot.send_photo(message.chat.id, photo = open('qrcode.png', 'rb'))

    elif message.text.lower() == "qr scanning":
        if message.chat.type == 'private':
            bot.send_message(message.chat.id, ":$ please, send your qr photo")
            bot.register_next_step_handler(message, qrscan)

            

    elif message.text.lower().startswith(".wiki "):
        res = wiki.summary(f"{message.text[6:]}")
        bot.send_message(message.chat.id, res)
        print(res)

    elif message.text.lower().startswith("?.d "): # 4:
        try:
            global id
            id = message.text[4:]
            bot.send_message(message.chat.id, "?:: your message: ")
            bot.register_next_step_handler(message, send_id)
        except Exception as e:
            bot.send_message(message.chat.id, f"::Error:: {e}")



    elif message.text.lower().startswith("?.s "): # 4:
        try:
            global u_name
            u_name = message.text[4:]
            bot.send_message(message.chat.id, "?:: your message: ")
            bot.register_next_step_handler(message, send)
        except Exception as e:
            bot.send_message(message.chat.id, f"::Error:: {e}")


    elif message.text.lower() == "?:: sms :: conf :: st ?: a":
        with open('smsconf.txt', 'w') as f:
            f.write('a')
        bot.send_message(message.chat.id, "02 hacker :$ sms conf is active")

    elif message.text.lower() == "?:: sms :: conf :: st ?: un":
        with open('smsconf.txt', 'w') as f:
            f.write('un')
        bot.send_message(message.chat.id, "02 hacker :$ sms conf is unactive")

    elif message.text.lower().startswith("?:: sms "):
        with open('smsconf.txt', 'r+') as f:
            list = f.read()

            if list == 'a':
                for sms in range(10):
                    smslist = requests.post("https://io.bellissimo.uz/api/verify-web",
                    data = {"phone" : message.text[8:]},)
                    bot.send_message(message.chat.id, f"02 hacker :$ sms T958Script {smslist}")
                    # print(message.text[8])

            else:
                bot.send_message(message.chat.id, f"02 hacker :$ sms conf is not active")

    ### anime

    elif message.text.lower() == "animes":
        if message.chat.type == 'private':
                bot.send_message(message.chat.id, f"02 wallpapers :$ wallpapers range:", reply_markup = button2)
                bot.register_next_step_handler(message, ranges)


                        # for data in range(10):
                        #     bot.send_photo(message.chat.id, photo = open(f'res/anime{data}.jpg', 'rb'))

            # if photos_to_send:
            #     bot.send_media_group(message.chat.id, media=photos_to_send)

        
        



    
    # elif message.text.lower().startswith(".ban "):
    #     member = bot.get_chat_member(message.chat.id, message.from_user.id)
    #     if member.status == 'administrator':
    #         bot.kick_chat_member(message.chat.id, message.reply_to.message.from_user.id)
    #         bot.send_message(message.chat.id, 
    #                          f"<b>{message.reply_to.message.from_user.first_name}</b> забанен!\n",
    #                          f"Админ: {message.from_user.id}\n",
    #                          f"причина: {message.text[5:]}", 
    #                          parse_mode = 'HTML')
    #         bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower().startswith(".ban "):
        member = bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status == 'administrator' or 'creator':
            bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"🔴 {message.reply_to_message.from_user.first_name} is banned!\nAdmin: {message.from_user.first_name}\nCause: {message.text[5:]}")
            bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower().startswith(".fly "):
        member = bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status == 'administrator' or 'creator':
            bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"✈️ {message.reply_to_message.from_user.first_name} is flied to dubai!\nAdmin: {message.from_user.first_name}\nCause: {message.text[5:]}")
            bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower().startswith(".boom "):
        member = bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status == 'administrator' or 'creator':
            bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"🔥 {message.reply_to_message.from_user.first_name} is boomed!\nAdmin: {message.from_user.first_name}\nCause: {message.text[5:]}")
            bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower().startswith("free ban :: mode"):
            bot.send_message(message.chat.id, "cheat mode :: st $$ on")
            bot.delete_message(message.chat.id, message.message_id)


    elif message.text.lower().startswith(".ch ban "):
            bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.first_name} is banned with cheat ban!\nAdmin: {message.from_user.first_name}\nCause: {message.text[8:]}", 
                            )
            bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower().startswith(".unban "):
        member = bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status == 'administrator' or 'creator':
            bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"🟢 {message.reply_to_message.from_user.first_name} is unbanned!\nCause: {message.text[7:]}")
            bot.delete_message(message.chat.id, message.message_id)

    ### mute unmute

    elif message.text.lower().startswith(".mute "):
        member = bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status == 'administrator' or 'creator':
            bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.first_name} is muted!\nCause: {message.text[6:]}")
            bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower().startswith(".unmute "):
        member = bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status == 'administrator' or 'creator':
            bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.first_name} is unmuted!\nCause: {message.text[8:]}")
            bot.delete_message(message.chat.id, message.message_id)

    ### group configurations

    elif message.text.lower() == ".pin":
        member = bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status == 'administrator' or 'creator':
            bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
            bot.delete_message(message.chat.id, message.message_id) 

    elif message.text.lower() == ".unpin":
        member = bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status == 'administrator' or 'creator':
            bot.unpin_chat_message(message.chat.id, message.reply_to_message.message_id)
            bot.delete_message(message.chat.id, message.message_id) 

    elif message.text.lower().startswith(".n "):
        member = bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status == 'administrator' or 'creator':
            bot.edit_chat_title(message.chat.id. message.text[3:])
            bot.delete_message(message.chat.id, message.message_id) 

    elif message.text.lower() == ".give":
        bot.send_message(message.chat.id, message.from_user.first_name + ' gived ' + 
                                          message.reply_to_message.from_user.first_name,
                                        )
        
    elif message.text.lower() == ".admin":
        bot.promote_chat_member(message.chat.id, can_delete_messages = True, )
        # member = bot.get_chat_member(message.chat.id. message.from_user.id)
        # if member.status == 'administrator':
            # bot.send_message(message.chat.id, message.member.username)

            # eval


    elif message.text.lower() == ".id":
        bot.send_message(message.chat.id, f"id: <code>{message.from_user.id}</code>", parse_mode = 'HTML')


    elif message.text.lower() == "..id":
        bot.send_message(message.chat.id, f"id: <code>{message.chat.id}</code>", parse_mode = 'HTML')

    elif message.text.lower().startswith('..nick '):
        db = sqlite3.connect('users.db')
        sql = db.cursor()

        sql.execute(f"""CREATE TABLE IF NOT EXISTS '{message.from_user.id}' (id INTEGER PRIMARY KEY AUTOINCREMENT, nickname TEXT, pic CHAR, bio TEXT)""")
        sql.execute(f"INSERT INTO '{message.from_user.id}' (id, nickname) VALUES (null, '{message.text[7:]}')")
        db.commit()
        bot.send_message(message.chat.id, "Установлен!")
        bot.delete_message(message.chat.id, message.message_id) 

    elif message.text.lower() == ".me":
        # if message.reply_to.message.from_user.id:
            # data = message.reply_to.message.from_user.id
            # bot.send_message(message.chat.id, ".")
        # else:
            db = sqlite3.connect('users.db')
            sql = db.cursor()
            for data in sql.execute(f"SELECT id, nickname FROM '{message.from_user.id}'").fetchall():
            
                bot.send_message(message.chat.id, f'<a href="tg://user?id={message.from_user.id}">{data[1]}</a>', parse_mode = 'HTML')

    elif message.text.lower() == ".nick":
        try:
            db = sqlite3.connect('users.db')
            sql = db.cursor()
            data = sql.execute(f"SELECT nickname FROM '{message.reply_to_message.from_user.id}'").fetchall()
            
            bot.send_message(message.chat.id, data)
        
        except Exception as e:
            bot.send_message(message.chat.id, f'{message.reply_to_message.from_user.first_name}')

    elif message.text.lower().startswith(".rc "):
       try:
           tts = gTTS(text = message.text[4:], lang = "ru")
           filename = "audio.mp3"
           tts.save(filename)

           bot.send_chat_action(message.chat.id, 'record_audio')
           bot.send_audio(message.chat.id, audio = open("audio.mp3", "rb"), caption = "@zerotwo_cmbot")
           bot.delete_message(message.chat.id, message.message_id) 
       except:
           bot.send_message(message.chat.id, "Error!")

    elif message.text.lower().startswith("!rc "):
       try:
           tts = gTTS(text = message.text[4:], lang = "ja")
           filename = "audio.mp3"
           tts.save(filename)

           bot.send_chat_action(message.chat.id, 'record_audio')
           bot.send_audio(message.chat.id, audio = open("audio.mp3", "rb"), caption = "@zerotwo_cmbot")
        #    bot.delete_message(message.chat.id, message.message_id) 
       except:
           bot.send_message(message.chat.id, "Error!")


    elif message.text.lower().startswith("..rc "):
       try:
           tts = gTTS(text = message.text[4:], lang = "en")
           filename = "audio.mp3"
           tts.save(filename)

           bot.send_chat_action(message.chat.id, 'record_audio')
           bot.send_audio(message.chat.id, audio = open("audio.mp3", "rb"), caption = "@zerotwo_cmbot")
           bot.delete_message(message.chat.id, message.message_id) 
       except:
           bot.send_message(message.chat.id, "Error!")

    elif message.text.lower() == ".del":
        bot.delete_message(message.chat.id, message.reply_to_message.message_id)
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower().startswith('.name '):
        member = bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status == 'administrator' or 'creator':
            bot.set_chat_title(message.chat.id, message.text[6:])
            bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower() == ".rd":
        rd_1 = "🟢", "🔴"
        res = random.choice(rd_1)
        bot.send_message(message.chat.id, f"$: {res}")
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower() == "..r":
        rd_1 = "🟢", "🔴"
        res = random.choice(rd_1)
        bot.send_message(message.chat.id, f"$: {res}")
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower() == ".rd":
        rd_1 = "🟢", "🔴"
        res = random.choice(rd_1)
        bot.send_message(message.chat.id, f"$: {res}")
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower() == ".q":
        rd_1 = "yashil", "qizil"
        res = random.choice(rd_1)
        bot.send_message(message.chat.id, f"$: {res}")
        bot.delete_message(message.chat.id, message.message_id)


    elif message.text.lower() == ".y":
        rd_1 = "yashil", "qizil"
        res = random.choice(rd_1)
        bot.send_message(message.chat.id, f"$: {res}")
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower() == ".s":
        rd_1 = "1", "2", "3", "4", "5", "6" 
        res = random.choice(rd_1)
        bot.send_message(message.chat.id, f"$: {res}")
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower() == "..s":
        rd_1 = "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
        res = random.choice(rd_1)
        bot.send_message(message.chat.id, f"$: {res}")
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower().startswith('..m '):
        try:
            bot.send_message(message.chat.id, eval(f"{message.text[4:]}"))
        except Exception as e:
            bot.send_message(message.chat.id, f"Error: {e}, Errors will send to admins")
            bot.send_message(5407368270, f"::log:: {e}")


        
    
        





    ## instagram 
    elif message.text.lower().startswith('.d '):
      try:
        bot.send_message(message.chat.id, "🟢 downloading...")

        print(message.text[3:])

        instance = instaloader.Instaloader()

        post = Post.from_shortcode(instance.context, f"{message.text[3:]}")
      # os.mkdir(f"{message.from_user.id}")

        instance.download_post(post, target = f"{message.from_user.id}")

        for file in os.listdir(f"{message.from_user.id}"):
          if file.endswith(".mp4"):
            video_path = os.path.join(f"{message.from_user.id}", file)
            bot.send_video(message.chat.id, open(video_path, 'rb'), caption = "by @zerotwo_cmbot")


            shutil.rmtree(f"{message.from_user.id}")
      except Exception as e:
        bot.send_message(message.chat.id, f"Error!, errors will send to admins! {e}")
        bot.send_message(5407368270, f"::log:: {e}")
      
        # os.remove(f'yt/{message.from_user.id}.mp4')
        # os.rmdir(f')
        # shutil.rmtree(f'{message.from_user.id}')
        # with open(src, 'wb') as new_file:
        #     new_file.write(video)
        # bot.reply_to(message, "Пожалуй, я сохраню это")



    elif message.text.lower().startswith(".test "):
          bot.send_message(message.chat.id, f"message: {message.text[6:]}")

    # translate 

    elif message.text.lower().startswith('.jt '):
        to_translate = f'{message.text[4:]}'
        translated = GoogleTranslator(source='auto', target='ja').translate(to_translate)
        bot.send_message(message.chat.id, translated)

    elif message.text.lower().startswith('.et '):
        to_translate = f'{message.text[4:]}'
        translated = GoogleTranslator(source='auto', target='en').translate(to_translate)
        bot.send_message(message.chat.id, translated)

    elif message.text.lower().startswith('.ut '):
        to_translate = f'{message.text[4:]}'
        translated = GoogleTranslator(source='auto', target='uz').translate(to_translate)
        bot.send_message(message.chat.id, translated)

    elif message.text.lower().startswith('.rt '):
        to_translate = f'{message.text[4:]}'
        translated = GoogleTranslator(source='auto', target='ru').translate(to_translate)
        bot.send_message(message.chat.id, translated)

    

    # group 

    elif message.text.lower() == "?command :: *gn":
        bot.send_message('@tisyachi_zvyozd', "<b>Good night!</b> 🌙✨",
                         parse_mode = 'HTML')
        
    elif message.text.lower() == "?command :: *gm":
        bot.send_message('@tisyachi_zvyozd', "<b>Good morning!</b> ☕️🍫",
                         parse_mode = 'HTML')

    elif message.text.lower() == "?cheat :: mode :: enable ?st :: a":
        with open(f'{message.chat.id}_ch', 'w') as f:
            f.write('true')        
        bot.send_message(message.chat.id, "02 cheat ::$ mode ?st :: t")

    elif message.text.lower() == "?cheat :: mode :: enable ?st :: f":
        with open(f'{message.chat.id}_ch', 'w') as f:
            f.write('false')        
        bot.send_message(message.chat.id, "02 cheat ::$ mode ?st :: f")

    elif message.text.lower() == "?cheat :: verify":
        with open(f'{message.chat.id}_ch', 'r+') as f:
            list = f.read()

            if list == 'true':        
                bot.send_message(message.chat.id, "02 cheat ::$ :st :: t")

            else:
                bot.send_message(message.chat.id, "02 cheat ::$ :st :: f")


    elif message.text.lower() == "anime list":
        db = sqlite3.connect('base.db')
        sql = db.cursor()

        sql.execute(f"CREATE TABLE IF NOT EXISTS '{message.chat.id}_animes' (id INTEGER PRIMARY KEY AUTOINCREMENT, image TEXT, title TEXT)")

        db.commit()

        for data in sql.execute(f"SELECT * FROM '{message.chat.id}_animes'").fetchall():
            bot.send_message(message.chat.id, f'{data[0]}. {data[1]}')

    elif message.text.lower().startswith("#anime "):
        member = bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status == 'administrator' or 'creator':
            db = sqlite3.connect('base.db')
            sql = db.cursor()
            data = sql.execute(f"SELECT id, title FROM '{message.chat.id}_animes'")

            if sql.fetchone() is None:
                # sql.execute(f"CREATE TABLE IF NOT EXISTS '{message.chat.id}_animes' (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT)")
                sql.execute(f"INSERT INTO '{message.chat.id}_animes' (id, title) VALUES (NULL, '{message.text[6:]}')")
                db.commit()
                bot.send_message(message.chat.id, "Successfully!")

            else:
                bot.send_message(message.chat.id, "Anime already exists!")

    elif message.text.lower().startswith("?update "): #7 
        member = bot.get_chat_member(message.chat.id, message.from_user.id)
        if member.status == 'administrator' or 'creator':
            global update_anime
            update_anime = f'{message.text[8:]}'
            bot.send_message(message.chat.id, f"Update: {message.text[8:]}")
            bot.register_next_step_handler(message, update_to)

    elif message.text.lower() == '.flip':
        rd_1 = 'b2.webp', 'b2.webp', 'b2.webp', 'b1.webp', 'b2.webp', 'b2.webp', 'b1.webp', 'b2.webp'
        res = random.choice(rd_1)
        bot.send_sticker(message.chat.id, sticker = open(res, 'rb'))

    elif message.text.lower() == '.f':
        rd_1 = 'b2.webp', 'b2.webp', 'b2.webp', 'b1.webp', 'b2.webp', 'b2.webp', 'b1.webp', 'b2.webp'
        res = random.choice(rd_1)
        bot.send_sticker(message.chat.id, sticker = open(res, 'rb'))


            



    ### Console 


    if message.chat.type == 'private':
        if message.text.lower() == "..c":
            try:
                db = sqlite3.connect("base.db")
                sql = db.cursor()
                sql.execute(f"CREATE TABLE IF NOT EXISTS console (id INTEGER PRIMARY KEY AUTOINCREMENT, admin TEXT, admin_id TEXT, status TEXT")
                
                db.commit()

                sql.execute(f"INSERT INTO console (id, admin, admin_id, status) VALUES (NULL, '{message.from_user.first_name}', 'moderator')")
                
                db.commit()



                
                bot.send_message(message.chat.id, "Success! you registered as console")
            except Exception as e:
                bot.send_message(message.chat.id, "::log:: error: errors will send to admins!")
                bot.send_message(5407368270, f"::log:: {e}")

        elif message.text.lower() == "consol .. g ":
            bot.send_message(message.chat.id, "group id")
            bot.register_next_step_handler(message, addgroup)

            

    elif message.text.lower() == "console":
        bot.send_message(message.chat.id, "Command console is will enabling with a 02 bot, example, you don't need write commands in the group. You can use commands in here! Console version: 1.0")

    elif message.text.lower().startswith(".. console "):
        pass

    elif message.text.lower().startswith("!! console "):
        pass

    elif message.text.lower().startswith("! console "):
        pass

    elif message.text.lower().startswith("consol ban "):
        pass

    elif message.text.lower().startswith("consol say "):
        pass

    elif message.text.lower().startswith("consol send "):
        pass

    elif message.text == "back":
        bot.send_message(message.chat.id, "Home", reply_markup = button)

def send_id(message):
    msg = message.text
    bot.send_message(id, msg)


def send(message):
    msg = message.text
    bot.send_message(f'{u_name}', msg)


def addgroup(message):
    global group
    group = message.text
    try: 
        db = sqlite3.connect('base.db')
        sql = db.cursor()

        sql.execute(f"CREATE TABLE IF NOT EXISTS ")
        ### sql
    except: pass 


def update_to(message):
    new_title = message.text
    db = sqlite3.connect('base.db')
    sql = db.cursor()

# sql.execute(f"CREATE TABLE IF NOT EXISTS '{message.chat.id}_animes' (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT)")
    sql.execute(f"""UPDATE '{message.chat.id}_animes' SET title = '{new_title}' WHERE id = {update_anime}""")

    print(update_anime)

    db.commit()

    bot.send_message(message.chat.id, "Successfully!")

def qrscan(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = f'qr/{message.from_user.id}.png' # message.photo[1].file_id
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_message(message.chat.id, "Scanning...")

    img = cv2.imread(f'qr/{message.from_user.id}.png')
    barcodes = pyzbar.decode(img)

    os.remove(f'qr/{message.from_user.id}.png')

    for b in barcodes:
        barcodesData = b.data.decode('utf-8')
        bot.send_message(message.chat.id, f'QrCode:\n\n{barcodesData}', disable_web_page_preview = True)


def ranges(message):
    if message.text == "5":
        for data in range(5):
            bot.send_photo(message.chat.id, photo = open(f'res/anime{data}.jpg', 'rb'))
        bot.send_message(message.chat.id, "Successfully!", reply_markup = button)
        

    elif message.text == "10":
        for data in range(10):
            bot.send_photo(message.chat.id, photo = open(f'res/anime{data}.jpg', 'rb'))
        bot.send_message(message.chat.id, "Successfully!", reply_markup = button)
        

    elif message.text == "20":
        for data in range(10):
            bot.send_photo(message.chat.id, photo = open(f'res/anime{data}.jpg', 'rb'))
        bot.send_message(message.chat.id, "Successfully!", reply_markup = button)

    

    elif message.text == "25":
        for data in range(25):
            bot.send_photo(message.chat.id, photo = open(f'res/anime{data}.jpg', 'rb'))
        bot.send_message(message.chat.id, "Successfully!", reply_markup = button)
        

    elif message.text == "30":
        for data in range(30):
            bot.send_photo(message.chat.id, photo = open(f'res/anime{data}.jpg', 'rb'))
        bot.send_message(message.chat.id, "Successfully!", reply_markup = button)


    elif message.text == "40":
        for data in range(40):
            bot.send_photo(message.chat.id, photo = open(f'res/anime{data}.jpg', 'rb'))
        bot.send_message(message.chat.id, "Successfully!", reply_markup = button)


    elif message.text == "45":
        for data in range(45):
            bot.send_photo(message.chat.id, photo = open(f'res/anime{data}.jpg', 'rb'))
        bot.send_message(message.chat.id, "Successfully!", reply_markup = button)
    

    elif message.text == "50":
        for data in range(50):
            bot.send_photo(message.chat.id, photo = open(f'res/anime{data}.jpg', 'rb'))
        bot.send_message(message.chat.id, "Successfully!", reply_markup = button)


    elif message.text == "60":
        for data in range(60):
            bot.send_photo(message.chat.id, photo = open(f'res/anime{data}.jpg', 'rb'))
        bot.send_message(message.chat.id, "Successfully!", reply_markup = button)


    elif message.text == "65":
        for data in range(65):
            bot.send_photo(message.chat.id, photo = open(f'res/anime{data}.jpg', 'rb'))
        bot.send_message(message.chat.id, "Successfully!", reply_markup = button)


    elif message.text == "70":
        for data in range(70):
            bot.send_photo(message.chat.id, photo = open(f'res/anime{data}.jpg', 'rb'))
        bot.send_message(message.chat.id, "Successfully!", reply_markup = button)

    
    elif message.text == "80":
        for data in range(80):
            bot.send_photo(message.chat.id, photo = open(f'res/anime{data}.jpg', 'rb'))
        bot.send_message(message.chat.id, "Successfully!", reply_markup = button)

    elif message.text == "back":
        bot.send_message(message.chat.id, "Home", reply_markup = button)
        
