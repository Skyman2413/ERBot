# coding: utf8
from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, InputMediaDocument
import os

import keyboards.common_kb
import standartMessages

router = Router()


@router.message(Command(commands=["start"]))
@router.message(Text(text="Помощь"))
async def cmd_start(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(standartMessages.start, parse_mode="HTML", reply_markup=keyboards.common_kb.default_keyboard())


@router.message(Command(commands=["contacts"]))
@router.message(Text(text="Контакты"))
async def cmd_contacts(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(standartMessages.contacts, parse_mode="HTML")


@router.message(Command(commands=["documents"]))
async def cmd_documents(msg: Message, state: FSMContext):
    root_path = os.getcwd()
    file1 = FSInputFile(root_path + r"\documents\Диплом кандидата.jpg", filename="Диплом кандидата.jpg")
    file2 = FSInputFile(root_path + r"\documents\Диплом магистра.jpg", filename="Диплом магистра.jpg")
    await msg.answer_media_group([InputMediaDocument(media=file1),
                                  InputMediaDocument(media=file2, caption=standartMessages.documents)])
    await state.clear()
