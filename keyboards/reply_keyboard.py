from aiogram.types import KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder


kb = ReplyKeyboardBuilder()

btn = KeyboardButton(text="Back")
kb.add(btn)

kb = kb.as_markup(resize_keyboard=True)







