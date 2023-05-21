from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import SheetsAPI
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import gspread

bot = Bot(token="5715651192:AAHvCCg-3KZmA3BOtFzqxCAjiTDQEzq7xEg")
dp = Dispatcher(bot)

isWork = False

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, '👋🏻 Привет!'
                                                 '\nДобро пожаловать в клан <b>Отстраненные</b>.'
                                                  , parse_mode="HTML", reply_markup=markup)

@dp.message_handler(Text(equals="⏩Обновить состав⏪"))
async def Members(message: types.Message):
    global isWork
    if not isWork:
        isWork = True
        await bot.send_message(message.from_user.id, "Обновление состава начато")

        SheetsAPI.checkPlayers(sh)

        await bot.send_message(message.from_user.id, "Состав обновлен", reply_markup=markup)
        isWork = False

@dp.message_handler(Text(equals="⏩Новые рейды⏪"))
async def Raids(message: types.Message):
    global isWork
    if not isWork:
        isWork = True
        await bot.send_message(message.from_user.id, "Обновление данных рейдов начато")

        SheetsAPI.setRaidResults(sh)

        await bot.send_message(message.from_user.id, "Обновление данных рейдов закончено", reply_markup=markup)
        isWork = False

@dp.message_handler(Text(equals="⏩ТАБЛИЦА⏪"))
async def SheetLink(message: types.Message):
    await bot.send_message(message.from_user.id, "⬇️⬇️⬇️", reply_markup=link)

btn_link = InlineKeyboardButton('Открыть таблицу', url='https://docs.google.com/spreadsheets/d/1WXli0D45kkwCV1fq2zB3WSkuzT0XPiMrhYDrk-zypQA/')
link = InlineKeyboardMarkup(row_width=1).add(btn_link)

button1 = KeyboardButton("⏩Обновить состав⏪")
button2 = KeyboardButton("⏩Новые рейды⏪")
button3 = KeyboardButton("⏩ТАБЛИЦА⏪", url= 'https://docs.google.com/spreadsheets/d/1WXli0D45kkwCV1fq2zB3WSkuzT0XPiMrhYDrk-zypQA/')

markup = ReplyKeyboardMarkup(resize_keyboard=True).row(button1).add(button2).add(button3)

if __name__ == '__main__':
    gc = gspread.service_account(filename='googleKeys.json')
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1WXli0D45kkwCV1fq2zB3WSkuzT0XPiMrhYDrk-zypQA/').sheet1

    executor.start_polling(dp, skip_updates=True)