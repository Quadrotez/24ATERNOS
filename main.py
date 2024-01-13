from aiogram import Bot, Dispatcher, types, F

from configparser import ConfigParser
import mf
import asyncio
import threading


config = ConfigParser()
config.read('config.ini')


dp = Dispatcher()

bot = Bot(token=config['SECURITY']['TOKEN'])

@dp.message(F.text)
async def main_text(message: types.Message):
    if message.text.lower() == '/start':
        await message.reply('Запуск бота...')
        thread = threading.Thread(target=mf.start())
        thread.start()
        thread.join()

    elif message.text.lower() == '/stop':
        await message.reply('Остановка бота...')
        thread = threading.Thread(target=mf.stop())
        thread.start()
        thread.join()

async def main():
    await dp.start_polling(bot)



# keep_alive()
asyncio.run(main())
