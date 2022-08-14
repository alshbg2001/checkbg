import json
import requests
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

bot = Client(
    "bot",
    api_id=2033318,
    api_hash='223cde1537f217dda4e16183f47af958',
    bot_token='5067621147:AAEeKEBjWuNMl82UJYOd_LgQE2WIcwTdttg'
)


@bot.on_message(filters.command('start'))
def start(bot, msg):
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton('start check users 3', callback_data=f"check#3"),
        ],
        [
            InlineKeyboardButton('start chech users 4', callback_data=f"check#4"),
        ],
    ])
    bot.send_message(
        msg.chat.id, f"welcom to bot\n check users telegram", reply_markup=reply_markup)


@bot.on_callback_query()
def check_start(bot, CallbackQuery):
    global running
    if CallbackQuery.data.split("#")[0] == "check":
        running = True
        reply_markup = InlineKeyboardMarkup([
            [
                InlineKeyboardButton('stop', callback_data=f"stop"),
            ],
            [
                InlineKeyboardButton('start', callback_data=f"check#"+str(CallbackQuery.data.split("#")[1]))
            ],
        ])
        chat_id = CallbackQuery.message.chat.id
        us = "qwertyuiopasdfghjklzxcvbnm"
        ii = 0
        yes = 0
        no = 0
        while running:
            ii += 1
            user = str(''.join(random.choice(us) for i in range(int(CallbackQuery.data.split("#")[1]))))
            r = requests.get(
                f"https://alsh-ax.ml/api/TelegramCheck.php?user={user}bot").json()
            if r['info']['status'] == "Available":
                yes += 1
                bot.send_message(chat_id, f"welcom.\n - is user Available : @{user}bot \n Dev @alsh_3k")
                ok = "done"
            elif r['info']['status'] == "UnAvailable":
                no += 1
                ok = "field"
            bot.edit_message_text(chat_id, CallbackQuery.message.id, f"Done Start. \n user : @{user}bot \n - checking : {ii} \n - done : {yes} \n - failed : {no}", reply_markup=reply_markup)
    elif CallbackQuery.data == "stop":
        running = False
        return running


bot.run()
