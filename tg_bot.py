import asyncio
import json
import aiogram
from aiogram import types
from mongo_worker import aggregate_payments
from const import ERROR_MSG, TELEGRAM_TOKEN


async def handle_message(message: aiogram.types.Message):
    try:
        data = json.loads(message.text)
        dt_from = data.get("dt_from")
        dt_upto = data.get("dt_upto")
        group_type = data.get("group_type")
        result = await aggregate_payments(dt_from, dt_upto, group_type)
        formatted_json = json.dumps(result)
    except json.JSONDecodeError:
        result = ERROR_MSG
    await message.answer(formatted_json)


async def handle_start(message: aiogram.types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}!")


async def main():
    bot = aiogram.Bot(token=TELEGRAM_TOKEN)
    dp = aiogram.Dispatcher(bot)
    dp.register_message_handler(handle_start, commands=["start"])
    dp.register_message_handler(callback=handle_message,
                                content_types=types.ContentType.TEXT,
                                state="*")
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
