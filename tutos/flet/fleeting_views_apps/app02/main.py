import flet as ft

import FleetingViews as fvs
from views.home import HomeView
from views.about import AboutView


def main(page: ft.Page):
    page.title = "Fleeting pages"
    
    views = {
        "home": {"bgcolor": "blue"},
        "about": {"bgcolor": "red"},
    }
    
    fv = fvs.create_views(
        view_definitions=views,
        page=page,
    )
    about_controls, update_about_page = AboutView(fv)
    
    fv.append("home", HomeView(fv, update_about_page))
    fv.append("about", about_controls)

    fv.view_go("home")


ft.app(main)
