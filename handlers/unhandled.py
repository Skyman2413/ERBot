from aiogram import Router
from aiogram.types import Message, CallbackQuery
import standartMessages

router = Router()


@router.message()
async def unhandled_message(msg: Message):
    await msg.answer(standartMessages.unhandled + msg.text)


@router.callback_query()
async def unhandled_callback(callback: CallbackQuery):
    await callback.answer(callback.data)
