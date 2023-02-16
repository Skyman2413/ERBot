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
    await msg.answer(standartMessages.thebook, reply_markup=keyboards.common_kb.get_yes_no_keyboard(),
                     parse_mode="HTML")
    await state.set_state(TheBookStates.first_line)


@router.callback_query(TheBookStates.first_line, F.text == "yes")
async def thebook_yes_first(msg: Message, state: FSMContext):
    '''TODO реализовать отправку фрагментов книг и отзывов'''
    await msg.answer(standartMessages.advert, reply_markup=keyboards.common_kb.get_yes_no_keyboard())
    await state.set_state(TheBookStates.second_line)


@router.callback_query(TheBookStates.first_line, F.text == "no")
async def thebook_no_first(msg: Message, state: FSMContext):
    await msg.answer(standartMessages.back_to_services)
    await state.clear()


@router.callback_query(TheBookStates.first_line, F.text == "yes")
async def thebook_want_to_buy(msg: Message, state: FSMContext):
    await msg.answer(standartMessages.contacts)
    await state.clear()
