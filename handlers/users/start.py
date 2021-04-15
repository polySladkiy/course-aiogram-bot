from re import compile

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters import IsPrivate
from loader import dp


# /d/d/d - <цифра><цифра><цифра>
@dp.message_handler(CommandStart(deep_link=compile(r"\d\d\d")), IsPrivate())
async def bot_start(message: types.Message):
    deep_link_args = message.get_args()
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"Вы находитесь в личной переписке.\n"
                         f"В вашей команде диплинк.\n"
                         f"Ваша диплинк ссылка - {deep_link_args}")


@dp.message_handler(CommandStart(deep_link=None), IsPrivate())
async def bot_start(message: types.Message):
    bot_user = await dp.bot.get_me()
    deep_link = f"http://t.me/{bot_user.username}?start=123"

    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"Вы находитесь в личной переписке.\n"
                         f"В вашей команде нет диплинка.\n"
                         f"Ваша диплинк ссылка - {deep_link}")
