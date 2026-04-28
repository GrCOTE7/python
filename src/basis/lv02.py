import flet as ft


def main(page: ft.Page):
    page.title = "Simple routing #02"

    async def go_about(e):
        # await api_call() # Exemple si req API nécessaire avant change route
        await page.push_route("/about")

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
                    ft.Button("Go to about page", on_click=go_about)
                ],
            )
        )

        # About view
        if page.route == "/about":
            page.views.append(
                ft.View(
                    route="/about",
                    controls=[
                        ft.Text("About page"),
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
