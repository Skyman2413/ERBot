from aiogram import Router
from aiogram.types import Message, CallbackQuery
import standartMessages

router = Router()


@router.message()
async def unhandled_message(msg: Message):
    await msg.answer(standartMessages.unhandled)


@router.callback_query()
async def unhandled_callback(callback: CallbackQuery):
    await callback.message.answer(standartMessages.unhandled_1)
    await callback.answer()
