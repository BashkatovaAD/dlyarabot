# -*- coding: utf-8 -*- 

import platform
import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

bot_token = '6547665217:AAEs6odbtzDUkEP57l9LZKiFWLTWWx7Tn9w'
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Информация о машине", callback_data='info')],
        [InlineKeyboardButton("Перейти в GitHub создателя бота", url="https://github.com/BashkatovaAD")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, я бот-помощник!", reply_markup=reply_markup)

def info(update, context):
    info_text = f"Информация о машине, на которой запущен бот-помощник:\n\n" \
                f"machine: {platform.machine()}\n" \
                f"version: {platform.version()}\n" \
                f"platform: {platform.platform()}\n" \
                f"uname: {platform.uname()}\n" \
                f"system: {platform.system()}\n" \
                f"processor: {platform.processor()}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=info_text)

def button_callback(update, context):
    query = update.callback_query
    if query.data == 'info':
        info(update, context)

def text_command(update, context):
    if update.message.text.lower() == '/info':
        info(update, context)

start_handler = CommandHandler('start', start)
info_button_handler = CallbackQueryHandler(button_callback)
text_command_handler = MessageHandler(Filters.text & ~Filters.command, text_command)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_button_handler)
dispatcher.add_handler(text_command_handler)

updater.start_polling()

