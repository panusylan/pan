import asyncio
from modules.dex_parser import fetch_new_tokens

async def main():
    print("Бот запускается...")
    while True:
        print("Вызываем fetch_new_tokens()...")
        await fetch_new_tokens()
        print("Ждем 3 минуты...")
        await asyncio.sleep(180)

if __name__ == "__main__":
    asyncio.run(main())
