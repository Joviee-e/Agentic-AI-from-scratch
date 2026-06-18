import asyncio

#not good for error handling and if one task fails, all tasks will fail

async def fetch_data(delay, id):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(delay)
    return {"id": id, "data": f" Sample data from coroutine {id}"}

async def main():
    result = await asyncio.gather(fetch_data(2 , 1), fetch_data(3 , 2), fetch_data(1 , 3))

    for results in result:
        print(results)


asyncio.run(main())