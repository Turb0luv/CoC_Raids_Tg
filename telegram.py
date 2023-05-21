from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import SheetsAPI
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

bot = Bot(token="5715651192:AAHvCCg-3KZmA3BOtFzqxCAjiTDQEzq7xEg")
dp = Dispatcher(bot)

isWork = False

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, '👋🏻 Привет!'
                                                 '\nДобро пожаловать в панель статистики клана <b>Отстраненные</b>.'
                                                 '\n<b>Clash of Clans</b>'
                                                  , parse_mode="HTML", reply_markup=markup)

@dp.message_handler(Text(equals="⏩Результаты КВ⏪"))
async def Members(message: types.Message):
    global isWork
    if not isWork:
        isWork = True
        await bot.send_message(message.from_user.id, "Обновление результатов начато...")

        SheetsAPI.setWarResults()

        await bot.send_message(message.from_user.id, "Результаты обновлены!", reply_markup=markup)
        isWork = False

@dp.message_handler(Text(equals="⏩Результаты рейдов⏪"))
async def Raids(message: types.Message):
    global isWork
    if not isWork:
        isWork = True
        await bot.send_message(message.from_user.id, "Обновление результатов рейдов начато...")

        SheetsAPI.setRaidResults()

        await bot.send_message(message.from_user.id, "Результаты обновлены!", reply_markup=markup)
        isWork = False

@dp.message_handler(Text(equals="⏩ТАБЛИЦА⏪"))
async def SheetLink(message: types.Message):
    await bot.send_message(message.from_user.id, "⬇️⬇️⬇️", reply_markup=link)

btn_link = InlineKeyboardButton('Открыть таблицу', url='https://docs.google.com/spreadsheets/d/1WXli0D45kkwCV1fq2zB3WSkuzT0XPiMrhYDrk-zypQA/')
link = InlineKeyboardMarkup(row_width=1).add(btn_link)

button1 = KeyboardButton("⏩Результаты КВ⏪")
button2 = KeyboardButton("⏩Результаты рейдов⏪")
button3 = KeyboardButton("⏩ТАБЛИЦА⏪", url= 'https://docs.google.com/spreadsheets/d/1WXli0D45kkwCV1fq2zB3WSkuzT0XPiMrhYDrk-zypQA/')

markup = ReplyKeyboardMarkup(resize_keyboard=True).add(button1).add(button2).row(button3)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)