import os
import telebot
from flask import Flask, request

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")
app = Flask(__name__)

users = [
    {"id": 7502713731, "name": "Baluka Aibyek"},
    {"id": 135182170, "name": "Dana"},
    {"id": 988494617, "name": "alz_sana"},
    {"id": 836832942, "name": "araysn16"},
    {"id": 997621105, "name": "dayanatalgat"},
    {"id": 319296930, "name": "Aia"},
    {"id": 500280475, "name": "Dana2"},
    {"id": 614649210, "name": "eclatant_aa"},
    {"id": 491966138, "name": "nailyamussayeva"},
    {"id": 947989741, "name": "alisher"},
    {"id": 422359565, "name": "Aizhan025"},
    {"id": 328952267, "name": "tomikandre"},
    {"id": 994649505, "name": "TGB4K"},
    {"id": 618710935, "name": "nurtleutheone"},
    {"id": 264019397, "name": "Amirlan_N"},
    {"id": 588439281, "name": "ars_0897"},
    {"id": 1167703998, "name": "Sansy0tom"},
    {"id": 979436015, "name": "aber052"},
    {"id": 1276461016, "name": "aimurellaa"},
    {"id": 491999714, "name": "assel_00"},
    {"id": 387258579, "name": "whataboutdayana"},
    {"id": 607510369, "name": "knb1507"},
    {"id": 1063503364, "name": "solivagant888"},
    {"id": 827348149, "name": "sabinaiskakovva"},
    {"id": 429250518, "name": "destruqt1on"},
    {"id": 291488787, "name": "malika1734"},
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Ваш ID: {message.from_user.id}")

@bot.message_handler(commands=['tagall'])
def tag_all(message):
    mentions = [f"[{u['name']}](tg://user?id={u['id']})" for u in users]
    bot.reply_to(message, " ".join(mentions))

@app.route(f"/{TOKEN}", methods=['POST'])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "ok", 200

@app.route('/')
def index():
    return "Бот работает!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/{TOKEN}")
    app.run(host="0.0.0.0", port=10000)
