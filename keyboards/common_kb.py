from aiogram import types
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def get_yes_no_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Да", callback_data="yes"))
    builder.add(types.InlineKeyboardButton(text="Нет", callback_data="no"))
    return builder.as_markup()


def default_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Услуги"))
    builder.add(types.KeyboardButton(text="Купить книгу"))
    builder.add(types.KeyboardButton(text="Контакты"))
    builder.add(types.KeyboardButton(text="Помощь"))
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=False)

