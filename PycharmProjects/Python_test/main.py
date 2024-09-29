import logging
from aiogram.utils import executor
from config import bot, dp, admin
from buttons import start_test
from handlers import commands, echo, fsm_store, send_products, order_products
from db import db_main


async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text='Бот работает!',
                               reply_markup=start_test)
        await db_main.sql_create()



commands.register_commands(dp)
fsm_store.register_store(dp)
send_products.register_send_products_handler(dp)
order_products.register_handlers_order(dp)

echo.register_echo(dp)




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)