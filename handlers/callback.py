from config import bot, Dispatcher
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def menu_sender(call: types.CallbackQuery):

    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("книги", callback_data="button_call_3")
    button_call_4 = InlineKeyboardButton("комиксы", callback_data="button_call_4")
    markup.add(button_call_3, button_call_4)

    photo = open("media/photo.png", "rb")
    await bot.send_photo(call.from_user.id, photo, reply_markup=markup)
    photo.close()

async def books_sender(call: types.CallbackQuery):
    photo1 = open("media/Running.jpg", "rb")
    photo2 = open("media/ohota-na-ovec.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo1)
    photo1.close()
    await bot.send_message(call.from_user.id, "Бегущий за ветром 500с")
    await bot.send_photo(call.from_user.id, photo2)
    photo2.close()
    await bot.send_message(call.from_user.id, 'Охота на овец 640с')

async def comics_sender(call: types.CallbackQuery):
    photo3 = open("media/marvel.jpg", "rb")
    photo4 = open("media/batman.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo3)
    photo3.close()
    await bot.send_message(call.from_user.id, "Комиксы Marvel - 400сом")
    await bot.send_photo(call.from_user.id, photo4)
    photo4.close()
    await bot.send_message(call.from_user.id, "Комиксы DC - 350 сом")

async def address_sender(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, "Наш адрес Ахунбаева, 78")

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(menu_sender, text="button_call_1")
    dp.register_callback_query_handler(address_sender, text="button_call_2")
    dp.register_callback_query_handler(books_sender, text="button_call_3")
    dp.register_callback_query_handler(comics_sender, text="button_call_4")