from aiogram.fsm.state import State, StatesGroup

class product(StatesGroup):
    all=State()
    pro=State()
    b=State()
    number=State()


class Karzinka(StatesGroup):
    contact = State()
    manzil = State()
    tasdiqlash = State()

class admin_add(StatesGroup):
    nomi=State()
    narx=State()
    rasm=State()
    about=State()