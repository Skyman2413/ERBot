from pathlib import Path
from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto
import keyboards.common_kb
import standartMessages

router = Router()


class TheBookStates(StatesGroup):
    first_line = State()
    second_line = State()


@router.message(Command(commands=["thebook"]))
@router.message(Text(text="Купить книгу"))
async def cmd_thebook(msg: Message, state: FSMContext):
    root_path = Path.cwd()
    file1 = FSInputFile(Path(root_path, "documents", "Oblozhki.jpg"))
    file2 = FSInputFile(Path(root_path, "documents", "Chetyre_veka_istorii_odnoy_semi.jpg"))
    file3 = FSInputFile(Path(root_path, "documents", "Istoricheskaya_rodoslovnaya_kasimovskikh_tatar.jpg"))
    file4 = FSInputFile(Path(root_path, "documents", "Rodoslovnaya_kniga.jpg"))
    await state.set_state(TheBookStates.first_line)
    await msg.answer(standartMessages.thebook, parse_mode="HTML", disable_web_page_preview=True)
    await msg.answer_media_group([InputMediaPhoto(media=file1), InputMediaPhoto(media=file2),
                                  InputMediaPhoto(media=file3), InputMediaPhoto(media=file4)])
    await msg.answer("Посмотреть отрывок из книги и отзывы?", reply_markup=keyboards.common_kb.get_yes_no_keyboard())


@router.callback_query(TheBookStates.first_line, Text(text="yes"))
async def thebook_first_yes(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(standartMessages.advert, parse_mode="HTML", disable_web_page_preview=True)
    await callback.answer()


@router.callback_query(TheBookStates.first_line, Text(text="no"))
async def thebook_first_no(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(standartMessages.back_to_services)
    await state.clear()
    await callback.answer()
