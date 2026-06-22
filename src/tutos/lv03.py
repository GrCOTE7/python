import flet as ft
import pathlib, sys

print(">>> LE SCRIPT SE LANCE BIEN <<<")
print("PYTHON =", sys.executable)
print("FLET   =", ft.__version__)

print(">>> SCRIPT LANCÉ <<<")

async def lv03(page: ft.Page):
    print(">>> LV03 APPELÉ <<<")
    page.title = "Tableau HTML avec LaTeX"

    # → Sert uniquement à ouvrir un navigateur web avec le tableau HTML généré par le tuto lv03.py
    # Impossible à l'heure actuelle d'afficher le tableau HTML directement dans l'application Flet, car Flet ne supporte pas encore l'intégration de contenu HTML complexe avec LaTeX. Cependant, vous pouvez ouvrir le fichier HTML dans un navigateur web pour visualiser le tableau correctement formaté.
    # Un solution existe qd même, mais très lourde : Utiliser un navigateur headless (Playwright ou Puppeteer)
    # from playwright.sync_api import sync_playwright

    # def capture_html():
    #     with sync_playwright() as p:
    #         browser = p.chromium.launch()
    #         page = browser.new_page()
    #         page.goto("file:///D:/Py/src/tutos/tableau.html")
    #         page.screenshot(path="tableau.png", full_page=True)
    #         browser.close()
    
    # page.padding = 20
    # with open("tableau.html", "r", encoding="utf-8") as f:
    #     html = f.read()

    # page.add(
    #     ft.WebView(
    #         content=html,
    #         expand=True
    #     )
    # )
    
    # await page.launch_url("http://localhost:5173/tableau.html")

    # html_path = pathlib.Path("tutos/tableau.html").absolute().as_uri()
    # await page.launch_url(html_path)
    
    # page.add(
    #     ft.Image(
    #         src="tableau.png",
    #         width=800,
    #         height=600,
    #         fit=ft.ImageFit.CONTAIN
    #     )
    # )

    page.add(ft.Text('Ready'))

    
if __name__ == "__main__":
    print(">>> MAIN <<<")
    ft.app(target=lv03)

