from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

import keyboards.services_kb
import standartMessages

router = Router()


@router.message(Command(commands=["services"]))
@router.message(Text(text="Услуги"))
async def cmd_services(msg: Message, state:FSMContext):
    await msg.answer(standartMessages.services, parse_mode="HTML", disable_web_page_preview=True,
                     reply_markup=keyboards.services_kb.services_kb())
    await state.clear()


@router.callback_query(Text(text="1"))
async def archive_search(callback: CallbackQuery):
    await callback.message.answer(standartMessages.services_1, parse_mode="HTML", disable_web_page_preview=True)
    await callback.answer()


@router.callback_query(Text(text="2"))
async def archive_search(callback: CallbackQuery):
    await callback.message.answer(standartMessages.services_2, parse_mode="HTML", disable_web_page_preview=True)
    await callback.answer()


@router.callback_query(Text(text="3"))
async def archive_search(callback: CallbackQuery):
    await callback.message.answer(standartMessages.services_3, parse_mode="HTML", disable_web_page_preview=True)
    await callback.answer()


@router.callback_query(Text(text="4"))
async def archive_search(callback: CallbackQuery):
    await callback.message.answer(standartMessages.services_4, parse_mode="HTML", disable_web_page_preview=True)
    await callback.answer()


@router.callback_query(Text(text="5"))
async def archive_search(callback: CallbackQuery):
    await callback.message.answer(standartMessages.services_5, parse_mode="HTML", disable_web_page_preview=True)
    await callback.answer()


@router.callback_query(Text(text="6"))
async def archive_search(callback: CallbackQuery):
    await callback.message.answer(standartMessages.services_6, parse_mode="HTML", disable_web_page_preview=True)
    await callback.answer()


@router.message(Command(commands=["mean"]))
async def send_more_info(message: Message):
    await message.answer(standartMessages.messageA, parse_mode="HTML", disable_web_page_preview=True)


@router.message(Command(commands=["more"]))
async def send_more_info(message: Message):
    await message.answer(standartMessages.messageB, parse_mode="HTML", disable_web_page_preview=True)

