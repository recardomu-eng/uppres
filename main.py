import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# Замени на свой токен от BotFather
TOKEN = "8635938067:AAEgWYwOAdIEsNBCBY0lfYYX5XcXJ8vy6RY"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    # Ссылка на твой будущий интерфейс (пока поставим заглушку)
    # Когда сделаешь сайт, заменишь google.com на свою ссылку
    web_app_url = "https://твой-сайт.рф" 
    
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Открыть Gift App 🎁", 
            web_app=WebAppInfo(url=web_app_url)
        )]
    ])
    
    await message.answer(
        f"Привет, {message.from_user.first_name}! \nНажми на кнопку ниже, чтобы посмотреть свои подарки:",
        reply_markup=markup
    )
@dp.message(F.content_type == "web_app_data")
async def process_win(message: types.Message):
    import json
    data = json.loads(message.web_app_data.data)
    
    if data['action'] == "win":
        await message.answer(
            f"💰 **Поздравляем!**\n"
            f"Вы успешно вывели {data['amount']} TON на коэффициенте {data['multiplier']}x!"
        )
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":

    asyncio.run(main())
