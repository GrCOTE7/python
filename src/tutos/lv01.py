from flet import *

# * [x] [17/11/2022 **Flet Tutorial Design - Cleaner App** 4 800 **33:59**](https://www.youtube.com/watch?v=xKgFiDSDtXk)


def main(page: Page):
    page.title = "Tutos #01"

    page.bgcolor = "lightblue"

    my_subtitle = Row(
        [
            Icon(Icons.GROUP_OFF, size=15, color="red"),
            Text("1.15 Gb Found", size=15),
        ]
    )

    page.add(
        AppBar(
            leading=IconButton(Icons.ARROW_BACK_IOS),
            title=Text("App Cleaner", weight=FontWeight.BOLD),
            bgcolor="lightblue",
            actions=[
                IconButton(
                    icon=Icons.YOUTUBE_SEARCHED_FOR,
                    icon_color=Colors.BLACK,
                    icon_size=30,
                ),
                IconButton(icon=Icons.STAR_RATE, icon_color=Colors.BLACK, icon_size=30),
            ],
        ),
        # BODY SECTION
        Column(
            [
                Row(
                    [
                        Card(
                            elevation=20,
                            content=Container(
                                # padding=Padding.all(20),
                                padding=20,
                                height=120,
                                width=270,
                                border_radius=BorderRadius.only(
                                    top_left=30, bottom_left=30
                                ),
                                content=Column(
                                    [
                                        Row(
                                            [
                                                Text(
                                                    "1.31 GB",
                                                    size=30,
                                                    weight=FontWeight.BOLD,
                                                )
                                            ],
                                            alignment=MainAxisAlignment.CENTER,
                                        ),
                                        Row(
                                            [
                                                Text(
                                                    "Cleanup Suggested",
                                                    color="#87888A",
                                                    size=12,
                                                    weight=FontWeight.BOLD,
                                                )
                                            ],
                                            alignment=MainAxisAlignment.CENTER,
                                        ),
                                    ],
                                    alignment=MainAxisAlignment.CENTER,
                                ),
                            ),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                # PROGRESSBAR
                Row(
                    [ProgressBar(width=270, value=0.4)],
                    alignment=MainAxisAlignment.CENTER,
                ),
                # ICON INFO
                Row(
                    [
                        Icon(
                            Icons.THUMB_UP,
                            size=20,
                        ),
                        Text(
                            "Used 3.2 Gb",
                            size=15,
                            weight=FontWeight.BOLD,
                        ),
                        Icon(
                            Icons.EMOJI_OBJECTS,
                            size=20,
                        ),
                        Text(
                            "Deleted 31 Gb",
                            size=15,
                            weight=FontWeight.BOLD,
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                # NEW DETAILS
                Column(
                    [
                        Container(
                            padding=20,
                            margin=Margin.symmetric(vertical=30),
                            bgcolor="black",
                            border_radius=BorderRadius.only(
                                top_right=30, bottom_right=30
                            ),
                            content=Text(
                                "can be deleted",
                                size=20,
                                color="white",
                                weight=FontWeight.BOLD,
                            ),
                        ),
                        # STACK CARD
                        Stack(
                            [
                                Card(
                                    elevation=30,
                                    content=Container(
                                        width=page.window.width,
                                        # margin=Margin.only(top=-10),
                                        height=300,
                                        content=Column(
                                            [
                                                ListTile(
                                                    leading=Icon(Icons.ADD_REACTION),
                                                    title=Text(
                                                        "Junk Files",
                                                        size=20,
                                                        weight=FontWeight.BOLD,
                                                    ),
                                                    subtitle=my_subtitle,
                                                ),
                                                ListTile(
                                                    leading=Icon(Icons.ADD_REACTION),
                                                    title=Text(
                                                        "Trash Files",
                                                        color="red",
                                                        size=20,
                                                        weight=FontWeight.BOLD,
                                                    ),
                                                    trailing=Button(
                                                        "Let Cleaned",
                                                        icon=Icons.WHATSHOT,
                                                        color=Colors.GREEN,
                                                        bgcolor="white",
                                                    ),
                                                    subtitle=my_subtitle,
                                                ),
                                                ListTile(
                                                    leading=Icon(Icons.ADD_REACTION),
                                                    title=Text(
                                                        "Slow Performance",
                                                        color="orange",
                                                        size=20,
                                                        weight=FontWeight.BOLD,
                                                    ),
                                                    subtitle=my_subtitle,
                                                ),
                                            ],
                                        ),
                                    ),
                                ),
                                Row(
                                    [
                                        Card(
                                            elevation=20,
                                            content=Container(
                                                margin=Margin.symmetric(vertical=-30),
                                                border_radius=BorderRadius.only(
                                                    bottom_left=30, top_right=30
                                                ),
                                                padding=10,
                                                bgcolor="green",
                                                content=Row(
                                                    [
                                                        Icon(
                                                            icon=Icons.FAVORITE,
                                                            color="pink",
                                                        ),
                                                        Text(
                                                            "Health System",
                                                            size=20,
                                                            weight=FontWeight.BOLD,
                                                            color="white",
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ),
                                    ],
                                    alignment=MainAxisAlignment.END,
                                ),
                            ]
                        ),
                        # END STACK
                    ]
                ),
                # FINAL
                Row(
                    [
                        Container(
                            ink=True,
                            margin=20,
                            padding=Padding.symmetric(horizontal=21, vertical=10),
                            bgcolor="black",
                            border=Border.all(color=Colors.LIGHT_GREEN_400, width=3),
                            border_radius=BorderRadius.all(30),
                            on_click=lambda _: print("Optimize Now!"),
                            content=Row(
                                [
                                    Icon(
                                        Icons.TOUCH_APP,
                                        color=Colors.LIGHT_GREEN_400,
                                        size=30,
                                    ),
                                    Text(
                                        "Optimize Now!",
                                        size=30,
                                        # weight=FontWeight.BOLD,
                                        color=Colors.LIGHT_GREEN_400,
                                    ),
                                ],
                            ),
                        ),
                        TextButton(
                            on_click=lambda _: print("Optimize Now!"),
                            style=ButtonStyle(
                                bgcolor="black",
                                padding=Padding.symmetric(horizontal=21, vertical=10),
                                shape=RoundedRectangleBorder(radius=30),
                                side=BorderSide(3, Colors.LIGHT_GREEN_400),
                                overlay_color=Colors.with_opacity(
                                    0.2, Colors.LIGHT_GREEN_400
                                ),
                            ),
                            content=Row(
                                [
                                    Icon(
                                        Icons.TOUCH_APP,
                                        color=Colors.LIGHT_GREEN_400,
                                        size=30,
                                    ),
                                    Text(
                                        "Optimize Now!",
                                        size=30,
                                        color=Colors.LIGHT_GREEN_400,
                                    ),
                                ],
                                alignment=MainAxisAlignment.CENTER,
                            ),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
            ],
            spacing=0,
        ),
    )


if __name__ == "__main__":
    run(main)
