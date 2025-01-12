from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from app.state import Student, student_data
from app.utils import schedule_task
from app.state import  student_data
from datetime import datetime
from app.db import saved_db

student_router = Router()

@student_router.message(Student.name)
async def name(message:types.Message, state=FSMContext):
    student_data['name'] = message.text
    await message.reply("Введите ваш номер телевона: ")
    await state.set_state(Student.age)

@student_router.message(Student.age)
async def num_phone(message:types.Message, state=FSMContext):
    student_data['num_phone'] = message.text
    await message.reply("Введите ваш возраст: ")
    await state.set_state(Student.num_phone)

        
@student_router.message(Student.num_phone)
async def age(message: types.Message, state: FSMContext):
    student_data['age'] = message.text
    await message.reply("Спасибо! Вы зарегистрированы.")
    await state.close()