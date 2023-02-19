from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

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


@router.callback_query(FaqStates.first_line, F.text == "no")
async def faq_yes(msg: Message, state: FSMContext):
    await msg.answer(standartMessages.back_to_services)
    await state.clear()


@router.callback_query(FaqStates.first_line, F.text == "yes")
async def faq_no(msg: Message, state: FSMContext):
    await msg.answer(standartMessages.contacts)
    await state.clear()
