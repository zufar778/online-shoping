from aiogram import  Router, F
from aiogram.types import Message
from aiogram.filters import Command
from db import MaxsulotAdd
from states import admin_add
from aiogram.fsm.context import FSMContext
from config import admins
adm_router= Router()

@adm_router.message(Command('add'))
async def adadd(message: Message, state: FSMContext):
    user_id=message.from_user.id
    for i in admins:
        if user_id==i:
           await message.answer('Mahsulot nomini kiriting: ')
           await state.set_state(admin_add.nomi)

        

@adm_router.message(F.text, admin_add.nomi)
async def nom(message: Message, state: FSMContext):
    xabar=message.text
    await state.update_data(name=xabar)
    await message.answer('Mahsulot narxini kiriting: ')
    await state.set_state(admin_add.narx)


@adm_router.message(F.text, admin_add.narx)
async def nom(message: Message, state: FSMContext):
    xabar=message.text
    await state.update_data(price=xabar)
    await message.answer('Mahsulot rasmini kiriting: ')
    await state.set_state(admin_add.rasm)


@adm_router.message(F.photo, admin_add.rasm)
async def nom(message: Message, state: FSMContext):
    xabar=message.photo[-1].file_id
    await state.update_data(image=xabar)
    await message.answer('Mahsulot haqida: ')
    await state.set_state(admin_add.about)


@adm_router.message(F.text, admin_add.about)
async def nom(message: Message, state: FSMContext):
    xabar=message.text
    print(xabar)
    data =await state.get_data()
    name=data.get('name')
    price=data.get('price')
    image=data.get('image')
    dec=xabar
    print('fgh')
    MaxsulotAdd(name, price, image, dec)
    await message.answer('Qoshildi')
    await state.clear()
