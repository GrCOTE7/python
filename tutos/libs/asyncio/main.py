import asyncio

async def child():
    print("A", end="")
    await asyncio.sleep(.1)
    print("B", end="")
    return "C"

async def parent():
    print("D", end="")
    child_coro = child()
    await asyncio.sleep(1)
    print("E", end="")
    print(await child_coro, end="")

asyncio.run(parent())
