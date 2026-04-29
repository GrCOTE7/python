from flet import * #type: ignore


def main(page: Page):
    page.title = "Dev"
    page.add(Text("Ready to dev some things !"))


if __name__ == "__main__":

    run(main)
