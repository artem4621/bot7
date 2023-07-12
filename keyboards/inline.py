
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from callback.animals import AnimalsCallback

phone = InlineKeyboardButton(text='Телефонов', callback_data=AnimalsCallback(animal='Телефон', count=4).pack())
laptop = InlineKeyboardButton(text='Ноутбуков', callback_data=AnimalsCallback(animal='Ноутбук', count=5).pack())

phone_laptop_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [phone, laptop],
])