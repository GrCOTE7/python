import flet as ft
from theTime import theTime as tt
from theTime import nf

def main(page: ft.Page):
    
    page.add(ft.Text('Ready.'))

    print(tt(), page.route)


ft.app(main)
