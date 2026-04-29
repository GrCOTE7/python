from flet import *  # type: ignore[import]

# * [x] [19/11/2022 **Flet tutorial design - Movie App Design** 7 302 **18:48**](https://www.youtube.com/watch?v=vsMBD_QXuDg)

try:
    from .appmenu import appmenu
    from .sections import section1
except ImportError:
    from src.tutos.movies.sections import section1
    from appmenu import appmenu


def main(page: Page):
    page.title = "Tutos #02"
    page.appbar = appmenu

    # page.add(Text("Ready to watch a movie?"))
    page.add(section1)


if __name__ == "__main__":

    run(main)
