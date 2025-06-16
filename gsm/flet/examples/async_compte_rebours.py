import flet as ft
import sys
from pathlib import Path
from datetime import datetime
import time
import asyncio

tools_path = Path(__file__).parent.parent.parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import *


class Countdown(ft.Text):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds

    def did_mount(self):
        self.running = True
        self.page.run_task(self.update_timer)

    def will_unmount(self):
        self.running = False

    async def update_timer(self):
        while 0 <= self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            await asyncio.sleep(1)
            self.seconds -= 1


def main(page: ft.Page):

    now = datetime.now()
    theTime = f"{now.hour: >2}:{now.minute:0>2}:{now.second:0>2}"
    # sys.stdout.write(f"\r{theTime}")

    page.title = "Test"
    page.add(Countdown(77), Countdown(10))
    
    t=ft.Text('Oki!')
    page.add(t)
    
    print(theTime, page.route)
    # exit()


ft.app(main)
