# coding: utf8
from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(commands=["start"])
async def cmd_start(msg: Message):
    await msg.answer('<br>Выберите категорию: Выберите категорию</br> <br>/services - Услуги</br> <br>/thebook - '
                     'Купить книгу</br><br>/contacts - Контакты</br><br>/FAQ – Частые вопросы</br><br>/documents – '
                     'Документы об образовании</br><br>/start – Помощь</br>', parse_mode="HTML")


