from flet import *  # type: ignore[import]

appmenu = AppBar(
    center_title=True,
    leading=IconButton(Icons.MENU, icon_size=30),
    title=Text("Movie `X", size=30, weight=FontWeight.BOLD),
    actions=[IconButton(Icons.SEARCH, icon_size=30)],
)
