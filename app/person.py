from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from app.state import Student, student_data
from app.utils import schedule_task
from app.state import  student_data
from datetime import datetime

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
    
@student_router.message(Student.schedule)
async def process_schedule_time(message: types.Message, state: FSMContext):
    try:
        deadline_time = datetime.strptime(message.text, "%d.%m.%Y %H:%M")  # Обратите внимание на формат даты
        student_data['deadline'] = deadline_time
        await message.answer(f"Задание будет выполнено в {deadline_time.strftime('%d.%m.%Y %H:%M')}")
        await schedule_task(deadline_time) 
        await state.finish()  
    except ValueError:
        await message.reply("Неверный формат даты, пожалуйста, введите в формате 'дд.мм.гггг чч:мм'")