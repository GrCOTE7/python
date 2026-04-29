from flet import * # type: ignore[import] 

def main(page: Page):
    page.title = "Tutos #02"

    page.add(Text("Ready"))


if __name__ == "__main__":

    run(main)
