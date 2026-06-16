import flet as ft


def main(page: ft.Page):
    page.title = "Simple routing #03"
    yourparams = None  # ou "Lionel"
    # yourparams = "Lionel"

    async def go_about(e):
        # await api_call() # Exemple si req API nécessaire avant change route
        route = f"/about/{yourparams}" if yourparams else "/about"
        print(route)
        await page.push_route(route)

    async def go_home(e):
        await page.push_route("/")

    # --- Routing ---
    def route_change(e=None):
        print("Route change:", page.route)

        page.views.clear()

        # Home view
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.Text("Home page"),
                    ft.Button("Go to about page", on_click=go_about),
                ],
            )
        )

        # About view (with param or not)
        if page.route == "/about" or page.route.startswith("/about/"):
            param = None
            if page.route.startswith("/about/"):
                param = page.route.split("/about/", 1)[1] or None
            page.views.append(
                ft.View(
                    route=page.route,
                    controls=[
                        ft.Text(f"About page - param: {param}"),
                        ft.Button("Go to home page", on_click=go_home),
                    ],
                )
            )

        page.update()

    # --- Back navigation ---
    async def view_pop(e):
        page.views.pop()
        await page.push_route(page.views[-1].route)

    # --- Bind events ---
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # --- Initial route ---
    if not page.route:
        page.route = "/"
    route_change()


if __name__ == "__main__":
    ft.run(main)
