from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from callback.animals import AnimalsCallback
cats = InlineKeyboardButton(text='Котов', callback_data=AnimalsCallback(
    animal='cat',
    count=4
).pack())
dogs = InlineKeyboardButton(text='Собак', callback_data=AnimalsCallback(
    animal='dog',
    count=5
).pack())

cats_dogs_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [cats, dogs],
])
