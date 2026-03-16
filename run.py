import os
import asyncio
from aiogram import Bot, Dispatcher, F

from dotenv import load_dotenv
from app.hendlers import router

dp = Dispatcher()

async def main(): 
    load_dotenv()
    bot = Bot(token=os.getenv('TG_TOKEN'))
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    dp.include_router(router)
    await dp.start_polling(bot)
    
async def startup(dispatcher: Dispatcher):
    print('starting up...')
    
async def shutdown(dispatcher: Dispatcher):
    print('Shutting down...')

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass