from threading import Timer

print("Code 1 Execution Started")

def display():
    print("Welcome to Guru99 Tutorials")


t = Timer(5, display) # EN sous-tâche...
t.start()
t.join() # bloque le programme principal jusqu’à ce que le timer se termine
print("-" * 72)

from threading import Event

print("Code 2 Execution Started")


def display():
    print("Welcome to Guru99 Tutorials")


Event().wait(5)
display()
print("-" * 72)


import asyncio

print("Code 3 Execution Started")


async def display():
    await asyncio.sleep(5)
    print("Welcome to Guru99 Tutorials")


asyncio.run(display())
print("-" * 72)

import time

print("ça va démarrer dans 3 secondes...")
time.sleep(3)
print("Go !")


for i in range(1, 6):
    time.sleep(1)
    print(i)

print("-" * 72)
