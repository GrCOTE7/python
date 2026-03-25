from flet import *
from custom_checkbox import CustomCheckBox


def main(page: Page):
    BG = "#041955"
    FWG = "#97b4ff"
    FG = "#3450a1"
    PINK = "#eb06ff"

    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route],
        )

    create_task_view = Container(
        content=Container(
            on_click=lambda _: page.go("/"), height=40, width=40, content=Text("x")
        )
        # content=Column(
        #     controls=[
        #         Row(
        #             controls=[
        #                 IconButton(
        #                     icon=Icons.ARROW_BACK,
        #                     icon_color=FG,
        #                     on_click=lambda e: page.go("/"),
        #                 ),
        #                 Text(
        #                     "Create Task",
        #                     size=20,
        #                 ),
        #             ]
        #         ),
        #         TextField(label="Task Name"),
        #         ElevatedButton(text="Add Task"),
        #     ]
        # )
    )

    tasks = Column(
        height=400,
        scroll="auto",
    )
    for i in range(10):
        tasks.controls.append(
            Container(
                height=70,
                width=400,
                bgcolor=BG,
                border_radius=20,
                padding=padding.all(15),  # Padding plus grand pour mieux voir
                content=Row(
                    alignment="start",
                    spacing=15,  # Espacement entre les éléments
                    controls=[
                        # Nouvelle implémentation de CustomCheckBox
                        CustomCheckBox(
                            color="#FF0000",  # Rouge vif
                            stroke_width=4,  # Trait épais
                            size=30,  # Taille plus grande
                        ),
                        Text(f"Tâche {i+1}", color="white", size=16),
                    ],
                ),
            )
        )

    categories_card = Row(alignment="spaceBetween", scroll="auto")

    categories = ["Business", "Familly", "Friends"]
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                border_radius=20,
                bgcolor=BG,
                width=170,
                height=110,
                padding=15,
                # content=Text(category, size=15),
                content=Column(
                    controls=[
                        Text("40 Tasks"),
                        Text(category),
                        Container(
                            width=160,
                            height=5,
                            bgcolor="white12",
                            border_radius=20,
                            padding=padding.only(right=i * 30),
                            content=Container(
                                bgcolor=PINK,
                            ),
                        ),
                    ]
                ),
                on_click=lambda e: print(f"Clicked {category}"),
                tooltip=f"{category}",
                # shadow=shadow.ELEVATION_12,
            )
        )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(
                    alignment="spaceBetween",
                    controls=[
                        Container(content=Icon(Icons.MENU)),
                        Row(
                            controls=[
                                Icon(Icons.SEARCH),
                                Icon(Icons.NOTIFICATIONS_OUTLINED),
                            ]
                        ),
                    ],
                ),
                Container(height=20),
                Text("What's up, Olivia!"),
                Text("CATEGORIES"),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content=categories_card,
                ),
                Container(height=20),
                Text("TODAY'S TASKS"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            bottom=2,
                            right=20,
                            icon=Icons.ADD,
                            on_click=lambda _: page.go("/create_task"),
                        ),
                    ]
                ),
            ]
        )
    )

    page_1 = Container()
    page_2 = Row(
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                padding=padding.only(top=50, left=20, right=20, bottom=5),
                content=Column(controls=[first_page_contents]),
            )
        ]
    )

    container = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        content=Stack(controls=[page_1, page_2]),
    )
    pages = {
        "/": View(
            "/",
            [
                container,
            ],
        ),
        "/create_task": View(
            "/create_task",
            [
                create_task_view,
            ],
        ),
    }

    page.add(container)
    # page.add(create_task_view)

    page.on_route_change = route_change
    page.go(page.route)


app(target=main)
