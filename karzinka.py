from aiogram import  Router, F
from aiogram.types import  CallbackQuery
from db import  karzin
from inline_buttons import menyu


k_router=Router()

@k_router.callback_query(F.data=='karzinka')
async def korish(call: CallbackQuery):
      user_id=call.from_user.id
      await call.message.answer('Sotib olingan narsalar')     
      for i in karzin(user_id):
            h=0
            h+=i[3]
            await call.message.answer(f"{i[2]} {i[4]} tasi {i[3]} som")
      await call.message.answer(f" Umumiy narx: {h}", reply_markup=menyu)
            
