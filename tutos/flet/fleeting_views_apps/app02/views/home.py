import flet as ft


def HomeView(fv, update_about_page):
    input_field = ft.TextField(label="input here")

    def go_about(e):
        fv.set_shared("user_input", {
          'val':input_field.value
        })
        fv.view_go('about?this_parameter=123')
        update_about_page()
        
    return [
        ft.Column(
            [
                ft.Text("This is the Home Page", size=30),
                input_field,
                ft.Button("Send to ABOUT page", on_click=go_about),
            ]
        )
    ]
