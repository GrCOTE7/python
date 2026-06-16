import sys
from pathlib import Path

import flet as ft

# Ensure this file's directory is on sys.path so 'views' is always found.
sys.path.insert(0, str(Path(__file__).parent))


async def main(page: ft.Page) -> None:
    txt = "Oki"
    page.add(ft.Text(txt))


def run_app(page: ft.Page | None = None) -> None:
    # Standalone launch: create Flet page loop via ft.run.
    if page is None:
        ft.run(main)
        return


if __name__ == "__main__":
    ft.run(main)
    # run_app()
