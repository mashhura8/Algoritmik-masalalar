# # Aiogram
# import asyncio
# from aiogram import Bot, Dispatcher
# from aiogram.filters import CommandStart, Command
# from aiogram.types import Message
#
# bot = Bot(token='8248582988:AAE20Jg5hJl_2jnz1muIIdRcbbO6D-Jnr_E')
# dp = Dispatcher()
#
#
# @dp.message(CommandStart())
# async def command_start(message: Message):
#     await message.reply(f"Assalomu alaykum, {message.from_user.full_name}!")
#
#
# @dp.message(Command("info"))
# async def command_info(message: Message):
#     await message.reply("Siz 9 (A) sinf botiga xush kelibsiz!\nBu bot orqali siz o'quvchilar va o'qituvchilar bilan bog'lanishingiz mumkin.")
#
# @dp.message(Command("salomlash"))
# async def command_salomlash(message: Message):
#     await message.reply("Assalomu alaykum, Telegram Botimizga xush kelibsiz!")
#
#
#
# async def main():
#     await dp.start_polling(bot)
#
# if __name__ == '__main__':
#     asyncio.run(main())
#
#
