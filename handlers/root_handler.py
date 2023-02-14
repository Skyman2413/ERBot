
from aiogram import Router
from aiogram.types import Message

from keyboards.for_questions import start_keyboard

router = Router()


@router.message(commands=["start"])
async def cmd_start(msg: Message):
    await msg.answer("Выберите категорию: ", reply_markup=start_keyboard())


