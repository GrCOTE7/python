import flet as ft
import pathlib, sys

print(">>> LE SCRIPT SE LANCE BIEN <<<")
print("PYTHON =", sys.executable)
print("FLET   =", ft.__version__)

print(">>> SCRIPT LANCÉ <<<")

async def lv03(page: ft.Page):
    print(">>> LV03 APPELÉ <<<")
    page.title = "Tutos #03"

    # html_path = pathlib.Path("src/tutos/tableau.html").absolute().as_uri()
    # print(">>> URL =", html_path)
    # await page.launch_url(html_path)
    
    await page.launch_url("http://localhost:8000/tableau.html")


if __name__ == "__main__":
    print(">>> MAIN <<<")
    ft.app(target=lv03)

