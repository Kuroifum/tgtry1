from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.web_app_info import WebAppInfo
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token='7070211781:AAHo-PZ49l7Y8SZGJDjJBkoV1PSEqaV-Az8')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Press the button', web_app=WebAppInfo(url='https://www.google.ru/')))
    await message.answer('Bot is ready', reply_markup=markup)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)