from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact_phone = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Contact ulashish", request_contact=True)]
    ],
    resize_keyboard=True
)


location_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Location ulashish", request_location=True)]
    ],
    resize_keyboard=True
)
