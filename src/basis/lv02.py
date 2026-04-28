import flet as ft


def main(page: ft.Page):
    page.title = "Simple routing #02"

    def route_change(e: ft.RouteChangeEvent | None = None):
        print(f"Route change: {page.route}")

        page.views.clear()
        
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.Text("Home page"),
                    ft.ElevatedButton(
                        "Go to about page", on_click=lambda _: page.go("/about")
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
                        ft.ElevatedButton(
                            "Go to home page", on_click=lambda _: page.go("/")
                        ),
                    ],
                ),
            )
            
        page.update()

    def view_pop(e: ft.ViewPopEvent):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    
    page.on_view_pop = view_pop
    
    if not page.route:
        page.route = "/"
    route_change()


if __name__ == "__main__":

    ft.run(main)
