from aiogram import *
from aiogram.types import *
from aiogram.utils import executor
import time

TOKEN = "5728446541:AAHUJrHGCh8Gweoh8uoxdJg2in1SE12TGY4"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Отсчёт пошёл ⏳')
    msg = await message.answer('1')
    n = 1
    while n<60:
        time.sleep(1)
        n += 1 
        await msg.edit_text(str(n))
    await message.answer('Время вышло ⌛️')

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)



