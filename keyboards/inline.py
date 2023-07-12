
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from callback.animals import AnimalsCallback

phone = InlineKeyboardButton(text='Телефоны', callback_data=AnimalsCallback(animal='Телефон', count=4).pack())
laptop = InlineKeyboardButton(text='Ноутбуки', callback_data=AnimalsCallback(animal='Ноутбук', count=5).pack())
mouse = InlineKeyboardButton(text='Мышки', callback_data=AnimalsCallback(animal='Мышка', count=12).pack())
headphones = InlineKeyboardButton(text='Наушники', callback_data=AnimalsCallback(animal='Наушники', count=44).pack())

phone_laptop_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [phone, laptop],
    [mouse, headphones]
])