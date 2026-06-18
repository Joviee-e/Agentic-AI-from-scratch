
import asyncio
import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("News_Api")

async def fetch_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

            print("\nTop Headlines\n:")

            for article in data.get("articles", [])[:5]:
                print(article["title"])

asyncio.run(fetch_news())