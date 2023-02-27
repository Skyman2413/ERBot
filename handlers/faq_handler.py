from aiogram import Router
from aiogram.filters import Command, Text
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
    await msg.answer(standartMessages.faq,
                     parse_mode="HTML", disable_web_page_preview=True)
    await msg.answer("У Вас остались вопросы?", reply_markup=keyboards.common_kb.get_yes_no_keyboard())
    await state.set_state(FaqStates.first_line)


@router.callback_query(FaqStates.first_line, Text(text="no"))
async def faq_no(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(standartMessages.back_to_services, disable_web_page_preview=True)
    await state.clear()
    await callback.answer()


@router.callback_query(FaqStates.first_line, Text(text="yes"))
async def faq_yes(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(standartMessages.contacts, parse_mode="HTML", disable_web_page_preview=True)
    await state.clear()
    await callback.answer()
