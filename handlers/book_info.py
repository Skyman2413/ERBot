from aiogram import Router, F
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

import keyboards.common_kb
import standartMessages

router = Router()


class TheBookStates(StatesGroup):
    first_line = State()
    second_line = State()


@router.message(Command(commands=["thebook"]))
async def cmd_thebook(msg: Message, state: FSMContext):
    await msg.answer(standartMessages.thebook_message, reply_markup=keyboards.common_kb.get_yes_no_keyboard(),
                     parse_mode="HTML")
    await state.set_state(TheBookStates.first_line)


@router.callback_query(TheBookStates.first_line, F.text == "yes")
async def thebook_yes_first(msg: Message, state: FSMContext):
    '''TODO реализовать отправку фрагментов книг и отзывов'''
    await state.set_state(TheBookStates.second_line)
