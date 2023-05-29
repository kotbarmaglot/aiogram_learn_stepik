from environs import Env
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)


env: Env = Env()
env.read_env()

bot_token = env('BOT_TOKEN')

bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher()


button1: KeyboardButton = KeyboardButton(text='Собак')
button2: KeyboardButton = KeyboardButton(text='Огурцов')


keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[button1, button2]],
    resize_keyboard=True,
    one_time_keyboard=True
)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Чего кошки боятся больше?',
                         reply_markup=keyboard)


@dp.message(Text(text='Собак'))
async def process_dog_answer(message: Message):
    await message.answer(text='Да, несомненно, кошки боятся собак. '
                              'Но вы видели как они боятся огурцов?')


@dp.message(Text(text='Огурцов'))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов '
                              'кошки боятся больше')


if __name__ == '__main__':
    dp.run_polling(bot)
