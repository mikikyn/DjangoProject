from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
from db import db_main
from aiogram.types import ReplyKeyboardRemove
from config import staff



class fsm_store(StatesGroup):
    name_products = State()
    category = State()
    size = State()
    price = State()
    product_id = State()
    photo_products = State()
    submit_button = State()


async def start_fsm(message: types.Message):
    if message.from_user.id not in staff:
        await message.answer('Команда только для сотрудников!')
        return
    await fsm_store.name_products.set()
    await message.answer('Введите название продукта: ')

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_products'] = message.text

    await message.answer('Введите категорию продукта: ')
    await fsm_store.next()


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await message.answer('Введите размер продукта: ')
    await fsm_store.next()


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await message.answer('Введите цену продукта: ')
    await fsm_store.next()


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await message.answer('Введите артикул(он должен быть уникальным): ')
    await fsm_store.next()


async def load_product_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text

    await message.answer('Отправьте фото: ')
    await fsm_store.next()


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

    await message.answer('Посмотрите, верные ли данные?')
    await message.answer_photo(
        photo=data['photo'],
        caption=f'Название продукта: {data["name_products"]}\n'
                f'Категория продукта: {data["category"]}\n'
                f'Размер продукта: {data["size"]}\n'
                f'Стоимость: {data["price"]}\n'
                f'Артикул: {data["product_id"]}\n',
        reply_markup=buttons.submit_button)

    await fsm_store.next()


async def submit_button(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardRemove()

    if message.text == 'Да':
        async with state.proxy() as data:
            await message.answer('Отлично, ваши данные в базе!', reply_markup=kb)
            await db_main.sql_insert_products(
            name_product=data['name_products'],
            category=data['category'],
            size=data['size'],
            price=data['price'],
            product_id=data['product_id'],
            photo=data['photo']
        )
            await state.finish()

    elif message.text == 'Нет':
        await message.answer('Хорошо, заполнение анкеты завершено!', reply_markup=kb)
        await state.finish()

    else:
        await message.answer('Выберите "Да" или "Нет" ')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    kb =ReplyKeyboardRemove()

    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=kb)

        await state.finish()


async def show_products(message: types.Message):
    products = await db_main.sql_insert_products()

    if not products:
        await message.answer('Нету товаров!')
        return


def register_store(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена', ignore_case=True), state='*')

    dp.register_message_handler(start_fsm, commands=['product_add'])
    dp.register_message_handler(load_name, state=fsm_store.name_products)
    dp.register_message_handler(load_category, state=fsm_store.category)
    dp.register_message_handler(load_size, state=fsm_store.size)
    dp.register_message_handler(load_price, state=fsm_store.price)
    dp.register_message_handler(load_product_id, state=fsm_store.product_id)
    dp.register_message_handler(load_photo, state=fsm_store.photo_products, content_types=['photo'])
    dp.register_message_handler(submit_button, state=fsm_store.submit_button)






