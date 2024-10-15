import test_bd
import test_bd as fun
from datetime import datetime

import asyncio
import logging
import sys

import config as cfg
import inline_menu as imenu
import menu

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram import F


dp = Dispatcher()
bot = Bot(token=cfg.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, *{message.from_user.full_name}*!", reply_markup=menu.hello(), parse_mode="MARKDOWN",
                         protect_content=True)
    test_bd.insert_registration(message.chat.id, datetime.now())
    print(test_bd.select_all_registration())



@dp.message()
async def messages(message: Message) -> None:
    if message.text =="Password":
        await message.answer(text=f"Ваш пароль: *{test_bd.select_registration(message.chat.id)[0][1]}*",
                             parse_mode="MARKDOWN", protect_content=True)
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
    if message.text == "Info":
        await message.answer(text=f"Ваши данные: *{test_bd.select_registration(message.chat.id)[0][0]}, {test_bd.select_registration(message.chat.id)[0][1]}, {str(test_bd.select_registration(message.chat.id)[0][2].strftime("%d/%m/%Y"))}*",
                             parse_mode="MARKDOWN", protect_content=True)
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)

@dp.callback_query(F.data == "next")
async def next_button(callback: CallbackQuery) -> None:
    await callback.answer(text="Вы _нажали_ *кнопку* 1.", parse_mode="MARKDOWN", protect_content=True)
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id - 1)

async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
