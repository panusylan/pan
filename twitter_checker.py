from playwright.async_api import async_playwright

async def check_twitter(twitter_url):
    if not twitter_url:
        return False

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(twitter_url)
        await page.wait_for_load_state("networkidle")

        try:
            followers = await page.inner_text("xpath=//span[contains(text(),'Followers')]/preceding-sibling::span")
            followers_count = int(followers.replace(",", ""))
            
            posts = await page.query_selector_all("xpath=//div[contains(@class, 'tweet')]")
            post_count = len(posts)

            return followers_count >= 1000 and post_count >= 10
        except Exception:
            return False
