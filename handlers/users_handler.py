from asgiref.sync import sync_to_async
from aiogram import Bot, types, Router, F
from aiogram.filters import CommandStart, Command, StateFilter
from keyboards import inline_keyboards, reply_keyboard
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from googletrans import Translator

from queries import query

translator = Translator()

users_router = Router()


class TranslatorState(StatesGroup):
    word = State()


class FindWordState(StatesGroup):
    word = State()


@users_router.message(CommandStart())
async def start_command(message: types.Message, bot: Bot):

    chat_id = message.chat.id
    first_name = message.chat.first_name
    username = message.chat.username
    user = query.get_user(chat_id, first_name, username)


    message_to_user = """
Assalomu alaykum, ushbu bot hozir test jarayonida.
Hozir faqatgina "Translator" bo'limi to'liq ishlayapti. 
Qolgan bo'limlar ishlab chiqilish jarayonida...
"""
    await bot.send_message(chat_id=message.chat.id,
                           text=message_to_user,
                           reply_markup=inline_keyboards.start_inline_kb())


@users_router.message(TranslatorState.word)
async def translater(message: types.Message, bot: Bot, state: FSMContext):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    username = message.chat.username
    user = query.get_user(chat_id, first_name, username)

    if message.text == 'Back':
        await message.answer("Translation has been stopped!", reply_markup=reply_keyboard.ReplyKeyboardRemove())
        await state.clear()
        return await start_command(message, bot)
    lang = translator.detect(message.text).lang
    dest = 'uz' if lang == 'en' else 'en'
    await message.reply(translator.translate(message.text, dest).text)


@users_router.callback_query(StateFilter(None), F.data.startswith('start'))
async def something(callback: types.CallbackQuery, state: FSMContext):
    chat_id = callback.message.chat.id
    first_name = callback.message.chat.first_name
    username = callback.message.chat.username
    user = query.get_user(chat_id, first_name, username)

    data = callback.data.split('_')[1]

    if data == 'translator':
        await callback.message.answer(text="Matn kiriting: ", reply_markup=reply_keyboard.kb)
        await state.set_state(TranslatorState.word)

    if data == "find":
        text = "So'z topish faollashdi! (stop - tugatish)"

        word, user_word_ids = await sync_to_async(query.get_random_word)([])
        text_uz = word.text_uz

        message_to_user = f"""
        [{text_uz.title()}] - inglizchasini yozing?
        """
        await callback.message.answer(text=text)
        await callback.message.answer(message_to_user)
        await state.set_state(FindWordState.word)

    if data == "test":
        pass

    await callback.answer()


@users_router.message(FindWordState.word)
async def find_words(message: types.Message, bot: Bot, state: FSMContext):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    username = message.chat.username
    user = await sync_to_async(query.get_user)(chat_id, first_name, username)

    user_text = message.text

    if user_text.lower() == "stop":
        await state.clear()
        return await start_command(message, bot)

    word, user_word_ids = await sync_to_async(query.get_random_word)([])

    text_uz = word.text_uz

    message_to_user = f"""
[{text_uz.title()}] - inglizchasini yozing?
"""
    return await message.answer(message_to_user)






