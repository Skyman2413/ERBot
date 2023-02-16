from aiogram import Router
from aiogram.types import Message
import standartMessages

router = Router()


@router.message()
async def unhandled_message(msg: Message):
    await msg.answer(standartMessages.unhandled)
