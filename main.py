from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from os import getenv
import logging
from module.start import start_command
from module.help import help_command
from module.Running_info import Running_command
from module.Ohota_info import Ohota_command
from module.marvel import Marvel_command
from module.admin import message_log, proverka_admin, bad_words, ban_user, da_net
from module.fms_info import (
	Form,
	cancel_handler,
	form_start,
	process_name,
	process_age,
	process_day,
	process_done
)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    bot = Bot(getenv("BOT_TOKEN"))
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    dp.register_message_handler(form_start, commands=['form'])
    dp.register_message_handler(form_start, Text(equals='Нет'), state=Form.done)
    dp.register_message_handler(cancel_handler, state='*', commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(process_name, state=Form.name)
    dp.register_message_handler(process_age, state=Form.age)
    dp.register_message_handler(process_day, state=Form.day)
    dp.register_message_handler(process_done, Text(equals='Да'), state=Form.done)
    dp.register_message_handler(start_command, commands=["start"])
    dp.register_message_handler(help_command, commands=["help"])
    dp.register_message_handler(Running_command, commands=['книга'])
    dp.register_message_handler(Marvel_command, Text(equals="книга 2"))
    dp.register_message_handler(Ohota_command, Text(equals="книга 3"))
    dp.register_message_handler(ban_user, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(da_net, commands=['да'], commands_prefix=['!'])
    dp.register_message_handler(bad_words)

    executor.start_polling(dp, skip_updates=True)