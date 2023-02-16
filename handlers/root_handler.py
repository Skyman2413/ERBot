# coding: utf8
from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
import standartMessages

router = Router()


@router.message(Command(commands=["start"]))
async def cmd_start(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer(standartMessages.start, parse_mode="HTML")
