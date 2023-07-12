import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text  # Фильтр для /start, /...
from aiogram.types import Message, CallbackQuery  # Тип сообщения

from callback.animals import AnimalsCallback
from config import config  # Config
from keyboards.inline import cats_dogs_keyboard

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Менеджер бота


# dp.message - обработка сообщений
# Command(commands=['start'] Фильтр для сообщений, берём только /start
@dp.message(Command(commands=['start']))  # Берём только сообщения, являющиеся командой /start
async def start_command(message: Message):  # message - сообщение, которое прошло через фильтр
    await message.answer("Привет, что ты любишь больше, собак или котов?",
                         reply_markup=cats_dogs_keyboard)  # Отвечаем на полученное сообщение


@dp.callback_query(AnimalsCallback.filter())
async def handle_cats(query: CallbackQuery, callback_data: AnimalsCallback):
    await query.answer(f'Вы нажали кнопку')
    await query.message.answer(f'Животное: {callback_data.animal}. Количество: {callback_data.count}')


async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')