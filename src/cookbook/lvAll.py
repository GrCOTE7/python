import flet as ft
import asyncio, os, sys
from pathlib import Path


class Lv99(ft.Container):
    def __init__(self):
        super().__init__()

        self.padding = ft.Padding.symmetric(vertical=3, horizontal=10)
        self.border_radius = 7
        self.bgcolor = ft.Colors.LIGHT_GREEN_ACCENT_400
        self.content = ft.Text(
            "Ready.",
            color=ft.Colors.BLACK_87,
            size=18,
            weight=ft.FontWeight.BOLD,
            italic=True,
            font_family="Arial",
        )


class Lv00(ft.Column):  # Simple class with a custom text

    def __init__(self, txt: str = ""):
        c = controls = [
            ft.Row(
                controls=[
                    ft.Text("Titre", weight=ft.FontWeight.BOLD, size=18),
                    ft.Container(expand=True),  # Spacer
                    ft.Text(
                        "Leçon #00", size=16, italic=True, color=ft.Colors.CYAN_300
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Divider(color=ft.Colors.CYAN_ACCENT_400, thickness=2, height=2),
        ]
        if txt:
            controls.append(ft.Text(txt, size=18, color=ft.Colors.WHITE))

        super().__init__(c)


class Lv01(ft.Container):  # Form with a text field and a button

    def myInputFieldStyle(self, txt=None, label: bool = True):
        text_kwarg = {"label" if label else "hint_text": txt} if txt else {}
        sizes = 18, 14
        return ft.TextField(
            text_size=sizes[0],
            label_style=ft.TextStyle(size=sizes[1]),
            hint_style=ft.TextStyle(size=sizes[1]),
            border_color=ft.Colors.BLUE_GREY_400,
            border_width=1,  # épaisseur
            border_radius=7,
            expand=True,
            **text_kwarg,
        )

    def __init__(self):
        super().__init__()

        self.padding = 10
        self.border = ft.Border.all(2, ft.Colors.BLUE_GREY_200)
        self.border_radius = 10
        self.content = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.myInputFieldStyle("First Name", label=False),
                        self.myInputFieldStyle("Last Name"),
                        self.myInputFieldStyle(),
                    ],
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.Button(
                            "Join chat",
                            bgcolor="BLACK",
                            # border_color="GREEN",
                            style=ft.ButtonStyle(
                                animation_duration=500,
                                shape=ft.RoundedRectangleBorder(radius=4),
                                mouse_cursor=ft.MouseCursor.CLICK,
                                side=ft.BorderSide(width=2, color=ft.Colors.GREEN),
                                color={
                                    ft.ControlState.HOVERED: ft.Colors.RED,
                                    ft.ControlState.FOCUSED: ft.Colors.BLUE_800,
                                    ft.ControlState.DEFAULT: ft.Colors.WHITE_54,
                                },
                            ),
                        )
                    ],
                ),
            ]
        )


class Lv02(ft.SafeArea):  # 3 blocs in a row with different expand values and colors

    def __init__(self):
        content = self.threeBlocs()
        super().__init__(content=content)

    def threeBlocs(self):
        ink = ft.TextStyle(color=ft.Colors.BLACK_87, size=24)
        return ft.Container(
            width=500,
            padding=10,
            border=ft.Border.all(2, ft.Colors.BLUE_GREY_200),
            border_radius=10,
            content=ft.Row(
                spacing=8,
                controls=[
                    ft.Container(
                        expand=1,
                        height=60,
                        bgcolor=ft.Colors.CYAN_300,
                        alignment=ft.Alignment.CENTER,
                        border_radius=8,
                        content=ft.Text("1", style=ink),
                    ),
                    ft.Container(
                        expand=3,
                        height=60,
                        bgcolor=ft.Colors.AMBER_300,
                        alignment=ft.Alignment.CENTER,
                        border_radius=8,
                        content=ft.Text("3", style=ink),
                    ),
                    ft.Container(
                        expand=1,
                        height=60,
                        bgcolor=ft.Colors.PINK_200,
                        alignment=ft.Alignment.CENTER,
                        border_radius=8,
                        content=ft.Text("1", style=ink),
                    ),
                ],
            ),
        )


class State:  # A counter (Imperative)
    counter = 0


class Lv03(ft.SafeArea):  # A counter (Imperative)
    counter = 0

    def __init__(self):
        self.state = State()
        self.message = ft.Text("0", size=32, color=ft.Colors.BLACK_87)
        bloc = ft.Container(
            width=200,
            height=100,
            bgcolor=ft.Colors.CYAN_200,
            border_radius=8,
            content=ft.Stack(
                controls=[
                    ft.Container(
                        expand=True,
                        alignment=ft.Alignment.CENTER,
                        content=self.message,
                    ),
                    ft.Container(
                        right=12,
                        bottom=12,
                        content=ft.FloatingActionButton(
                            icon=ft.Icons.ADD,
                            mini=True,
                            on_click=self.handle_button_click,
                        ),
                    ),
                ]
            ),
        )

        super().__init__(
            expand=True,
            content=ft.Container(
                alignment=ft.Alignment.CENTER,
                content=bloc,
            ),
        )

    def handle_button_click(self, e: ft.Event[ft.FloatingActionButton]):
        self.state.counter += 1
        self.message.value = str(self.state.counter)
        self.message.update()


class Lv04(ft.Container):  # 3 blocs in a stack with different expand values and colors
    def __init__(self):
        super().__init__()

        my_stack = ft.Stack(
            controls=[
                ft.Container(
                    width=200,
                    height=200,
                    left=100,
                    top=20,
                    bgcolor=ft.Colors.BLUE,
                ),
                ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.Colors.RED,
                    top=50,
                    left=50,
                ),
                ft.Container(
                    width=50,
                    height=50,
                    bgcolor=ft.Colors.with_opacity(0.7, ft.Colors.YELLOW),
                    top=120,
                    left=120,
                ),
            ],
        )
        self.width = 300
        self.height = 240
        self.bgcolor = ft.Colors.GREEN_400
        self.padding = 12
        self.border_radius = 8
        self.content = my_stack


class Lv05(ft.Container):  # Row, Column, Container, Safearea, Stack

    def __init__(self):
        content = self.myCard()
        # content = self.mySerie()
        super().__init__(content=content)

    def myCard(self, myLabel: str = "Label"):
        return ft.Card(
            content=ft.Container(
                padding=ft.Padding.symmetric(horizontal=7, vertical=-3),
                border_radius=ft.BorderRadius.all(4),
                bgcolor=ft.Colors.AMBER_100,
                content=ft.Text(myLabel, color=ft.Colors.BLACK, size=24),
            ),
        )

    def mySerie(self):
        return ft.Row(  # Try Column / Row
            expand=True,
            height=100,
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls=[self.myCard(str(i)) for i in range(1, 6)],
        )


class Lv06(ft.Container):  # ResponsiveRow

    def __init__(self):
        content = self.myResponsiveRow()
        super().__init__(content=content)

    def myCard(self, myLabel: str = ""):
        return ft.Card(
            shape=ft.ContinuousRectangleBorder(radius=10),
            content=ft.Container(
                padding=ft.Padding.symmetric(horizontal=7, vertical=-3),
                border_radius=ft.BorderRadius.all(4),
                bgcolor=ft.Colors.AMBER_100,
                content=ft.Text(myLabel, color=ft.Colors.BLACK, size=24),
            ),
        )

    def myResponsiveRow(self):
        return ft.ResponsiveRow(
            controls=[
                ft.Button(
                    f"Button {i}",
                    color=ft.Colors.BLUE_GREY_300,
                    col={
                        ft.ResponsiveRowBreakpoint.XS: 12,
                        ft.ResponsiveRowBreakpoint.MD: 6,
                        ft.ResponsiveRowBreakpoint.LG: 3,
                    },
                )
                for i in range(1, 6)
            ],
        )


class Lv07(ft.Container):  # Shadow & Action

    def __init__(self):
        self.btn = self.myShadowedBtn()
        super().__init__(content=self.btn)

    def btnAction(self, e: ft.Event[ft.Button]):

        msg = f"Button {e.control.data} clicked!"
        e.control.content = msg
        e.control.update()
        print(msg)

    def longPress(self):
        print("Long Press!")

    def myBtn(self):
        label = "Lesson Lv07"
        return ft.Button(
            content=label,
            data="btn_" + label,
            on_click=self.btnAction,
            icon=ft.Icons.PARK_ROUNDED,
            icon_color=ft.Colors.GREEN_400,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=4),
                color={
                    ft.ControlState.HOVERED: ft.Colors.RED_700,
                    ft.ControlState.FOCUSED: ft.Colors.BLUE,
                    ft.ControlState.DEFAULT: ft.Colors.RED_300,
                },
                bgcolor={
                    ft.ControlState.FOCUSED: ft.Colors.PINK_200,
                    ft.ControlState.DEFAULT: ft.Colors.YELLOW_ACCENT_200,
                },
                mouse_cursor=ft.MouseCursor.CLICK,
                # elevation={
                #     ft.ControlState.DEFAULT: 0,
                #     ft.ControlState.HOVERED: 5,
                #     ft.ControlState.PRESSED: 10,
                # },
                # animation_duration=500,
            ),
            on_long_press=self.longPress,
        )

    def myShadowedBtn(self):
        return ft.Container(
            content=self.myBtn(),
            # border_radius=ft.BorderRadius.all(50),
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            shadow=ft.BoxShadow(
                color=ft.Colors.RED_400,
                blur_radius=10,
                offset=ft.Offset(5, 5),
            ),
        )


class Lv08(ft.Container):  # A container in another

    def __init__(self):
        super().__init__(
            expand=True,
            padding=ft.Padding.symmetric(horizontal=8, vertical=13),
            bgcolor=ft.Colors.RED,
            border_radius=ft.BorderRadius.all(10),
            alignment=ft.Alignment(1, 1),
            content=self.myLv08(),
        )

    def myLv08(self):

        return ft.Container(
            width=216,  # largeur du fond jaune
            height=54,
            padding=ft.Padding.symmetric(horizontal=20, vertical=8),
            alignment=ft.Alignment.CENTER,
            bgcolor=ft.Colors.YELLOW,
            border_radius=7,
            border=ft.Border.all(2, ft.Colors.BLACK_38),
            content=ft.Text(
                "#08",
                text_align=ft.TextAlign.CENTER,
                color=ft.Colors.BLACK,
                size=24,
            ),
        )


class Lv09(ft.Container):  # Fonts

    def __init__(self, page):
        super().__init__(
            content=self.myLv09(),
        )

        page.fonts = {
            "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
            "Open Sans": "/fonts/OpenSans-Regular.ttf",
            "Roboto Condensed": "https://raw.githubusercontent.com/google/fonts/main/apache/robotocondensed/RobotoCondensed-Regular.ttf",
        }
        print(page.fonts)

    def myLv09(self):

        doc = ft.Column()

        z = ft.Row()  # z → zône

        z.controls.append(ft.Image(src="icon.png", width=50, height=50))

        z.controls.append(
            ft.Column(
                controls=[
                    ft.Text(
                        "Premier texte de la leçon #09\n",
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.AMBER,
                        size=20,
                    ),
                    ft.Text(
                        "2ème texte de la leçon #09",
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.AMBER,
                        size=20,
                        font_family="Consolas",
                    ),
                ],
                spacing=-30,
            )
        )
        doc.controls.append(z)

        doc.controls.append(ft.Divider(color=ft.Colors.RED_ACCENT_400))

        doc.controls.append(
            ft.Text("Kanit", font_family="Kanit", size=20, color=ft.Colors.CYAN_700)
        )
        doc.controls.append(
            ft.Text(
                "Open Sans", font_family="Open Sans", size=20, color=ft.Colors.CYAN_700
            )
        )
        doc.controls.append(
            ft.Text(
                "Arial Gras",
                weight=ft.FontWeight.BOLD,
                font_family="Arial",
                size=20,
                color=ft.Colors.CYAN_700,
            )
        )
        doc.controls.append(
            ft.Text("Arial", font_family="Arial", size=20, color=ft.Colors.CYAN_700)
        )
        doc.controls.append(ft.Divider(color=ft.Colors.WHITE_24))
        doc.controls.append(
            ft.Text(
                "Exemples largeur / stretch",
                size=16,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.ORANGE_300,
            )
        )
        doc.controls.append(
            ft.Text(
                "Roboto Condensed = vraie fonte plus etroite",
                font_family="Roboto Condensed",
                size=20,
                color=ft.Colors.LIGHT_GREEN_300,
            )
        )
        doc.controls.append(
            ft.Text(
                "Arial avec letter_spacing negatif (simulation compacte)",
                size=20,
                color=ft.Colors.CYAN_700,
                style=ft.TextStyle(font_family="Arial", letter_spacing=-1.5),
            )
        )
        doc.controls.append(
            ft.Text(
                "Arial avec letter_spacing positif (simulation elargie)",
                size=20,
                color=ft.Colors.CYAN_700,
                style=ft.TextStyle(font_family="Arial", letter_spacing=3),
            )
        )
        doc.controls.append(
            ft.Text(
                "Le letter_spacing change l'espacement, pas la largeur reelle des glyphes.",
                size=14,
                color=ft.Colors.GREY_400,
                italic=True,
            )
        )

        return doc


def _read_env_value(key: str, fallback: str = "No defined") -> str:
    """Récupère la valeur d'une clé dans les variables d'environnement ou dans un fichier .env
    (En cherchant cette key d'abord dans src/.env, puis dans le .env à la racine du projet).
    Args:
        key (str): La clé à rechercher.
        fallback (str, optional): Valeur par défaut si la clé n'est pas trouvée. Defaults to "Not defined".

    Returns:
        str: La valeur de la clé ou la valeur par défaut si la clé n'est pas trouvée.
    """
    value = os.environ.get(key)
    if value is not None:
        return value

    env_candidates = [
        Path(__file__).resolve().parents[1] / ".env",
        Path(__file__).resolve().parents[2] / ".env",
    ]

    for env_path in env_candidates:
        if not env_path.is_file():
            continue

        for raw_line in env_path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue

            env_key, env_value = line.split("=", 1)
            if env_key.strip() == key:
                return env_value.strip().strip("\"'")

    return fallback


class Lv10(ft.Container):  # .env

    def __init__(self):
        super().__init__(
            content=self.myLv10(), width=392, height=1088, bgcolor="#070021"
        )

    def myLv10(self):

        return ft.Text(
            self.ct(), text_align=ft.TextAlign.CENTER, color=ft.Colors.AMBER, size=14
        )

    def ct(self):

        default_env = os.environ.get(
            "FLET_ASSETS_DIR", "No defined"
        )  # → D:\flet_doc\src\assets

        custom_env = _read_env_value("MY_KEY")  # → MY_VALUE_SRC depuis src/.env

        txt = f"#10 {default_env} - {custom_env}"
        print(txt)

        return txt


class Lv11(ft.Container):  # Theming

    def __init__(self, page):
        super().__init__(content=self.myLv11())
        print(page.dark_theme)

        page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)
        # page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.RED_800)
        # page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE_800)
        # print(page.dark_theme)

        page.add(
            # Page theme
            ft.Container(
                content=ft.Button("Page theme button"),
                bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                padding=20,
                width=300,
            ),
            # Inherited theme with primary color overridden
            ft.Container(
                theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.Colors.PINK)),
                content=ft.Button("Inherited theme button"),
                bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                padding=20,
                width=300,
            ),
            # Unique always DARK theme
            ft.Container(
                theme=ft.Theme(color_scheme_seed=ft.Colors.INDIGO),
                theme_mode=ft.ThemeMode.DARK,
                content=ft.Button("Unique theme button"),
                bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                padding=20,
                width=300,
            ),
        )

        page.update()

    def myLv11(self):

        return ft.Text(
            # self.ct(), text_align=ft.TextAlign.CENTER, color=ft.Colors.AMBER, size=14
            self.ct()
        )

    def ct(self):

        txt = "Ready."

        return txt


class Lv12(ft.Container):  # Imperative CRUD

    def __init__(self, page):
        super().__init__(content=self.imperative(page))

    def imperative(self, page):

        from cookbook.crud import imperative

        imperative.main(page)
        page.controls.append(ft.Divider(color=ft.Colors.RED_ACCENT_400))

        return


class Lv13(ft.Container):  # Declarative CRUD (uses page.render)

    def __init__(self, page):
        super().__init__(content=self.declarative(page))

    def declarative(self, page):

        from cookbook.crud import declarative

        declarative.main(page)

        return


class Lv14(ft.Container):  # Minimalist Declarative Counter
    def __init__(self, page):
        super().__init__(content=self.declarative(page))

    def declarative(self, page):

        from cookbook.crud import minimalist

        minimalist.main(page)

        return


class Lv15(ft.Container):  # Drag & Drop

    def __init__(self):
        super().__init__(content=self.dragAndDrop())

    def dragAndDrop(self):
        txt = "Drag & Drop"
        print(txt)
        return self.zones(txt)

    def drag_accept(self, e, rows):
        print("Accepted!")
        # get draggable (source) control by its ID
        src = e.page.get_control(e.src_id)
        # update text inside draggable control
        src.content.content.value = "0"
        # update text inside drag target control
        e.control.content.content.value = "1"
        # reset border
        e.control.content.border = None

        rows.update()

    def drag_will_accept(self, e):
        # DragWillAcceptEvent exposes `accept` as a real bool.
        accepted = e.accept
        e.control.content.border = ft.Border.all(
            5, ft.Colors.GREEN_ACCENT_400 if accepted else ft.Colors.RED_400
        )
        e.control.update()

    def drag_leave(self, e):
        e.control.content.border = None
        e.control.update()

    def zones(self, label: str):

        zones = ft.Row(
            [
                ft.Draggable(
                    group="Number1",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.Colors.CYAN_200,
                        border_radius=5,
                        content=ft.Text("1", color=ft.Colors.BLACK_87, size=24),
                        alignment=ft.Alignment.CENTER,
                    ),
                    content_when_dragging=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.Colors.BLUE_GREY_200,
                        border_radius=5,
                    ),
                    content_feedback=ft.Text("1"),
                ),
                ft.Draggable(
                    group="Number2",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.Colors.AMBER_200,
                        border_radius=5,
                        content=ft.Text("X", color=ft.Colors.BLACK_87, size=24),
                        alignment=ft.Alignment.CENTER,
                    ),
                    content_when_dragging=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.Colors.BLUE_GREY_200,
                        border_radius=5,
                    ),
                    content_feedback=ft.Text("X"),
                ),
                ft.Container(width=100),
                ft.DragTarget(
                    group="Number1",
                    content=ft.Container(
                        width=50,
                        height=50,
                        bgcolor=ft.Colors.PINK_200,
                        border_radius=5,
                        content=ft.Text("0", color=ft.Colors.BLACK_87, size=24),
                        alignment=ft.Alignment.CENTER,
                    ),
                    on_accept=lambda e: self.drag_accept(e, zones),
                    on_will_accept=lambda e: self.drag_will_accept(e),
                    on_leave=lambda e: self.drag_leave(e),
                ),
            ]
        )

        return ft.Container(
            ft.Column(
                height=1000,
                controls=[
                    ft.Text(
                        "Drag & Drop Example",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Divider(color=ft.Colors.LIGHT_GREEN_ACCENT_400, thickness=2),
                    zones,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )


class Lv16(ft.Container):  # Keybord Shortcuts
    def __init__(self, page):
        super().__init__(content=self.essai(page))

    def on_keyboard(self, e: ft.KeyboardEvent, page: ft.Page):
        page.add(
            ft.Text(
                f"Key: {e.key}, Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
            )
        )

    def essai(self, page):

        page.on_keyboard_event = lambda e: self.on_keyboard(e, page)
        page.add(
            ft.Text(
                "Press any key with a combination of CTRL, ALT, SHIFT and META keys..."
            )
        )

        return ft.Text("Ready.")


class Lv17(ft.Container):  # Async
    def __init__(self, page: ft.Page | None = None):
        self.message = ft.Text(
            "Loading...",
            size=24,
            color=ft.Colors.CYAN_ACCENT_200,
            weight=ft.FontWeight.BOLD,
        )
        self._task_started = False
        super().__init__(content=self.message)

    def page_resize(self, page: ft.Page):
        print(f"New page size: {page.window.width} x {page.window.height}")

    def did_mount(self):
        print("Démarrage...")
        if self._task_started:
            print("Task démarrée...")
            return
        print("Task NON démarrée...")
        self._task_started = True
        page = cast(ft.Page, self.page)
        page.run_task(self.main, page)

    async def main(self, page: ft.Page):
        self.page_resize(page)

        async def button_click(e):
            print("Clicked!")
            # await some_async_method()
            page.add(ft.Text("Hello!"))
            await asyncio.sleep(5)  # Delay execution
            page.add(ft.Text("Fait !"))

        page.add(ft.Button("Say hello!", on_click=button_click))

        await asyncio.sleep(5)
        page.on_resize = lambda e: self.page_resize(page)
        self.message.value = "Ready."
        self.message.update()


class Countdown(ft.Text):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds
        self.size = 24
        self.color = ft.Colors.CYAN_ACCENT_200

    def did_mount(self):
        self.running = True
        page = cast(ft.Page, self.page)
        page.run_task(self.update_timer)

    def will_unmount(self):
        self.running = False

    async def update_timer(self):
        while self.seconds + 1 and self.running:
            mins, secs = divmod(self.seconds, 60)
            print(secs)
            self.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            await asyncio.sleep(1)
            self.seconds -= 1


class Lv18(ft.Container):  # Countdown

    def __init__(self):
        self.message = ft.Text(
            "Loading...",
            size=24,
            color=ft.Colors.CYAN_ACCENT_200,
            weight=ft.FontWeight.BOLD,
        )
        self._started = False
        self.countdown_120 = Countdown(30)
        self.countdown_60 = Countdown(20)
        super().__init__(
            content=ft.Column(
                controls=[
                    self.message,
                    ft.Row(
                        controls=[self.countdown_120, self.countdown_60], spacing=20
                    ),
                ]
            )
        )

    def did_mount(self):
        if self._started:
            return
        self._started = True
        self.message.value = "Ready."
        self.message.update()


class Lv19(ft.Container):  # Large Lists
    _MARGES_V = 20

    os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = (
        "8000000"  # Augment WebSocket message in bytes that can be received by Flet Server rendering the page
    )

    def __init__(self):
        super().__init__(
            padding=ft.Padding.only(
                top=68, left=10, right=10, bottom=self._MARGES_V + 10
            ),  # 2ar MARGE_V top & +10 bottom
            height=750,
            bgcolor="#014201",
            border=ft.Border.all(5, ft.Colors.GREEN_200),
            border_radius=ft.BorderRadius.all(7),
            # content=self.build_table(),
            # content=self.list_view(),
            # content=self.grid_view_by_rows(),
            content=self.grid_view(),
        )

    def build_table(self):
        rows = []

        # Max 897 sauf au lancement : 10001+ sinon blocage silencieux
        for i in range(1, 101):
            rows.append(
                ft.Row(
                    spacing=10,
                    controls=[
                        ft.Container(
                            width=40,
                            alignment=ft.alignment.Alignment(-1, 0),
                            content=ft.Text("Line", size=18),
                        ),
                        ft.Container(
                            width=50,
                            alignment=ft.alignment.Alignment(1, 0),
                            content=ft.Text(f"{i}", size=18, font_family="monospace"),
                        ),
                    ],
                )
            )

        return ft.Container(
            expand=True,
            height=700,
            content=ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                spacing=4,
                controls=rows,
            ),
        )

    def list_view(self):
        return ft.ListView(
            scroll=ft.Scrollbar(
                thumb_visibility=True,
                track_visibility=True,
                interactive=True,
                thickness=10,
            ),
            spacing=4,
            controls=[ft.Text(f"Line {i: >5}", size=18) for i in range(1, 101)],
        )

    def grid_view_by_rows(self):
        cases_size = 120  # 54
        # ecartement = 10   # 15
        return ft.Row(
            wrap=True,
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            # spacing=ecartement,
            # run_spacing=ecartement,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    content=ft.Text(
                        f"Item {i}",
                        size=18,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.BLACK_87,
                    ),
                    width=cases_size,
                    height=cases_size,
                    alignment=ft.Alignment.CENTER,
                    bgcolor=ft.Colors.AMBER_100 if i % 2 == 0 else ft.Colors.CYAN_100,
                    border=ft.Border.all(
                        5, ft.Colors.AMBER_400 if i % 2 == 0 else ft.Colors.CYAN_200
                    ),
                    border_radius=7,
                )
                for i in range(1, 121)
            ],
        )

    def grid_view(self):
        return ft.GridView(
            # expand=True,
            max_extent=134,
            child_aspect_ratio=0.99,
            # spacing=20,
            # run_spacing=20,
            padding=ft.Padding.only(left=30, right=30),
            controls=[
                (
                    ft.Container(
                        content=ft.Text(
                            f"Item {i}",
                            size=18,
                            text_align=ft.TextAlign.CENTER,
                            color=ft.Colors.BLACK_87,
                        ),
                        alignment=ft.Alignment.CENTER,
                        bgcolor=(
                            ft.Colors.AMBER_100 if i % 2 == 0 else ft.Colors.CYAN_100
                        ),
                        border=ft.Border.all(
                            5, ft.Colors.AMBER_400 if i % 2 == 0 else ft.Colors.CYAN_200
                        ),
                        border_radius=7,
                    )
                )
                for i in range(1, 121)
            ],
            scroll=ft.ScrollMode.AUTO,
            # scroll=ft.Scrollbar(
            #     thumb_visibility=True,
            #     track_visibility=True,
            #     interactive=True,
            #     thickness=10,
            # ),
        )


class Lv20(ft.Container):  # ELarge list by batch

    def __init__(self):

        super().__init__(
            padding=10,
            expand=True,
            bgcolor="#014201",
            border=ft.Border.all(5, ft.Colors.GREEN_200),
            border_radius=7,
            content=self.simple_batch_loader(),
        )

    def simple_batch_loader(self):

        class BatchList(ft.ListView):
            def __init__(self, total=5001, batch=500):
                super().__init__(expand=True)
                self.total = total
                self.batch = batch

            def did_mount(self):
                for i in range(self.total):
                    self.controls.append(ft.Text(f"Line {i}"))

                    if i % self.batch == 0:
                        print(i)
                        self.update()

                # dernière update
                self.update()

        return BatchList()


class Lv21(ft.Container):  # ELarge list by batch

    def __init__(self):
        self.max_rows = 10000
        self.batch_size = 500
        self.next_row = 1
        self.loading_batch = False
        self.list_view = ft.ListView(
            expand=True,
            spacing=4,
            scroll=ft.Scrollbar(
                thumb_visibility=True,
                track_visibility=True,
                interactive=True,
                thickness=10,
            ),
            build_controls_on_demand=True,
            item_extent=30,
            on_scroll=self.on_list_scroll,
        )
        super().__init__(
            padding=10,
            expand=True,
            bgcolor="#014201",
            border=ft.Border.all(5, ft.Colors.GREEN_200),
            border_radius=7,
            content=self.build_table(),
        )

    def did_mount(self):
        self.append_batch()

    def build_table(self):
        return ft.Container(
            expand=True,
            height=700,
            content=self.list_view,
        )

    def make_row(self, i: int) -> ft.Row:
        return ft.Row(
            spacing=10,
            controls=[
                ft.Container(
                    width=40,
                    alignment=ft.alignment.Alignment(-1, 0),
                    content=ft.Text("Line", size=18),
                ),
                ft.Container(
                    width=50,
                    alignment=ft.alignment.Alignment(1, 0),
                    content=ft.Text(f"{i}", size=18, font_family="monospace"),
                ),
            ],
        )

    def append_batch(self):
        if self.loading_batch or self.next_row > self.max_rows:
            return

        self.loading_batch = True
        start = self.next_row
        stop = min(start + self.batch_size, self.max_rows + 1)
        print(stop)
        self.list_view.controls.extend(self.make_row(i) for i in range(start, stop))
        self.next_row = stop
        self.loading_batch = False
        self.list_view.update()

    def on_list_scroll(self, e: ft.OnScrollEvent):
        if e.extent_after < 300:
            self.append_batch()


class Lv22(
    ft.Container
):  # Large list by batch with background loading and scroll trigger

    def __init__(self):
        self._loading_started = False
        self._loading_batch = False
        self._alive = True
        self.total_rows = 50000
        self.next_row = 0
        self.initial_batch = 300
        self.background_batch = 300
        self.scroll_batch = 1200
        super().__init__(
            padding=10,
            expand=True,
            bgcolor="#014201",
            border=ft.Border.all(5, ft.Colors.GREEN_200),
            border_radius=7,
            height=700,
        )

        # On crée le ListView vide ici
        self.lv = ft.ListView(
            expand=True,
            spacing=4,
            build_controls_on_demand=True,
            item_extent=24,
            scroll=ft.Scrollbar(
                thumb_visibility=True,
                track_visibility=True,
                interactive=True,
                thickness=10,
            ),
            on_scroll=self.on_scroll,
        )
        self.content = self.lv

    def did_mount(self):
        if self._loading_started:
            return
        self._loading_started = True

        # Affiche vite un premier écran de lignes.
        self.append_batch(self.initial_batch)

        page = cast(ft.Page, self.page)
        page.run_task(self.load_items)

    def will_unmount(self):
        self._alive = False

    def append_batch(self, amount: int):
        if self._loading_batch or self.next_row >= self.total_rows:
            return

        self._loading_batch = True
        start = self.next_row
        stop = min(start + amount, self.total_rows)
        self.lv.controls.extend(ft.Text(f"Line {i}") for i in range(start, stop))
        self.next_row = stop
        self._loading_batch = False
        self.lv.update()

    async def load_items(self):
        while self._alive and self.next_row < self.total_rows:
            self.append_batch(self.background_batch)
            await asyncio.sleep(0.02)

    def on_scroll(self, e: ft.OnScrollEvent):
        if e.extent_after < 800:
            self.append_batch(self.scroll_batch)


class Lv23(ft.Container):

    def __init__(self):
        super().__init__()

        self.messages = ft.Column()
        self.user = ft.TextField(hint_text="Your name", width=150)
        self.message = ft.TextField(hint_text="Your message...", expand=True)

        self.content = ft.Column(
            controls=[
                self.sub_title(),
                self.fake_chat(),
            ]
        )

    # ---------------------------------------------------------
    # 1) Appelé automatiquement quand le contrôle est sur la page
    # ---------------------------------------------------------
    def did_mount(self):
        self.page.pubsub.subscribe(self.on_message)

    def sub_title(self):
        return ft.Column(
            controls=[
                ft.Text("Pub/Sub Simple Example", size=18, weight=ft.FontWeight.BOLD),
                ft.Divider(color=ft.Colors.CYAN_ACCENT_400, thickness=2, height=2),
            ]
        )

    def on_message(self, msg):
        self.messages.controls.append(ft.Text(f"Received: {msg}"))
        self.update()

    def send_click(self, e):
        self.page.pubsub.send_all(f"{self.user.value}: {self.message.value}")
        self.message.value = ""
        self.page.update()

    def fake_chat(self):
        send = ft.Button("Send", on_click=self.send_click)

        return ft.Column(
            controls=[
                ft.Text("Fake chat"),
                self.messages,
                ft.Row(controls=[self.user, self.message, send]),
            ]
        )


class Lv24(ft.Column):  # Subprocess Examples

    def __init__(self, txt: str = ""):

        c = controls = [
            ft.Text("Subprocess", size=18),
            ft.Divider(color=ft.Colors.CYAN_ACCENT_400, thickness=2),
            ft.Text(self.myProcess(), size=16, weight=ft.FontWeight.BOLD),
        ]
        if txt:
            controls.append(ft.Text(txt, size=18, color="#eeffffff"))

        super().__init__(c)

    def myProcess(self):
        import subprocess
        import ctypes

        # Codepage OEM utilisé par cmd.exe (ex: cp850 sur Windows FR, cp437 sur EN)
        oem_enc = f"cp{ctypes.windll.kernel32.GetOEMCP()}"
        print(f"OEM encoding: {oem_enc}")

        commands = [
            "echo Bonjour depuis un subprocess en été !",
            "dir",
        ]

        outputs = []
        separator = "─" * 15

        for i, cmd in enumerate(commands, 1):
            p = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
            )
            # IMPORTANT: when shell=True is used, the command must be passed as a single string, not a list.

            # Décodage avec le vrai encodage console (OEM)
            try:
                text = p.stdout.decode(oem_enc, errors="replace")
            except Exception:
                text = p.stdout.decode("cp850", errors="replace")

            outputs.append(f"{separator} Resultat   {i} {separator}\n\n{text}")
        print(outputs)
        return "\n".join(outputs).strip()


class Lv25(ft.Column):  # Routing & Navigation

    def __init__(self, page: ft.Page, txt: str = ""):
        controls = [
            self.route_use(page),
            *([ft.Text(txt, size=18, color="#eeffffff")] if txt else []),
        ]
        super().__init__(controls=controls)

    def route_use(self, page):
        route_log = ft.Column(
            controls=[ft.Text(f"Dans App Lv25 → Initial route : {page.route = }")]
        )

        def lesson_header_controls():
            return [
                ft.Row(
                    controls=[
                        ft.Text(
                            "Routing & Navigation",
                            weight=ft.FontWeight.BOLD,
                            size=18,
                        ),
                        ft.Container(expand=True),
                        ft.Text(
                            "Leçon # 25",
                            size=16,
                            italic=True,
                            color=ft.Colors.CYAN_300,
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Divider(color=ft.Colors.RED_ACCENT_400, thickness=2, height=0),
                ft.Divider(
                    color=ft.Colors.LIGHT_GREEN_ACCENT_400, thickness=2, height=0
                ),
            ]

        async def open_mail_setting(e):
            await page.push_route("/settings/mail")

        async def open_setting(e):
            await page.push_route("/settings")

        def route_change(e):
            print(f"Route change: {page.route}")

            page.views.clear()  # Clear current views
            page.views.append(
                ft.View(
                    route="/",
                    controls=[
                        ft.SafeArea(
                            content=ft.Column(
                                controls=[
                                    *lesson_header_controls(),
                                    ft.AppBar(
                                        title=ft.Text("Flet App"),
                                        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                                        toolbar_height=68,
                                    ),
                                    ft.Button("Go to Settings", on_click=open_setting),
                                ],
                            )
                        )
                    ],
                )
            )
            if page.route == "/settings" or page.route == "/settings/mail":
                page.views.append(
                    ft.View(
                        route="/settings",
                        controls=[
                            ft.SafeArea(
                                content=ft.Column(
                                    controls=[
                                        *lesson_header_controls(),
                                        ft.AppBar(
                                            title=ft.Text("Settings"),
                                            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                                            toolbar_height=68,
                                        ),
                                        ft.Text(
                                            "Settings!",
                                            theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                                        ),
                                        ft.Button(
                                            content="Go to mail settings",
                                            on_click=open_mail_setting,
                                        ),
                                    ]
                                )
                            )
                        ],
                    )
                )
            if page.route == "/settings/mail":
                page.views.append(
                    ft.View(
                        route="/settings/mail",
                        controls=[
                            ft.SafeArea(
                                content=ft.Column(
                                    controls=[
                                        *lesson_header_controls(),
                                        ft.AppBar(
                                            title=ft.Text("Mail Settings"),
                                            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                                            toolbar_height=68,
                                        ),
                                        ft.Text("Mail settings!"),
                                    ]
                                )
                            )
                        ],
                    )
                )
            page.update()

        async def view_pop(e):
            if e.view is not None:
                print("View pop:", e.view)
                page.views.remove(e.view)
                top_view = page.views[-1]
                await page.push_route(top_view.route)

        page.on_route_change = route_change
        page.on_view_pop = view_pop

        route_change(e=None)  # Initialize views based on the initial route

        return route_log


class Lv26(ft.Column):  # Routing & Navigation with separated pages

    def __init__(
        self, page: ft.Page, txt: str = "Page d'accueil au lancement (Uniquement)"
    ):
        super().__init__(
            controls=[
                self.route_use(page),
                *([ft.Text(txt, size=18, color="#eeffffff")] if txt else []),
            ]
        )

    def route_use(self, page):
        route_log = ft.Column(
            controls=[ft.Text(f"Dans App Lv26 → Initial route : {page.route = }")]
        )

        try:
            from cookbook.pages_lv26 import (
                get_page_builders,
            )
        except ImportError:
            from pages_lv26 import (
                get_page_builders,
            )

        build_root_view, build_settings_view, build_mail_settings_view = (
            get_page_builders(lesson=26)
        )

        async def open_setting(e):
            await page.push_route("/settings")

        async def open_mail_setting(e):
            await page.push_route("/settings/mail")

        def route_change(e):
            print(f"Route change: {page.route}")

            page.views.clear()
            page.views.append(build_root_view(open_setting))

            if page.route == "/settings" or page.route == "/settings/mail":
                page.views.append(build_settings_view(open_mail_setting))

            if page.route == "/settings/mail":
                page.views.append(build_mail_settings_view())

            page.update()

        async def view_pop(e):
            if e.view is not None:
                print("View pop:", e.view)
                page.views.remove(e.view)
                top_view = page.views[-1]
                await page.push_route(top_view.route)

        page.on_route_change = route_change
        page.on_view_pop = view_pop

        route_change(e=None)

        return route_log


class Lv27(ft.Column):  # Routing & Navigation with separated pages

    def __init__(
        self, page: ft.Page, txt: str = "Page d'accueil au lancement (Uniquement)"
    ):
        super().__init__(
            controls=[
                self.route_use(page),
                *([ft.Text(txt, size=18, color="#eeffffff")] if txt else []),
            ]
        )

    def route_use(self, page):
        route_log = ft.Column(
            controls=[ft.Text(f"Dans App Lv27 → Initial route : {page.route = }")]
        )

        try:
            from cookbook.pages_lv26 import (
                get_page_builders,
            )
        except ImportError:
            from pages_lv26 import (
                get_page_builders,
            )

        build_root_view, build_settings_view, build_mail_settings_view = (
            get_page_builders(lesson=27)
        )

        async def open_setting(e):
            await page.push_route("/settings")

        async def open_mail_setting(e):
            await page.push_route("/settings/mail")

        async def ask_mail_settings_pop_permission(mail_view: ft.View):
            async def on_dlg_yes(e):
                page.pop_dialog()
                await mail_view.confirm_pop(True)

            async def on_dlg_no(e):
                page.pop_dialog()
                await mail_view.confirm_pop(False)

            dlg_modal = ft.AlertDialog(
                # dlg_modal = ft.CupertinoAlertDialog(
                title=ft.Text("Confirmer le retour"),
                content=ft.Text(
                    "Des modifications dans Mail Settings ne sont peut-être pas encore enregistrées. Quitter cette page ?"
                ),
                actions=[
                    ft.TextButton("Oui", on_click=on_dlg_yes),
                    ft.TextButton("Non", on_click=on_dlg_no),
                ],
                # actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: print("Confirmation de retour fermee."),
            )

            page.show_dialog(dlg_modal)

        def route_change(e):
            print(f"Route change: {page.route}")

            page.views.clear()
            page.views.append(build_root_view(open_setting))

            if page.route == "/settings" or page.route == "/settings/mail":
                page.views.append(build_settings_view(open_mail_setting))

            if page.route == "/settings/mail":
                mail_settings_view = build_mail_settings_view()

                async def confirm_mail_settings_pop(e):
                    await ask_mail_settings_pop_permission(mail_settings_view)

                mail_settings_view.can_pop = False
                mail_settings_view.on_confirm_pop = confirm_mail_settings_pop
                page.views.append(mail_settings_view)

            page.update()

        async def view_pop(e):
            if e.view is not None:
                print("View pop:", e.view)
                page.views.remove(e.view)
                top_view = page.views[-1]
                await page.push_route(top_view.route)

        page.on_route_change = route_change
        page.on_view_pop = view_pop

        route_change(e=None)

        return route_log


class Lv28(ft.Column):  # Routing & Navigation with separated pages

    def __init__(
        self, page: ft.Page, txt: str = "Page d'accueil au lancement (Uniquement)"
    ):
        self.page_ref = page
        self.simple_drawer(page)

        header_controls = [
            ft.Row(
                controls=[
                    ft.Text(
                        "Simple drawer (Menu Burger)",
                        weight=ft.FontWeight.BOLD,
                        size=18,
                    ),
                    ft.Container(expand=True),
                    ft.Text(
                        "Leçon # 28",
                        size=16,
                        italic=True,
                        color=ft.Colors.CYAN_300,
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Divider(color=ft.Colors.RED_ACCENT_400, thickness=2, height=0),
            ft.Divider(color=ft.Colors.LIGHT_GREEN_ACCENT_400, thickness=2, height=0),
        ]

        super().__init__(
            controls=[
                *header_controls,
                self.route_use(page),
                ft.Text(txt or "Drawer configure.", size=18, weight=ft.FontWeight.BOLD),
                ft.FilledButton(
                    "Ouvrir le menu",
                    icon=ft.Icons.MENU,
                    on_click=self.open_drawer,
                ),
            ]
        )

    def route_use(self, page):
        route_log = ft.Column(
            controls=[ft.Text(f"Dans App Lv28 → Initial route : {page.route = }")]
        )

        try:
            from cookbook.pages_lv26 import (
                get_page_builders,
            )
        except ImportError:
            from pages_lv26 import (
                get_page_builders,
            )

        build_root_view, build_settings_view, build_mail_settings_view = (
            get_page_builders(lesson=28)
        )

        return route_log

    async def open_drawer(self, e):
        await self.page_ref.show_drawer()

    def simple_drawer(self, page: ft.Page):
        page.drawer = ft.NavigationDrawer(
            controls=[
                ft.NavigationDrawerDestination(icon=ft.Icons.HOME, label="Home"),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.SETTINGS, label="Settings"
                ),
            ],
            on_change=lambda e: print("Index:", e.control.selected_index),
        )


class Lv29(ft.Column):  # Routing & Navigation with separated pages

    def __init__(
        self, page: ft.Page, txt: str = "Page d'accueil Lv29 (Lancement Uniquement)"
    ):
        header_controls = [
            ft.Row(
                controls=[
                    ft.Text(
                        "Simple drawer + Navigation",
                        weight=ft.FontWeight.BOLD,
                        size=18,
                    ),
                    ft.Container(expand=True),
                    ft.Text(
                        "Leçon # 29",
                        size=16,
                        italic=True,
                        color=ft.Colors.CYAN_300,
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Divider(color=ft.Colors.RED_ACCENT_400, thickness=2, height=0),
            ft.Divider(color=ft.Colors.LIGHT_GREEN_ACCENT_400, thickness=2, height=0),
        ]

        self.status = ft.Text(
            "Aucune selection menu.", size=14, color=ft.Colors.WHITE_70
        )
        self.simple_drawer(page)

        async def open_drawer(e):
            await page.show_drawer()

        super().__init__(
            controls=[
                *header_controls,
                ft.Text(txt or "Drawer configure.", size=18),
                self.status,
                ft.FilledButton(
                    "Ouvrir le menu",
                    icon=ft.Icons.MENU,
                    on_click=open_drawer,
                ),
            ]
        )

    async def on_drawer_change(self, page: ft.Page, e):
        index = e.control.selected_index
        route_map = {
            0: ("Home", "/"),
            1: ("Settings", "/settings"),
        }

        target = route_map.get(index)
        if target is None:
            print(f"[Lv29] Menu clique: index inconnu ({index})")
            self.status.value = f"Selection inconnue: {index}"
        else:
            label, route = target
            print(f"[Lv29] Menu clique: {label} ({index}) -> {route}")
            self.status.value = f"Selection: {label} ({index}) -> {route}"
            await page.push_route(route)

        self.update()

        await page.close_drawer()

    def simple_drawer(self, page: ft.Page):
        page.drawer = ft.NavigationDrawer(
            controls=[
                ft.NavigationDrawerDestination(icon=ft.Icons.HOME, label="Home"),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.SETTINGS, label="Settings"
                ),
            ],
            on_change=lambda e: page.run_task(self.on_drawer_change, page, e),
        )


class Lv30(ft.Column):  # Route templates (parameterized routes)

    def __init__(
        self,
        page: ft.Page,
    ):
        self._mounted = False
        self.route_log = ft.Column(
            controls=[ft.Text(f"Dans App Lv30 → Initial route : {page.route = }")]
        )

        header_controls = [
            ft.Row(
                controls=[
                    ft.Text(
                        "Parameterized routes",
                        weight=ft.FontWeight.BOLD,
                        size=18,
                    ),
                    ft.Container(expand=True),
                    ft.Text(
                        "Leçon #30",
                        size=16,
                        italic=True,
                        color=ft.Colors.CYAN_300,
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Divider(color=ft.Colors.RED_ACCENT_400, thickness=2, height=0),
            ft.Divider(color=ft.Colors.LIGHT_GREEN_ACCENT_400, thickness=2, height=0),
        ]

        async def go_home(e):
            await page.push_route("/")

        async def go_book(e):
            await page.push_route("/books/42")

        async def go_order(e):
            await page.push_route("/account/A-100/orders/O-900")

        async def go_unknown(e):
            await page.push_route("/something/else")

        def route_change(e):
            troute = ft.TemplateRoute(page.route)
            msg_color = ft.Colors.CYAN_500

            if troute.match("/books/:id"):
                msg = f"Book ID: {getattr(troute, 'id', '')}"
            elif troute.match("/account/:account_id/orders/:order_id"):
                msg = (
                    f"Account: {getattr(troute, 'account_id', '')} | "
                    f"Order: {getattr(troute, 'order_id', '')}"
                )
            else:
                msg = "Unknown route"
                msg_color = ft.Colors.RED_400

            print(f"[Lv30] {msg} | route={page.route}")
            self.route_log.controls = [
                ft.Text(f"Dans App Lv30 → Route courante : {page.route}"),
                ft.Text(f"Match: {msg}", color=msg_color),
            ]
            if self._mounted:
                self.update()

        page.on_route_change = route_change
        self._route_change = route_change

        super().__init__(
            controls=[
                *header_controls,
                ft.Text(
                    "Templates tests: /books/:id et /account/:account_id/orders/:order_id",
                    size=14,
                    color=ft.Colors.WHITE_70,
                ),
                self.route_log,
                ft.Row(
                    wrap=True,
                    spacing=8,
                    controls=[
                        ft.OutlinedButton("/", on_click=go_home),
                        ft.OutlinedButton("/books/42", on_click=go_book),
                        ft.OutlinedButton(
                            "/account/A-100/orders/O-900", on_click=go_order
                        ),
                        ft.OutlinedButton("/something/else", on_click=go_unknown),
                    ],
                ),
            ]
        )

        route_change(e=None)

    def did_mount(self):
        self._mounted = True
        self._route_change(e=None)


class Lv31(ft.Column):  # Adaptive apps

    def __init__(self, page: ft.Page, txt: str = "oOo"):
        c = controls = [
            ft.Row(
                controls=[
                    ft.Text("Adaptive apps", weight=ft.FontWeight.BOLD, size=18),
                    ft.Container(expand=True),  # Spacer
                    ft.Text(
                        "Leçon #31", size=16, italic=True, color=ft.Colors.CYAN_300
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Divider(
                color=ft.Colors.CYAN_ACCENT_400, thickness=2, height=2
            ),  # default: height=2}
            ft.Text("─" * int(self.adapt_sample(page) // 8)),
            ft.Divider(color=ft.Colors.WHITE, thickness=2, height=1),
            ft.Text(f"Window width: {self.adapt_sample(page)} px", size=14),
            ft.Divider(color=ft.Colors.CYAN_ACCENT_400, thickness=1),
            ft.CupertinoCheckbox(
                value=True,
                label="CupertinoCheckbox",
            ),
            ft.Checkbox(
                value=True,
                label="Checkbox",
            ),
        ]
        if txt:
            controls.append(ft.Text(txt, size=18, color=ft.Colors.WHITE_70))

        super().__init__(c)

    def adapt_sample(self, page):
        width = page.window.width or page.width or 800
        print(width)
        return width


class Lv32(ft.Column):  # DataTable (sortable)

    def __init__(self, txt: str = "Ready."):
        self.table: ft.DataTable | None = None
        c = controls = [
            ft.Row(
                controls=[
                    ft.Text("DataTable", weight=ft.FontWeight.BOLD, size=18),
                    ft.Container(expand=True),  # Spacer
                    ft.Text(
                        "Leçon #32", size=16, italic=True, color=ft.Colors.CYAN_300
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Divider(color=ft.Colors.CYAN_ACCENT_400, thickness=2, height=2),
            self.myTable(),
        ]
        if txt:
            controls.append(ft.Text(txt, size=18, color=ft.Colors.WHITE))

        super().__init__(c)

    def myTable(self):
        self.table = ft.DataTable(
            columns=[
                ft.DataColumn(label=ft.Text("ID"), numeric=True),
                ft.DataColumn(label=ft.Text("Nom")),
                ft.DataColumn(
                    label=ft.Text("Âge"), numeric=True, on_sort=self.sort_by_age
                ),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("1")),
                        ft.DataCell(ft.Text("Alice")),
                        ft.DataCell(ft.Text("3")),
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("2")),
                        ft.DataCell(ft.Text("Bob")),
                        ft.DataCell(ft.Text("105")),
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("300")),
                        ft.DataCell(ft.Text("Charlie")),
                        ft.DataCell(ft.Text("25")),
                    ]
                ),
            ],
        )

        return self.table

    def sort_by_age(self, e):
        if self.table is None:
            return

        # Flet fournit généralement e.ascending/e.column_index dans l'event de tri.
        ascending = bool(getattr(e, "ascending", True))
        column_index = int(getattr(e, "column_index", 2))

        def age_value(row: ft.DataRow) -> int:
            content = row.cells[2].content
            value = getattr(content, "value", "0")
            return int(str(value))

        self.table.rows.sort(key=age_value, reverse=not ascending)
        self.table.sort_column_index = column_index
        self.table.sort_ascending = ascending
        self.table.update()


if __name__ == "__main__":

    def app_main(page: ft.Page):
        page.add(Lv31(page))

    ft.run(app_main, view=ft.AppView.WEB_BROWSER)
    # ft.run(app_main)
