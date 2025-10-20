from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from db import Maxsulotlar



buying=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='ha', callback_data='ha'), InlineKeyboardButton(text='yoq', callback_data='yoq')]
    ]
)
menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Menyu 📝", callback_data="menyu")],
        [InlineKeyboardButton(text="Karzinka 🛒", callback_data="karzinka"), InlineKeyboardButton(text="admin 🙍‍♂️", callback_data="admin")]
    ]
)

def MenyuButtons():
    buttons = InlineKeyboardBuilder()
    for text in Maxsulotlar():
        buttons.add(InlineKeyboardButton(text=f"{text[1]}", callback_data=f"{text[1]}"))
    buttons.add(InlineKeyboardButton(text="ortga ⬅️", callback_data="ortga"))
    buttons.adjust(2)
    return buttons.as_markup()




def RaqamButtons():
    buttons = InlineKeyboardBuilder()
    for text in range(1, 10):
        buttons.add(InlineKeyboardButton(text=f"{text}", callback_data=f"{text}"))
    buttons.add(InlineKeyboardButton(text="ortga ⬅️", callback_data="ortga"))
    buttons.adjust(3)
    return buttons.as_markup()

