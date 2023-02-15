# coding: utf8
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup


def get_yes_no_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        types.InlineKeyboardButton(text="Да", callback_data="yes"),
        types.InlineKeyboardButton(text="Нет", callback_data="no")
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
