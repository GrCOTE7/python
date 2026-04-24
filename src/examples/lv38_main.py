import flet as ft
import sys
from pathlib import Path

# Allow running this file directly: python src/examples/lv38_main.py
SRC_ROOT = Path(__file__).resolve().parents[1]
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from examples.lv38_solitaire import Solitaire
from tools.screen_utils import gc7_rules as gc7


def main(page: ft.Page):

    gc7(page, width=710)
    title = "Setup - Solitaire #38"
    page.title = title.replace("-", "|")
    page.add(ft.Text(title, size=18, weight=ft.FontWeight.BOLD))
    page.bgcolor = ft.Colors.GREEN_900

    solitaire = Solitaire()
    page.add(solitaire)


if __name__ == "__main__":
    ft.run(main, assets_dir="images")
