import asyncio

#semaphore allows a certain number of coroutines to access a resource concurrently

async def access_resource(semaphore, id):
    async with semaphore:
        print(f"Accessing resource {id}")
        await asyncio.sleep(1)
        print(f"Releasing resource {id}")


async def main():
    semaphore = asyncio.Semaphore(2) # allow only 2 coroutines to access the resource concurrently
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5))) # '*' is used to unpack the list of coroutines into individual arguments for gather

asyncio.run(main())