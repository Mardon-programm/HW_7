import os, asyncio, logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from app.start import start_router
from app.person import student_router
import aioschedule


logging.basicConfig(level=logging.DEBUG)

load_dotenv()

bot = Bot(token=os.environ.get("token"))
dp = Dispatcher()

user_schedules = {} 

@dp.message(Command('set_schedule'))
async def set_schedule(message: types.Message):
    user_id = message.from_user.id
    time = message.get_args()
    
    if not time:
        await message.reply("Пожалуйста, укажите время в формате 'HH:MM'.")
        return

    user_schedules[user_id].append(time)
    await message.reply(f"Уведомление будет отправлено каждый день в {time}.")
    

    aioschedule.every().day.at(time).do(send_notification, chat_id=message.chat.id)


async def send_notification(chat_id):
    await bot.send_message(chat_id, "Пора выполнить задачу!")

@dp.message(Command('view_schedule'))
async def view_schedule(message: types.Message):
    user_id = message.from_user.id
    schedule = user_schedules.get(user_id, [])
    
    if not schedule:
        await message.reply("У вас нет запланированных уведомлений.")
    else:
        await message.reply("Ваше расписание:\n" + "\n".join(schedule))

@dp.message(Command('delete_schedule'))
async def delete_schedule(message: types.Message):
    user_id = message.from_user.id
    time = message.get_args()
    
    if time in user_schedules.get(user_id, []):
        user_schedules[user_id].remove(time)
        await message.reply(f"Уведомление в {time} удалено.")
    else:
        await message.reply(f"Уведомление в {time} не найдено.")

async def schedule_jobs():
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def main():
    dp.include_router(start_router)
    dp.include_router(student_router)
    loop = asyncio.get_event_loop()
    loop.create_task(schedule_jobs())
    dp.start_polling(dp, skip_updates=True)

    await dp.start_polling(bot)

asyncio.run(main())