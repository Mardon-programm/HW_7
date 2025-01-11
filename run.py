import os, asyncio, logging
from aiogram import Bot, Dispatcher 
from dotenv import load_dotenv
from app.start import start_router
from app.person import student_router


logging.basicConfig(level=logging.DEBUG)

load_dotenv()

bot = Bot(token=os.environ.get("token"))
dp = Dispatcher()

async def main():
    dp.include_router(start_router)
    dp.include_router(student_router)

  

    await dp.start_polling(bot)

asyncio.run(main())