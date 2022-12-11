from aiogram import *
from aiogram.types import *
from aiogram.utils import executor
from datetime import date

TOKEN = "5865860744:AAG4oMuAE0tjeKj2ze6jLDdKfrj0Tl5iQCs"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

button = ReplyKeyboardMarkup(resize_keyboard=True).row('⏳ Сколько осталось до нового года? ⏳')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    anm = open('animation.tgs', 'rb')
    await bot.send_animation(message.chat.id, anm)
    await bot.send_message(message.chat.id, f'👋Здравствуй дорогой *{message.from_user.first_name}*.\n*Чeм я вам могу помочь ?*', reply_markup=button, parse_mode='Markdown')

@dp.message_handler()
async def event(message: types.Message):
    today = date.today()
    d, m, y = today.strftime("%d %m %Y").split()
    if message.text == '⏳ Сколько осталось до нового года? ⏳':
        await message.answer(f'🗓 <b><i>{31-int(d)}</i></b> дней осталось до 🎄<b>НОВОГО ГOДA</b>🎄', parse_mode='html')

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)





