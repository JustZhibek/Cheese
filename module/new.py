from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db.base import get_products


def buy_books_kb(product_id):
    book1_kb = InlineKeyboardMarkup()
    book1_kb.add(InlineKeyboardButton("получить", callback_data=f"book1 {product_id}"))
    return book1_kb


async def show_books(message: types.Message):
    """
        Функция показывает книги
    """
    await message.answer(text="все книги:")
    ohota_book = get_products()[1]
    book5_book = get_products()[0]
    marvel_book = get_products()[3]

    await message.answer_photo(
        open(ohota_book[5], 'rb'),
        caption=f'{ohota_book[1]}, цена - {ohota_book[3]}',
        reply_markup=book1_kb(ohota_book)
    )

    await message.answer_photo(
        open(book5_book[4], 'rb'),
        caption=f'{book5_book[0]}, цена - {book5_book[1]}',
        reply_markup=book1_kb(book5_book)
    )

    await message.answer_photo(
        open(marvel_book[5], 'rb'),
        caption=f'{marvel_book[2]}, цена - {marvel_book[3]}',
        reply_markup=book1_kb(marvel_book)
    )
