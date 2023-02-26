from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def services_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Архивный поиск", callback_data="1"))
    builder.add(types.InlineKeyboardButton(text="Семейная история", callback_data="2"))
    builder.add(types.InlineKeyboardButton(text="Писательские услуги", callback_data="3"))
    builder.add(types.InlineKeyboardButton(text="Издательские услуги", callback_data="4"))
    builder.add(types.InlineKeyboardButton(text="Графика", callback_data="5"))
    builder.add(types.InlineKeyboardButton(text="Фильмы о семейной истории" , callback_data="6"))
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)
