from aiogram.fsm.state import State, StatesGroup

class Reg(StatesGroup):
    name = State()
    age = State()
    photo = State()