from pathlib import Path

from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, InputMediaDocument
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
    await msg.answer(standartMessages.contacts, parse_mode="HTML", disable_web_page_preview=True)


@router.message(Command(commands=["documents"]))
async def cmd_documents(msg: Message, state: FSMContext):
    root_path = Path.cwd()
    file1 = FSInputFile(Path(root_path, "documents", "Диплом кандидата.jpg"), filename="Диплом кандидата.jpg")
    file2 = FSInputFile(Path(root_path, "documents", "Диплом магистра.jpg"), filename="Диплом магистра.jpg")
    await msg.answer(standartMessages.documents, parse_mode="HTML")
    await msg.answer_media_group([InputMediaDocument(media=file1),
                                  InputMediaDocument(media=file2)])
    await state.clear()
