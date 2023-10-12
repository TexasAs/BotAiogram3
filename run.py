import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.handlers import router
from app.states import router2


load_dotenv()
# Polling, т.е бесконечный цикл проверки апдейтов
async def main():
    bot = Bot(os.getenv('YOUR_TOKEN'))
    dp = Dispatcher()
    dp.include_routers(router, router2)
    await dp.start_polling(bot)


# Функция main() запускается только в случае если скрипт запущен с этого файла
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')