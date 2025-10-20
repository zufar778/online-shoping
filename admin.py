from aiogram import  Router, F
from aiogram.types import  CallbackQuery
from inline_buttons import menyu
from config import admins

a_router=Router()

@a_router.callback_query(F.data=='admin')
async def sending(call: CallbackQuery):
    for i in admins:
        xab=f"[{call.from_user.full_name}](tg://user?id={call.from_user.id})"
        await call.message.answer('Sorov yuborildi')
        await call.bot.send_message(chat_id=i, text=f"Sizga {xab} dan so'rov bor", parse_mode="MarkdownV2", reply_markup=menyu)