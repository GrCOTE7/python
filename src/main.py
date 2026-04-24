from re import A

import flet as ft
import datetime, time
import asyncio
import importlib.util
from pathlib import Path
from tools.screen_utils import gc7_rules as gc7


async def main(page: ft.Page, width: int = 392):
    # gc7(page, mode="LIGHT", name="Cookbook", width=900, height=700)
    # gc7(page, mode="LIGHT", width=width)
    # 1520 → à droite écran 1 si défini - 1912 à gche écran 2 si indéfini

    # left = 1520 # Ligne à commenter pour avoir l'app sur écran #2

    gc7(page, left=1520 if "left" in locals() else 1912)

    ################################### Base ###################################
    from examples.lv00_matrice import main

    from basis.scroll_example import main
    from basis.lv01_essai import essai as main
    from basis.lv02_ready import main

    from examples.lv04_calc_ui import calc as main  # Juste le design
    from examples.lv05_calc_ui_reusable import calc as main  # Opérationnel

    from devs.lv01_icons_list import icons_list as main  # 3 versions dispos

    from devs.lv02_blocs import main as main

    # # ❌ Finir game NbreX
    from devs.lv05_nbre_x import game as main

    from cookbook.main import main as main

    from devs.lv10_tutos import ab_btn as main  # label alternatif et btn adapté
    from devs.lv10_tutos import tofs as main  # Mur de tofs

    # gc7(page, width=976)
    # gc7(page, "LIGHT", width=976)

    # main(page)

    ################################### ToDo ###################################

    from examples.lv06_todo_simple import todo_list as main  # Simple field + add btn

    # Test fonctions asynchones
    if 0:
        from examples.lv07_todo_async import todo_list as todo7
        from examples.lv06_async_todo_simple import todo_list as todo6_async

        async def fini():
            print(
                datetime.datetime.now().strftime("%H:%M:%S"), "> Todos 6 & 7 Ready.\n"
            )

        async def async_fctns():
            print(datetime.datetime.now().strftime("%H:%M:%S"), "> async_fctns")
            await asyncio.gather(todo6_async(page), todo7(page))
            await fini()

        await async_fctns()
        time.sleep(1)

    from examples.lv08_todo import todo_list as main  # 08

    from examples.lv09_todo_simple import todo9 as main  # 09 - As tuto

    from examples.lv09_todo import todo_list as main  # 09

    # page.add(ft.Text('─'*49))

    from examples.lv10_todo import todo as finalTodo

    # gc7(page, width=950)
    # finalTodo(page)

    from examples.lv11_todo import main  # + Footer

    from examples.lv11_todo_official import main

    # gc7(page, "LIGHT", width=600)

    # main(page)

    # * [ ] LV 12 à comprendre pour incorporer ici
    # ⚠️ render_views prend le contrôle total de la page → ne pas mélanger avec page.add()
    from examples.lv12_todo_reactive import main  # 12 - Reactiv Todo - Use return

    # main(page)
    # return  # render_views incompatible avec page.controls / page.add() ci-dessous

    ################################### CHAT ###################################

    # * [/] chat

    from examples.lv20_chat import main  # Base
    from examples.lv21_chat import main  # Add pubsub.subscribe ( Broadcasting)
    from examples.lv22_chat import main  # Login ( + auto login ) → --web
    from examples.lv23_chat import main  # Class + ↑ User msg design

    # ❌  2fix Chat #24
    from examples.lv24_chat import main  # SIMU login & msgs Scrolling auto

    # main(page)

    # gc7(page, "LIGHT")
    # main(page)

    ################################ SOLITAIRE  ################################

    from examples.lv30_a1_stack import main  # 3 image blocs
    from examples.lv30_a2_stack import main  # 3 cards (Bleu-blanc-rouge)
    from examples.lv30_a3_stack import main  # A card on a tapis

    from examples.lv30_solitaire import main  # GestureDetector (on_tap)
    from examples.lv31_solitaire import main  # drag a card
    from examples.lv32_solitaire import main  # drag to slot

    # gc7(page, mode="LIGHT", width=976)  # 976 pour // 2 l'écran de droite
    from examples.lv33_solitaire import (
        main,
    )  # drag a card on a slot else return back position

    # drag 2 cards with pans
    from examples.lv34_solitaire import main

    # drop in 3 slots
    from examples.lv35_solitaire import main

    # Classes for better code structure (POO)
    from examples.lv36_main import main

    # Fanned cards piles (Piles en éventail)
    from examples.lv37_main import main

    # Solitaire setup
    from examples.lv38_main import main

    # * [/] Solitaire general rules
    from examples.lv39_main import main

    # main(page)
    #

    ################################## CookBook ################################
    from cookbook.main import main  # Une série ~30 exemples classés par thème

    # (CRUD, Async, PubSub, Routing, etc.)
    # gc7(page, "LIGHT", width=976)
    # ❌ Finir de Vérif les cookbooks en les réactivant 1 à 1
    # main(page)
    #

    # ❌ Cf. fin de tuto + Étudier le seul qui corrige le pb de double clic → Le comprendre complètement à la fin - D:\flet_doc\sdk\python\examples\tutorials\solitaire_declarative\solitaire-final\main.py

    ################################### FLETX ##################################
    ################################### FLETX ##################################

    # Pour tester rapidement:
    # À considérer : PY3.13.13 - Flet 0.84.0 - FletX 0.2.0
    # Fork du GH (Git clone https://github.com/GrCOTE7/python Py)
    # → Clone en local de VOTRE repo → Un dossier Py/ (Là où vous avez lancé)
    # À la racine (Py/) : Si vous êtes sous Win: ./go + enter
    # Et sinon: uv run --active run flet -r
    # Régler la ligne 16 si la résolution de votre écran n'est pas 1920x1080 (ex: 2560x1440 → left=2000) pour que la fenêtre s'ouvre sur le bon écran, et si pas 2 écrans, la commenter pour avoir le rendu de la fenêtre de l'app à droite de votre écran principal

    # Ensuite, pour tester, juste déplacer le: main(page) → Affichera l'import juste avant

    # from fletx_tuto.lv00 import main  # Simple counter Flet sans réactivité
    # from fletx_tuto.lv01 import main  # Counter avec RxInt + obx (réactivité auto)

    # lv02 dépend d'une API legacy (Xapp) absente selon la version de fletx installée.
    # ❌ 2fix from fletx_tuto.lv02 import main  # type: ignore[assignment]

    # lv03 peut ne pas exposer un symbole `main` suivant la variante du tuto.
    from fletx_tuto.lv03_routing import run_app as main  # Routing avec ModuleRouter + @register_router
    main()

    #################################### Dev ###################################

    from devs.lv00_dev import dev as main

    # main(page)

    if not page.controls:
        page.add(
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                margin=ft.Margin.only(top=25),
                controls=[
                    ft.Text(
                        "No content.",
                        size=30,
                        color=ft.Colors.RED_ACCENT_200,
                        weight=ft.FontWeight.BOLD,
                    )
                ],
            )
        )


if __name__ == "__main__":
    print(datetime.datetime.now().strftime("%H:%M:%S"), "> ")
    ft.run(main)
