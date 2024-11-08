import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests, random
from user_agent import generate_user_agent

token = "𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐓𝐨𝐤𝐞𝐧"
bot = telebot.TeleBot(token)

def is_valid_link(link):
    return link.startswith("https://")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Throw 50 likes", callback_data="request_likes")
    markup.add(button)
    bot.send_message(message.chat.id, "To request a like, click on the like button 50 times.", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "request_likes")
def ask_for_username(call):
    bot.send_message(call.message.chat.id, "Send your Instagram username")
    bot.register_next_step_handler(call.message, process_username)

def process_username(message):
    user = message.text
    bot.send_message(message.chat.id, "Send the link of the post you want to share.")
    bot.register_next_step_handler(message, lambda msg: process_link(msg, user))

def process_link(message, user):
    link = message.text
    if not is_valid_link(link):
        bot.send_message(message.chat.id, "The link is invalid. Make sure it starts withـ https://")
        return

    email = random.randint(100000, 999999)
    res = requests.post('https://api.likesjet.com/freeboost/7', json={
        'instagram_username': user, 
        'link': link, 
        'email': f'{email}@gmail.com'}, 
        headers={
            'Host': 'api.likesjet.com', 
            'content-length': '137', 
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"', 
            'accept': 'application/json, text/plain, */*', 
            'content-type': 'application/json', 
            'sec-ch-ua-mobile': '?1', 
            'user-agent': generate_user_agent(), 
            'sec-ch-ua-platform': '"Android"', 
            'origin': 'https://likesjet.com', 
            'sec-fetch-site': 'same-site', 
            'sec-fetch-mode': 'cors', 
            'sec-fetch-dest': 'empty', 
            'referer': 'https://likesjet.com/', 
            'accept-language': 'en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5'
        }
    )

    if 'You can only receive likes once per day.' in res.text:
        bot.send_message(message.chat.id,'Please try again after 24 hours before requesting a refill. ')
    elif 'Success! You will receive likes within next few minutes.' in res.text:
        uu = f'''
Requested for throwing
Username  : {user}
Post link {link}
Quantity 50 likes

by @dXlaw

'''
        bot.send_message(message.chat.id, uu)
    else:
        bot.send_message(message.chat.id, res.json().get('message', 'An unexpected error occurred..'))

#تمت بواسطه @PY_50   
bot.polling()