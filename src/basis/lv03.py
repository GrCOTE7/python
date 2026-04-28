import flet as ft


def main(page: ft.Page):
    page.title = "LV 03 - Routing #03"

    async def go_about(_: ft.Event[ft.Button]):
        # await some_api_call() # Une méthode asynchrone pour faire une requête API avant de changer de route
        await page.push_route("/about")

    def route_change(e: ft.RouteChangeEvent | None = None):
        print(f"Route change: {page.route}")

        page.views.clear()

        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.Text("Home page"),
                    ft.Button(
                        # "Go to about page", on_click=lambda _: page.go("/about")
                        "Go to about page",
                        on_click=go_about,
                    ),
                    ft.Text("Oki", color=ft.Colors.BLACK, size=20),
                ],
            ),
        )
        if page.route == "/about":
            page.views.append(
                ft.View(
                    route="/about",
                    controls=[
                        ft.Text("About page"),
                        ft.Button(
                            "Go to home page", on_click=lambda e: page.push_route("/")
                        ),
                    ],
                ),
            )

        page.update()

    async def view_pop(e: ft.ViewPopEvent):
        page.views.pop()
        top_view = page.views[-1]
        await page.push_route(top_view.route)

    page.on_route_change = route_change

    page.on_view_pop = view_pop

    if not page.route:
        page.route = "/"
    route_change()


if __name__ == "__main__":

    ft.run(main)
