from aiogram import  Router, F
from aiogram.types import Message, ChatPermissions
from aiogram.filters import CommandStart, and_f
import time

router = Router()


@router.message(CommandStart(), F.chat.type=="supergroup")
async def StartBot(message: Message):
    await message.answer(f"Assalomu alaykum {message.from_user.first_name}")


@router.message(F.chat.type=="supergroup", F.new_chat_members)
async def AddUsers(message: Message):
    users = message.new_chat_members
    for user in users:
        await message.answer(f"Assalomu alaykum Guruhga xush kelibsiz\n\n{user.first_name}")




@router.message(F.chat.type=="supergroup", F.left_chat_member)
async def LeftUsers(message: Message):
    user = message.left_chat_member
    await message.answer(f"Xayr do'stim kelib turing: {user.first_name}")



@router.message(F.chat.type == 'supergroup',and_f(F.text == "yoz", F.reply_to_message))
async def get_not_ban_chat(message: Message):
   user_id = message.reply_to_message.from_user.id
   permsions = ChatPermissions(can_send_messages=True)
   await message.chat.restrict(user_id, permsions)
   await message.answer(f"Siz endi yoza olasiz\n🆗 {message.reply_to_message.from_user.full_name}")



@router.message(F.chat.type == "supergroup",and_f(F.text == "ban", F.reply_to_message))
async def get_bann_chat(message: Message):
   user_id = message.reply_to_message.from_user.id
   await message.chat.ban_sender_chat(user_id)
   await message.answer(f"Siz guruhdan haydaldingiz\n ❌ {message.reply_to_message.from_user.full_name}")



@router.message(F.chat.type == "supergroup",and_f(F.text == "unban", F.reply_to_message))
async def get_unbann_chat(message: Message):
   user_id = message.reply_to_message.from_user.id
   await message.chat.unban_sender_chat(user_id)
   await message.answer(f"Siz endi guruhga qo'shila olasiz\n 🆗 {message.reply_to_message.from_user.full_name}")




@router.message(F.chat.type == 'supergroup')
async def get_banned_chat(message: Message):
   if message.text == "Salom":
        user_id = message.from_user.id
        permsions = ChatPermissions(can_send_messages=False)
        await message.chat.restrict(user_id, permsions)
        await message.answer(f"Siz notog'ri so'zdan foydlaandizngiz\n🚫 {message.from_user.full_name}")
        time.sleep(5)
        permsions = ChatPermissions(can_send_messages=True)
        await message.chat.restrict(user_id, permsions)
