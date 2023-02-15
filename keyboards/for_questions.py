# coding: utf8
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup


def start_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        types.ReplyKeyboardMarkup(
            text="/services"
        ),
        types.ReplyKeyboardMarkup(
            text="/thebook"
        ),
        types.ReplyKeyboardMarkup(
            text="/contacts"
        ),
        types.ReplyKeyboardMarkup(
            text="/FAQ"
        ),
        types.ReplyKeyboardMarkup(
            text="/documents"
        ),
        types.ReplyKeyboardMarkup(
            text="/start"
        ),
    ]
    kb = types.ReplyKeyboardMarkup(reply_keyboard=buttons, resize_keyboard=True)
    return kb
