# coding: utf8
from pathlib import Path

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, InputMediaDocument
import os
import standartMessages

router = Router()


@router.message(Command(commands=["start"]))
async def cmd_start(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(standartMessages.start, parse_mode="HTML")


@router.message(Command(commands=["contacts"]))
async def cmd_start(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(standartMessages.contacts, parse_mode="HTML")


@router.message(Command(commands=["documents"]))
async def cmd_documents(msg: Message, state: FSMContext):
    '''TODO: send documents'''
    media = []
    root_path = os.getcwd()
    file1 = FSInputFile(root_path + r"\documents\Rodoslovnaya kniga.pdf", filename="Родословная книга.pdf")
    file2 = FSInputFile(root_path + r"\documents\Rodoslovnaya kniga.pdf", filename="Историческая родословная касимовских татар.pdf")
    file3 = FSInputFile(root_path + r"\documents\Chetyre veka istorii odnoy semyi.pdf", filename="Четыре века истории одной семьи.pdf")
    await msg.answer_media_group([InputMediaDocument(media=file1),
                                  InputMediaDocument(media=file2),
                                  InputMediaDocument(media=file3, caption=standartMessages.advert)])
    await state.clear()
