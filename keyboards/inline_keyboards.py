from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def gen_keyboard(button_dict: dict, sizes: tuple, value: str):
    keyboard = InlineKeyboardBuilder()
    for text, callback_data in button_dict.items():
        button = InlineKeyboardButton(
            text=text,
            callback_data=f"{value}_{callback_data}"
        )
        keyboard.add(button)
    keyboard.adjust(*sizes)
    return keyboard.as_markup()


def start_inline_kb():

    return gen_keyboard(
        {
            "Show word": "show",
            "Test": 'test',
            "Find word": 'find',
            "Translator": "translator",
        },
        sizes=(3,),
        value="start"
    )


