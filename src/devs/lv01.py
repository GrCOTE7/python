from flet import *  # type: ignore


def main(page: Page) -> None:
    page.title = "Dev"
    page.add(Text(value="Ready to dev some things !"))


if __name__ == "__main__":

    run(main=main)
