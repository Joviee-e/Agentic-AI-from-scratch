import asyncio
import aiohttp
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("Weather_Api")


async def fetch_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

            # Error handling
            if response.status != 200:
                print("\nError:")
                print(data.get("message", "Unknown error"))
                return

            print(f"\nWeather in {city.title()}")
            print("-" * 30)
            print(f"Temperature : {data['main']['temp']} °C")
            print(f"Feels Like  : {data['main']['feels_like']} °C")
            print(f"Humidity    : {data['main']['humidity']}%")
            print(f"Pressure    : {data['main']['pressure']} hPa")
            print(f"Weather     : {data['weather'][0]['description'].title()}")
            print(f"Wind Speed  : {data['wind']['speed']} m/s")


async def main():
    city = input("Enter city name: ").strip()
    await fetch_weather(city)


if __name__ == "__main__":
    asyncio.run(main())