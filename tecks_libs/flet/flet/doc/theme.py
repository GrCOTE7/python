from ctypes import alignment
import flet as ft
from theTime import theTime as tt


import flet_lottie as fl


def main(page: ft.Page):

    def example():
        t = ft.Tabs(
            selected_index=1,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="Tab 1",
                    content=ft.Container(
                        content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                    ),
                ),
                ft.Tab(
                    tab_content=ft.Icon(ft.Icons.SEARCH),
                    content=ft.Container(content=ft.Text("This is Tab 2"), padding=10),
                ),
                ft.Tab(
                    text="Tab 3",
                    icon=ft.Icons.SETTINGS,
                    content=ft.Text("This is Tab 3"),
                ),
            ],
            expand=1,
        )

        c = ft.Container(
            content=t,
            height=300,
            width=300,
            border=ft.border.all(1, "grey"),
            border_radius=ft.border_radius.all(8),
            theme=ft.Theme(
                tabs_theme=ft.TabsTheme(
                    divider_color=ft.Colors.BLUE,
                    indicator_color=ft.Colors.RED,
                    indicator_tab_size=True,
                    label_color=ft.Colors.GREEN,
                    unselected_label_color=ft.Colors.AMBER,
                    overlay_color={
                        ft.ControlState.FOCUSED: ft.Colors.with_opacity(
                            0.2, ft.Colors.GREEN
                        ),
                        ft.ControlState.DEFAULT: ft.Colors.with_opacity(
                            0.2, ft.Colors.PINK
                        ),
                    },
                )
            ),
        )

        return c

    # Yellow page theme with SYSTEM (default) mode
    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.YELLOW,
    )

    page.add(
        # Page theme
        ft.Container(
            theme_mode=ft.ThemeMode.SYSTEM,
            content=ft.ElevatedButton("Page theme button"),
            bgcolor=ft.Colors.BLUE_ACCENT_200,
            padding=20,
            width=300,
        ),
        # Inherited theme with primary color overridden
        ft.Container(
            theme_mode=ft.ThemeMode.DARK,
            theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.Colors.PINK)),
            content=ft.ElevatedButton("Inherited theme button"),
            bgcolor=ft.Colors.ERROR,
            padding=20,
            width=300,
        ),
        # Unique always DARK theme
        ft.Container(
            theme=ft.Theme(color_scheme_seed=ft.Colors.INDIGO),
            theme_mode=ft.ThemeMode.DARK,
            content=ft.ElevatedButton("Unique theme button"),
            # content_color=ft.CupertinoColors.SYSTEM_BLUE,
            bgcolor=ft.CupertinoColors.ACTIVE_ORANGE,
            padding=20,
            width=300,
        ),
    )

    def on_keyboard(e: ft.KeyboardEvent):
        page.add(
            ft.Text(
                f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
            )
        )

    page.add(example())
    
    page.on_keyboard_event = on_keyboard
    page.add(
        ft.Text("Press any key with a combination of CTRL, ALT, SHIFT and META keys...")
    )


    print(tt(), page.route)


ft.app(main)
