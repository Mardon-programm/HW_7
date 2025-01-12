from aiogram.fsm.state import State, StatesGroup

class Student(StatesGroup):
    name = State()
    age = State()
    num_phone = State()

student_data ={}