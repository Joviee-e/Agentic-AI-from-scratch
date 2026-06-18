import asyncio

async def fetch_data(delay, id):
    print(f"Fetching data from {id}")
    await asyncio.sleep(delay)
    print(f"Data fetched from {id}")
    return {"id": id, "data": f"Data from {id}"}

#coroutine function
async def main():
    task1 = fetch_data(2, "1")
    task2 = fetch_data(3, "2")

    result1 = await task1
    result2 = await task2

    print("Results:")
    print(result1)
    print(result2)

#main()
asyncio.run(main())