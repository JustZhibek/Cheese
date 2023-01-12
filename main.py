from aiogram import Bot,Dispatcher,executor,types
from dotenv import load_dotenv
from random import choice
import os


load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message:types.Message):
    await message.answer(f"Hello,welcome {message.from_user.first_name}")
    await message.delete()

@dp.message_handler(commands=['help'])
async def start_command(message:types.Message):
    await message.answer(f'''Команды:
     start - начало
     help - список команд,помощь
     myinfo - получить информацию о себе
     picture - показать рандомную картинку''')
    await message.delete()


@dp.message_handler(commands=['myinfo'])
async def start_command(message:types.Message):
        await message.answer(text = f'Your ID: {message.from_user.id} \n'
                                    f'your name: {message.from_user.first_name} \n'
                                    f'your nickname: {message.from_user.username}')


@dp.message_handler(commands=['picture'])
async def friend_picture(message: types.Message):
        photo = open('media/'+ choice(os.listdir('media')), 'rb')
        await bot.send_photo(message.chat.id, photo)
        await message.delete()


@dp.message_handler()
async def echo(message: types.Message):
    letters = message.text.split(' ')
    if len(letters) >= 3:
        await message.answer(message.text.upper())
    else:
        await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)