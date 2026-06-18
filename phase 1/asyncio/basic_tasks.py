import asyncio

async def fetch_data(delay, id):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(delay)
    return {"id": id, "data": f" Sample data from coroutine {id}"}

async def main():
    #creating tasks
    task1 = asyncio.create_task(fetch_data(2 , 1))
    task2 = asyncio.create_task(fetch_data(3 , 2))
    task3 = asyncio.create_task(fetch_data(1 , 3))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)

asyncio.run(main())