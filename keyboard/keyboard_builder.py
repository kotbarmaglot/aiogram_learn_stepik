from environs import Env
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text, Command
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove, KeyboardButtonPollType)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo


env: Env = Env()
env.read_env()

bot_token = env('BOT_TOKEN')

bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher()

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

i = 0

web_app_btn: KeyboardButton = KeyboardButton(
                                text='Start Web App',
                                web_app=WebAppInfo(url="https://www.youtube.com/"))

buttons1: list[KeyboardButton] = [KeyboardButton(
    text=f'Кнопка {i + 1}') for i in range(6)]

buttons2: list[KeyboardButton] = [KeyboardButton(
    text=f'Кнопка {i + 7}') for i in range(10)]

contact_btn: KeyboardButton = KeyboardButton(text='Отправить телефон',
                                             request_contact=True)

geo_btn: KeyboardButton = KeyboardButton(text='Отправить геолокацию',
                                         request_location=True)

poll_btn: KeyboardButton = KeyboardButton(
    text='Создать опрос/викторину',
    request_poll=KeyboardButtonPollType())


kb_builder.row(contact_btn, geo_btn, poll_btn, width=1)

# keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True,
#                                                      one_time_keyboard=True)


# Создаем объект клавиатуры
web_app_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                            keyboard=[[web_app_btn]],
                                            resize_keyboard=True)


# Создаем список списков с кнопками
keyboard: list[list[KeyboardButton]] = [
    [KeyboardButton(text=str(i)) for i in range(1, 4)],
    [KeyboardButton(text=str(i)) for i in range(4, 7)],
    [KeyboardButton(text=str(i)) for i in range(7, 9)]]

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True)


# kb_builder.row(*buttons1, width=4)
# kb_builder.row(*buttons2, width=4)
# kb_builder.adjust(4, 1, 2, repeat=True)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Вот такая получается клавиатура',
                         reply_markup=my_keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)
