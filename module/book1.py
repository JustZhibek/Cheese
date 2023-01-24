from aiogram import types
from module.constans import book1,sth
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

book1_kb = InlineKeyboardMarkup()
book1_kb.add(
    InlineKeyboardButton("Приобрести", callback_data="book1")
)

async def book_command(message: types.Message):
    await message.answer(text="интересная книга для любителей фантастики:")
    await message.answer_photo(open(
        'C:\Users\User\PycharmProjects\HW1\media\batman.jpeg', 'rb'),
        caption=book1, reply_markup=book1_kb)
    await message.answer_photo(open('C:\Users\User\PycharmProjects\HW1\media\marvel.jpg', 'rb'),
                               caption=sth, reply_markup=book1_kb)