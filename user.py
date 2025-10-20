from aiogram import  Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from inline_buttons import menyu, MenyuButtons, RaqamButtons, buying
from db import Maxsulotlar, MaxsulotAdds, qosh
from states import product
from aiogram.fsm.context import FSMContext

router = Router()



@router.message(CommandStart())
async def StartBot(message: Message, state: FSMContext):
    try:
        user_id=message.from_user.id
        name=message.from_user.first_name
        username=message.from_user.username
        qosh(user_id, name, username)
        await message.answer_photo(photo="https://www.arzaan.pk/cdn/shop/articles/3.jpg",caption=f"Assalomu alaykum Dokonimizga Xush kelibsiz\n\n{message.from_user.first_name}", reply_markup=menyu)

    except:
        await message.answer_photo(photo="https://www.arzaan.pk/cdn/shop/articles/3.jpg",caption=f"Welcome back Dokonimizga Xush kelibsiz\n\n{message.from_user.first_name}", reply_markup=menyu)




@router.callback_query(F.data=='menyu')
async def Menyubot(call: CallbackQuery, state: FSMContext):
    await call.message.answer_photo(photo="https://g2u-wp-prod.s3-ap-southeast-2.amazonaws.com/wp-content/uploads/2022/09/Online-shopping-hero.jpg", caption="Bizdagi maxsulotlar !!", reply_markup=MenyuButtons())
    await state.set_state(product.pro)



    

@router.callback_query(F.data, product.pro)
async def MaxsulotBots(call: CallbackQuery, state: FSMContext):
    xabar = call.data
    for text in Maxsulotlar():
        if text[1] == xabar:
            await call.message.answer_photo(photo=f"{text[3]}", caption=f"Nomi: {text[1]}\nNarxi: {text[2]}\nXaqida: {text[4]}", reply_markup=RaqamButtons())
            await state.update_data(name=f"{text[1]}", price=f"{text[2]}" )
            await state.set_state(product.number)
            break
        elif xabar=='ortga':
            await state.set_state(product.pro)
            await call.message.answer('Tanlang:', reply_markup=menyu)
            break
    else:
        await call.answer("mavjud emas")



@router.callback_query(product.number)
async def raq(call: CallbackQuery, state: FSMContext):
    try:
        data=await state.get_data()
        name=data.get('name')
        price=float(data.get('price'))
        xabar=int(call.data)
        user_id=call.from_user.id
        print(xabar*price)
        MaxsulotAdds(user_id=user_id, name=name, price=(xabar*price),count=xabar)
        await call.message.answer('added')
        await state.set_state(product.pro)
        await call.message.answer_photo(photo="https://g2u-wp-prod.s3-ap-southeast-2.amazonaws.com/wp-content/uploads/2022/09/Online-shopping-hero.jpg", caption="Bizdagi maxsulotlar !!", reply_markup=MenyuButtons())

    except:
        await state.set_state(product.pro)
        await call.message.answer_photo(photo="https://g2u-wp-prod.s3-ap-southeast-2.amazonaws.com/wp-content/uploads/2022/09/Online-shopping-hero.jpg", caption="Bizdagi maxsulotlar !!", reply_markup=MenyuButtons())
