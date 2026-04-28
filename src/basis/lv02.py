import flet as ft


def main(page: ft.Page):
    page.title = "Simple routing #02"

    async def go_about(_: ft.Event[ft.ElevatedButton]):
        await page.push_route("/about")

    async def go_home(_: ft.Event[ft.ElevatedButton]):
        await page.push_route("/")

    def route_change(e: ft.RouteChangeEvent | None = None):
        print(f"Route change: {page.route}")

        page.views.clear()

        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.Text("Home page"),
                    ft.ElevatedButton("Go to about page", on_click=go_about),
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
                        ft.ElevatedButton("Go to home page", on_click=go_home),
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
