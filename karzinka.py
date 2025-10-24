from aiogram import  Router, F, Bot
from aiogram.types import  CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from states import Karzinka
from db import  karzin
from inline_buttons import buyurtma, buying
from reply import contact_phone, location_button
from config import admins


k_router=Router()

@k_router.callback_query(F.data=='karzinka')
async def korish(call: CallbackQuery):
      user_id=call.from_user.id
      await call.message.answer('Sotib olingan narsalar')  
      jami_summa = 0 
      text = "" 
      for i in karzin(user_id):
            jami_summa += i[3]
            text += f"Nomi: {i[2]}\nnarxi: {i[3]/i[4]} so'm\nSoni {i[4]}\nsummasi {i[3]} so'm\n\n"
      await call.message.answer(text=f"{text}\n\nJami summa: {jami_summa}", reply_markup=buyurtma)
            

@k_router.callback_query(F.data=="zakaz")
async def KarzinkaBot(call: CallbackQuery, state: FSMContext):
      await call.message.answer("Contactingizni yuboring", reply_markup=contact_phone)
      await state.set_state(Karzinka.contact)


@k_router.message(F.contact, Karzinka.contact)
async def ContactBot(message: Message, state: FSMContext):
      telefon = message.contact.phone_number
      await state.update_data({"telefon":telefon})
      await message.answer(text="endi location yuboring ", reply_markup=location_button)
      await state.set_state(Karzinka.manzil)


@k_router.message(F.location, Karzinka.manzil)
async def LocationBot(message: Message, state: FSMContext):
      la = message.location.latitude
      lo = message.location.longitude
      await state.update_data({"la":la, "lo":lo})
      await state.set_state(Karzinka.tasdiqlash)
      await message.answer("Tasdiqlash", reply_markup=buying)


@k_router.callback_query(F.data == "ha", Karzinka.tasdiqlash)
async def AdminBot(call: CallbackQuery, state: FSMContext):
      user_id = call.from_user.id
      data = await state.get_data()
      contact = data.get("telefon")
      la = data.get("la")
      lo = data.get("lo")
      jami_summa = 0 
      text = "" 
      for i in karzin(user_id):
            jami_summa += i[3]
            text += f"Nomi: {i[2]}\nnarxi: {i[3]/i[4]} so'm\nSoni {i[4]}\nsummasi {i[3]} so'm\n\n"
      await call.bot.send_location(chat_id =admins[0] ,latitude=la, longitude=lo)
      await call.bot.send_message(chat_id=admins[0], text=f"Telefon: {contact}\n{text}\n\nJami summa: {jami_summa}", reply_markup=buying)
      await state.clear()