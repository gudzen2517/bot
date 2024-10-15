from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def hello():
    FirstButton = InlineKeyboardButton(text="Кнопка1", callback_data="next")
    SecondButton = InlineKeyboardButton(text="Кнопка2", callback_data="prev")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[FirstButton], [SecondButton]])
    return keyboard
