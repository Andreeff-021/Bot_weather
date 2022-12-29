from aiogram import Bot, types, Dispatcher, executor
from config import TOKEN
from weather import weather_city
from keyboard import greet_kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer(text='Чтобы посмотреть погоду, введите город')


@dp.message_handler()
async def weather(message: types.Message):
    await bot.send_message(message.from_user.id, weather_city(message.text))
    await message.answer(text='Для получения новых данных, нажмите "start"', reply_markup=greet_kb)


if __name__ == '__main__':
    executor.start_polling(dp)