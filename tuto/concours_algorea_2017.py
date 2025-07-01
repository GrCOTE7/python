import algo2017.grands_plateaux as gp
import flet as ft
from re import S
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "tools"))
from tools import *
from tools import cls
from mvts import *
from datetime import datetime as dt

# https://concours.algorea.org/contents/4807-4802-1735320797656206224-103413922876285801-586581477687690666/
# https://www.youtube.com/watch?v=LXT5prbKUMM&list=PLZZpsVWcTOhEtUyJKPvFuJ53g7bVAZDTy&index=6&ab_channel=ThinhNguyen


def main(page: ft.Page):
    page.title = "Algorea 2017"
    page.add(ft.Text("Hello World 21 !"))


if __name__ == "__main__":
    cls(" old.algorea.org")
    now = dt.now()
    tt = f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}"
    gp.case()
    print("Ready.", tt)
    ft.app(target=main)
    # exit()
