import flet as ft
import sys
from pathlib import Path
from datetime import datetime


tools_path = Path(__file__).parent.parent.parent.parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import *
import time


def main(page: ft.Page):

    now = datetime.now()
    theTime = f"{now.hour: >2}:{now.minute:0>2}:{now.second:0>2}"
    # sys.stdout.write(f"\r{thetime}")

    # page.controls.append(ft.Text("Fini"))
    # page.update()

    content = ft.Text("Ok", size=48)

    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)
        page.update()
        time.sleep(0.3)

    page.add(content)

    print(theTime)
    # exit()


ft.app(main)
