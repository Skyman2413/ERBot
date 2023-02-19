# coding: utf8
from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_yes_no_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Да", callback_data="yes"))
    builder.add(types.InlineKeyboardButton(text="Нет", callback_data="no"))

    return builder.as_markup()
