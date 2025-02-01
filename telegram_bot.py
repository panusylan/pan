from telegram import Bot
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def send_to_telegram(name, price, contract_address, twitter_url, website_url):
    bot = Bot(token=TOKEN)
    message = (f"🔥 Новый токен обнаружен!\n\n"
               f"📌 Название: {name}\n"
               f"💰 Цена: {price}\n"
               f"🔗 Контракт: {contract_address}\n"
               f"🔍 DexScreener: https://dexscreener.com/solana/{contract_address}\n"
               f"🐦 Twitter: {twitter_url}\n"
               f"🌍 Website: {website_url}")

    await bot.send_message(chat_id=CHAT_ID, text=message)
