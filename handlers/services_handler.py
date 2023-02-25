import os
from aiogram import Router, F
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, FSInputFile, InputMediaDocument

import standartMessages
import keyboards

router = Router()


class ServiceStates(StatesGroup):
    select_service = State()


@router.message(Command(commands=["services"]))
@router.message(Text(text="Услуги"))
async def cmd_services(msg: Message, state: FSMContext):
    await msg.answer(standartMessages.services, parse_mode="HTML", disable_web_page_preview=True)
    await state.set_state(ServiceStates.select_service)


@router.message(ServiceStates.select_service, Command(commands=["1"]))
async def archive_search(msg: Message, state: FSMContext):
    await msg.answer(standartMessages.services_1, parse_mode="HTML", disable_web_page_preview=True)


@router.message(ServiceStates.select_service, Command(commands=["2"]))
async def archive_search(msg: Message, state: FSMContext):
    await msg.answer(standartMessages.services_2, parse_mode="HTML", disable_web_page_preview=True)


@router.message(ServiceStates.select_service, Command(commands=["3"]))
async def archive_search(msg: Message, state: FSMContext):
    await msg.answer(standartMessages.services_3, parse_mode="HTML", disable_web_page_preview=True)


@router.message(ServiceStates.select_service, Command(commands=["4"]))
async def archive_search(msg: Message, state: FSMContext):
    await msg.answer(standartMessages.services_4, parse_mode="HTML", disable_web_page_preview=True)


@router.message(ServiceStates.select_service, Command(commands=["5"]))
async def archive_search(msg: Message, state: FSMContext):
    await msg.answer(standartMessages.services_5, parse_mode="HTML", disable_web_page_preview=True)


@router.message(ServiceStates.select_service, Command(commands=["6"]))
async def archive_search(msg: Message, state: FSMContext):
    await msg.answer(standartMessages.services_6, parse_mode="HTML", disable_web_page_preview=True)


@router.message(ServiceStates.select_service, Command(commands=["mean"]))
async def send_more_info(msg: Message, state: FSMContext):
    await msg.answer(standartMessages.messageA, parse_mode="HTML", disable_web_page_preview=True)


@router.message(ServiceStates.select_service, Command(commands=["more"]))
async def send_more_info(msg: Message, state: FSMContext):
    await msg.answer(standartMessages.messageB, parse_mode="HTML", disable_web_page_preview=True)

