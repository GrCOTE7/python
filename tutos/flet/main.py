import flet as ft

def main(page: ft.Page):

    txt = 'Ready.'
    print(txt)

    page.add(ft.Text(txt))
    page.update()

if __name__ == "__main__":

    ft.run(main)
