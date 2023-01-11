from aiogram import Bot,Dispatcher,executor,types
from dotenv import load_dotenv
from os import getenv

TOKEN ='TOKEN'
load_dotenv()
bot = Bot(getenv(TOKEN))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message:types.Message):
    await message.answer(f"Hello,welcome {message.from_user.first_name}")

    await message.answer('this is answer')
    await message.reply('reply method')


@dp.message_handler(commands=['picture'])
async def start_command(message:types.Message):
    await message.answer_photo(open('media/mem.jpg','rb'),
    caption = 'dog')

@dp.message_handler()
async def echo(message:types.Message):
    await bot.send_message(message.from_user.id,message.text)
    await message.reply(text=message.text.upper())


if __name__ == '__main__':
    executor.start_polling(dp)