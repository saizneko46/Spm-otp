
# Instagram Booster class for boosting posts
class InstagramBooster:
    def __init__(self):
        self.ua = UserAgent("ios").Random()

    def boost_post(self, user: str, link: str) -> dict:
        email = f"x_spoilt{random.randint(100000, 999999)}@gmail.com"
        headers = {
            "Host": "api.likesjet.com",
            "content-length": "137",
            "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "sec-ch-ua-mobile": "?1",
            "user-agent": self.ua,
            "sec-ch-ua-platform": "\"Android\"",
            "origin": "https://likesjet.com",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://likesjet.com/",
            "accept-language": "en-XA,en;q=0.9,ar-XB;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5"
        }
        data = {"instagram_username": user, "link": link, "email": email}
        response = requests.post('https://api.likesjet.com/freeboost/7', json=data, headers=headers).json()
        return response

# Function to display text with a delay
def slow_type(text):
    for char in text + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(30 / 2000)

# Handler for /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    if user_id == USER_ID:
        bot.send_message(message.chat.id, "Bot by AW-TEAM Modified by KiNGEX, Nork || JOIN FOR MORE: https://t.me/join_another_world || (If you purchased this script then you are scammed because its free on our channel)")
        
        ab = pyfiglet.figlet_format("AW")
        bot.send_message(message.chat.id, ab)  # Sending plain text without Markdown
        slow_type("Bot By Nork (AnotherWorld)")

        # Create inline keyboard with two buttons
        markup = types.InlineKeyboardMarkup()
        button_report = types.InlineKeyboardButton('Report', callback_data='report')
        button_boost = types.InlineKeyboardButton('Like Sender', callback_data='like_sender')
        markup.row(button_report, button_boost)

        # Send message with inline keyboard
        bot.send_message(message.chat.id, "Choose an action:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Unauthorized user")

# Handler for inline keyboard button callback
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == 'report':
        # Ask for target username
        msg = bot.send_message(call.message.chat.id, "Enter the target username:")
        bot.register_next_step_handler(msg, process_target_username)
    elif call.data == 'like_sender':
        # Ask for Instagram username and post link
        msg = bot.send_message(call.message.chat.id, "Enter Instagram username:")
        bot.register_next_step_handler(msg, process_instagram_username)

def process_target_username(message):
    user_id = message.from_user.id
    target_username = message.text.strip()

    # Logic for reporting goes here
    head = {
        "Host": "help.instagram.com",
        "content-length": "715",
        "x-fb-lsd": "AVq5uabXj48",
        "x-asbd-id": "129477",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
        "sec-ch-ua-platform": "\"Android\"",
        "content-type": "application/x-www-form-urlencoded",
        "accept": "*/*",
        "origin": "https://help.instagram.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://help.instagram.com/contact/723586364339719",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,ar-DZ;q=0.8,ar;q=0.7,fr;q=0.6,hu;q=0.5",
        "cookie": "ig_nrcb=1"
    }

    while True:
        dt1 = datetime.now()
        ts1 = str(datetime.timestamp(dt1)).split('.')[0]
        us = 'qwertyuiopasdfghjklzxcvbnm._1234567890'
        boy = str("".join(random.choice(us) for i in range(10)))
        email = boy + '@gmail.com'
        data = f'jazoest=2931&lsd=AVq5uabXj48&Field258021274378282={target_username}&Field735407019826414=&Field506888789421014[year]=2014&Field506888789421014[month]=11&Field506888789421014[day]=11&Field294540267362199=Parent&inputEmail={email}&support_form_id=723586364339719&support_form_locale_id=en_US&support_form_hidden_fields=%7B%7D&support_form_fact_false_fields=[]&__user=0&__a=1&__req=6&__hs=19552.BP%3ADEFAULT.2.0..0.0&dpr=1&__ccg=GOOD&__rev=1007841948&__s=s4c6vz%3Anapxo9%3An9ncx2&__hsi=7255652935514227640&__dyn=7xe6E5aQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXw5ux60Vo1upE4W0OE2WxO2O1Vwooa81VohwnU1e42C220qu1Tw40wdq0Ho2ewnE3fw6iw4vwbS1Lw4Cwcq&__csr=&__spin_r=1007841948&__spin_b=trunk&__spin_t={ts1}'
        res = requests.post('https://help.instagram.com/ajax/help/contact/submit/page', data=data, headers=head).status_code
        bot.send_message(message.chat.id, f'[+] Report Sent ✅ | SC : {res}')

def process_instagram_username(message):
    user_id = message.from_user.id
    instagram_username = message.text.strip()

    # Ask for post link
    msg = bot.send_message(message.chat.id, "Enter post link:")
    bot.register_next_step_handler(msg, lambda msg: process_post_link(msg, instagram_username))

def process_post_link(message, instagram_username):
    post_link = message.text.strip()

    # Boost post using InstagramBooster
    booster = InstagramBooster()
    response = booster.boost_post(instagram_username, post_link)
    result_message = f"Status: {'[bold green]Success[/]' if response.get('status') else '[bold red]Failed[/]'}\nMessage: {response.get('message')}"
    bot.send_message(message.chat.id, Panel(result_message, title="[bold blue]Boost Result[/]"))

# Start polling
bot.polling()
