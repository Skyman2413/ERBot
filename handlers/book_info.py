from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

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


@router.callback_query(TheBookStates.first_line)
async def thebook_first(callback: CallbackQuery, state: FSMContext):
    '''TODO реализовать отправку фрагментов книг и отзывов'''
    if callback.data == "yes":
        await callback.message.answer(standartMessages.advert, reply_markup=keyboards.common_kb.get_yes_no_keyboard())
        await state.set_state(TheBookStates.second_line)
        await callback.answer()
    elif callback.data == "no":
        await callback.message.answer(standartMessages.back_to_services)
        await state.clear()
        await callback.answer()


@router.callback_query(TheBookStates.second_line)
async def thebook_want_to_buy(callback: CallbackQuery, state: FSMContext):
    if callback.data == "yes":
        await callback.message.answer(standartMessages.contacts)
        await state.clear()
        await callback.answer()
    elif callback.data == "no":
        await callback.message.answer(standartMessages.back_to_services)
        await state.clear()
        await callback.answer()
