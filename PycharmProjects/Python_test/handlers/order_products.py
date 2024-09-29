from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, staff


class FSM_order(StatesGroup):
    product_id = State()
    size = State()
    quantity = State()
    contact = State()

async def start_order(message: types.Message):
    await FSM_order.product_id.set()
    await message.answer("Введите артикул товара, который хотите сделать заказ: ")

async def load_product_id_order(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await FSM_order.next()
    await message.answer("Введите размер: ")

async def load_size_order(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await FSM_order.next()
    await message.answer("Введите количество: ")

async def load_quantity_order(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text

    await FSM_order.next()
    await message.answer("Введите ваши контактные данные: ")

async def load_contact_order(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact'] = message.text

        await send_order_to_staff(data)
        await message.answer("Ваш заказ отправлен!")
    await state.finish()


async def send_order_to_staff(order_data):
    for staff_id in staff:
        await bot.send_message(staff_id,
            f"Новый заказ:\n"
            f"Артикул: {order_data['product_id']}\n"
            f"Размер: {order_data['size']}\n"
            f"Количество: {order_data['quantity']}\n"
            f"Контакт: {order_data['contact']}"
        )

def register_handlers_order(dp: Dispatcher):

    dp.register_message_handler(start_order, commands=['order'])
    dp.register_message_handler(load_product_id_order, state=FSM_order.product_id)
    dp.register_message_handler(load_size_order, state=FSM_order.size)
    dp.register_message_handler(load_quantity_order, state=FSM_order.quantity)
    dp.register_message_handler(load_contact_order, state=FSM_order.contact)
