import json, requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from requests import post,get

bot = Client(
    "Echo_bot",
    api_id=2033318,
    api_hash='223cde1537f217dda4e16183f47af958',
    bot_token='1128799285:AAH634XjJOUgU1CfeMYK35uU0GJOkAypiL4'
)

@bot.on_message(filters.command('start'))
def trply_to_hi(bot, msg):
    bot.send_message(msg.chat.id, f"مرحبا بك في بوت تحميل")

@bot.on_message(filters.text)
def trply_to_hi(bot, msg):
    if "tiktok" in msg.text:
        BOTTOM = [
            [
                InlineKeyboardButton('mp3', callback_data=f"mp3#{msg.text}")
            ],
        ]
        reply_markup = InlineKeyboardMarkup(BOTTOM)
        chat_id = msg.chat.id
        msgid = bot.send_message(chat_id, f"جاري التحميل...")
        api = requests.get(f"https://lovetik.com/api/ajax/search?k={msg.text}").json()
        bot.send_video(chat_id, api['links'][0]['a'], f"@alsh_3k - size {api['links'][0]['s']}", reply_markup=reply_markup)
        bot.delete_messages(chat_id, msgid.id)

@bot.on_callback_query()
def trply_to_mp3(bot, CallbackQuery):
    if CallbackQuery.data.split('#')[0] == "mp3":
        chat_id = CallbackQuery.message.chat.id
        bot.delete_messages(chat_id, CallbackQuery.message.id)
        msgid = bot.send_message(chat_id, f"جاري التحميل...")
        api = requests.get(f"https://lovetik.com/api/ajax/search?k={CallbackQuery.data.split('#')[1]}").json()
        for i in api['links']:
           # print(i['t'])
            if "MP3" in i['t']:
                bot.send_audio(chat_id, i['a'], f"@alsh_3k - {i['t']}", )
                bot.delete_messages(chat_id, msgid.id)

bot.run()
