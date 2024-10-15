from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


def hello():
    btnFirst=KeyboardButton(text="Password")
    btnSecond=KeyboardButton(text="Info")
    keyboard= ReplyKeyboardMarkup(keyboard=[[btnFirst],[btnSecond]], resize_keyboard=True)
    return keyboard