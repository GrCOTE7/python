import flet as ft


def AboutView(fv):
    shared_text = ft.Text()
    param_text = ft.Text()

    def update_data():
        shared_value = fv.get_shared("user_input", {"val": "no value from home"})
        param_value = fv.get_param("this_parameter", "no param from home")

        shared_text.value = f"shared : {shared_value['val']}"
        param_text.value = f"param : {param_value['val']}"

        fv.page.update()

    controls = [
        ft.Column(
            [
                ft.Text("This is the About Page", size=30),
                shared_text,
                param_text,
                ft.Button(
                    "Go Back HOME !",
                    on_click=lambda e: fv.view_go("home"),
                ),
            ]
        )
    ]

    return controls, update_data
