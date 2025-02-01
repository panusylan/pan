import asyncio
from playwright.async_api import async_playwright

async def fetch_new_tokens():
    """
    Функция подключается к уже запущенному реальному Chrome (с включённой отладкой через CDP)
    и открывает сайт DexScreener.
    
    Перед запуском скрипта обязательно запустите Chrome с нужным профилем, например, командой:
    
    "C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Profile 2" --remote-debugging-port=9222
    """
    async with async_playwright() as p:
        try:
            # Подключаемся к запущенному экземпляру Chrome по протоколу CDP
            browser = await p.chromium.connect_over_cdp("http://localhost:9222")
        except Exception as e:
            print("Не удалось подключиться к Chrome через CDP:", e)
            return

        # Если в браузере уже существуют контексты, используем первый; иначе создаём новый.
        if browser.contexts:
            context = browser.contexts[0]
        else:
            context = await browser.new_context()

        page = await context.new_page()

        # Добавляем скрипт для удаления признака автоматизации (navigator.webdriver)
        await page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)

        print("Открываем DexScreener...")
        await page.goto("https://dexscreener.com/solana?rankBy=trendingScoreM5&order=desc&maxAge=1")
        await asyncio.sleep(10)  # Ждем загрузки страницы
        print("Dexscreener открыт!")
        
        # Здесь мы не закрываем браузер, чтобы не завершить ваш реальный экземпляр Chrome.
        # Если нужно закрыть только страницу, можно выполнить: await page.close()
