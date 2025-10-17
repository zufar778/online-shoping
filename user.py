from aiogram import  Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from inline_buttons import menyu, MenyuButtons, RaqamButtons
from db import Maxsulotlar

router = Router()



@router.message(CommandStart(),)
async def StartBot(message: Message):
    await message.answer_photo(photo="https://www.arzaan.pk/cdn/shop/articles/3.jpg",caption=f"Assalomu alaykum Dokonimizga Xush kelibsiz\n\n{message.from_user.first_name}", reply_markup=menyu)


@router.callback_query(F.data=="menyu")
async def Menyubot(call: CallbackQuery):
    await call.message.answer_photo(photo="https://g2u-wp-prod.s3-ap-southeast-2.amazonaws.com/wp-content/uploads/2022/09/Online-shopping-hero.jpg", caption="Bizdagi maxsulotlar !!", reply_markup=MenyuButtons())


@router.callback_query(F.data)
async def MaxsulotBots(call: CallbackQuery):
    xabar = call.data
    for text in Maxsulotlar():
        if text[1] == xabar:
            await call.message.answer_photo(photo=f"{text[3]}", caption=f"Nomi: {text[1]}\nNarxi: {text[2]}\Xaqida: {text[4]}", reply_markup=RaqamButtons())
            break
    else:
        await call.answer("mavjud emas")