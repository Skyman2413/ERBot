from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

import keyboards.common_kb
import standartMessages

router = Router()


class FaqStates(StatesGroup):
    first_line = State()


@router.message(Command(commands=["FAQ"]))
async def cmd_faq(msg: Message, state: FSMContext):
    await msg.answer(standartMessages.faq, reply_markup=keyboards.common_kb.get_yes_no_keyboard(),
                     parse_mode="HTML")
    await state.set_state(FaqStates.first_line)


@router.callback_query(FaqStates.first_line)
async def faq(callback: CallbackQuery, state: FSMContext):
    if callback.data == "no":
        await callback.message.answer(standartMessages.back_to_services)
        await state.clear()
        await callback.answer()
    elif callback.data == "yes":
        await callback.message.answer(standartMessages.contacts, parse_mode="HTML")
        await state.clear()
        await callback.answer()
