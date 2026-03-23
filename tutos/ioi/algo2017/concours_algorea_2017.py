import flet as ft
from re import S
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent / "tools"))
from tools import *
from tools import cls, ls

sys.path.append(str(Path(__file__).resolve().parent.parent))
from mvts import *
from datetime import datetime as dt

# import o1_grands_plateaux as gp
import o2_dist_min as dm

# https://concours.algorea.org/contents/4807-4802-1735320797656206224-103413922876285801-586581477687690666/
# https://www.youtube.com/watch?v=LXT5prbKUMM&list=PLZZpsVWcTOhEtUyJKPvFuJ53g7bVAZDTy&index=6&ab_channel=ThinhNguyen


def main(page: ft.Page):
    page.title = "Algorea 2017"
    page.add(ft.Text("Hello World !"))
    # gp.case(page, ls)
    dm.case(page, ls)


if __name__ == "__main__":
    cls(" old.algorea.org")
    now = dt.now()
    tt = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"
    print("Ready.", tt)
    ls()
    # ft.app(target=main, view=ft.WEB_BROWSER)
    ft.app(target=main)
    # CLI: flet run -d -r --web file.py
