import asyncio

shared_rresource = 0
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_rresource
    async with lock:
        print(f"Resource before modification: {shared_rresource}")
        shared_rresource += 1
        await asyncio.sleep(1)
        print(f"Resource after modification: {shared_rresource}")


async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))


asyncio.run(main())