import asyncio

print("Code Execution Started")


async def display():
    await asyncio.sleep(3)
    print("Welcome to Guru99 Tutorials\n")


asyncio.run(display())

print("Fini", '-'*56, '\n')

import time

my_message = "Guru99"
for i in my_message:
    print(i)
    time.sleep(1)

print("\nFini2", '-'*55, '\n')

