import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher
from aiogram.filters import Command  # Фильтр для /start, /...
from aiogram.types import Message, CallbackQuery  # Тип сообщения

from callback.animals import AnimalsCallback
from config import config  # Config
from keyboards.inline import phone_laptop_keyboard

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Менеджер бота


# dp.message - обработка сообщений
# Command(commands=['start'] Фильтр для сообщений, берём только /start
@dp.message(Command(commands=['start']))  # Берём только сообщения, являющиеся командой /start
async def start_command(message: Message):  # message - сообщение, которое прошло через фильтр
    await message.answer("Привет,напиши /shop чтобы посмотреть товары")  # Отвечаем на полученное сообщение


@dp.message(Command(commands=['shop']))  # Берём только сообщения, являющиеся командой /start
async def start_command(message: Message):  # message - сообщение, которое прошло через фильтр
    await message.answer("Вот что у нас есть:",
                         reply_markup=phone_laptop_keyboard)
@dp.callback_query(AnimalsCallback.filter())
async def handle_cats(query: CallbackQuery, callback_data: AnimalsCallback):
    await query.answer(f'Вы купили товар')
    await query.message.answer(f'Товар: {callback_data.animal}. Количество: {callback_data.count}')

# dp.callback_query - обработка нажатия inline кнопок



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