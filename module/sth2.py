from aiogram import types
from module.constans import Running
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buy_run_kb = InlineKeyboardMarkup()
buy_run_kb.add(
    InlineKeyboardButton("Приобрести", callback_data="buy_run_kb")
)


async def weapon_command(message: types.Message):

    await message.answer(text="книга от Халеда Хоссейни")
    await message.answer_photo(open('C:\Users\User\PycharmProjects\HW1\media\Running.jpg','rb'),
                               caption=Running, reply_markup=buy_run_kb)