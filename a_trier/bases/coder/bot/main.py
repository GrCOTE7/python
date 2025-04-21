# https://www.youtube.com/watch?v=yEYN4P0lRzY

from tkinter import N
import pyautogui as pag
import time

time.sleep(2)

print("-" * 77)
print(pag.size())

pag.moveTo(1920 / 2, 1080 / 2, 1)
pag.move(200, 200, 1)
# pag.rightClick(1200,500)
print(pag.position())
# pag.write("oki", 1)
# pag.press('enter')

sc = pag.screenshot(region=(100, 100, 200, 200))
sc.save("uuu.png")
