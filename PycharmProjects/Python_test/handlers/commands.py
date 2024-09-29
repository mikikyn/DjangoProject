from aiogram import types, Dispatcher
import os
from buttons import start
from config import bot




async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Здравствуйте!',
                           reply_markup=start)



async def send_info(message: types.Message):
    info = ('Здравствуйте, этот бот для онлайн-магазина')
    await bot.send_message(chat_id=message.from_user.id, text=info)



def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(send_info, commands=['info'])