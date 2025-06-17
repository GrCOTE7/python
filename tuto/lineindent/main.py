import flet as ft
from theTime import theTime as tt
from theTime import nf

import os

#SUPABASE
URL: str = ''
KEY: str = ''


def main(page: ft.Page):

    t = ft.Text("Oki 21", size=20, color="cyan")
    page.add(t)

    print(tt(), page.route)


if __name__ == "__main__":

    ft.app(main)
