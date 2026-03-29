from pymox_kit import cls, end
import pyperclip, time

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
project_root_str = str(PROJECT_ROOT)
if project_root_str not in sys.path:
    sys.path.append(project_root_str)

from tools.tools import *

pws_dict = {
    "fb": "fb_123",
    "twit": "tw_123",
    "gm": "gm_123",
    "gh": "gh_123",
}

repeat_forever = True


def get_pw():
    for site in pws_dict:
        print("- " + site)

    site = input("Enter the name of the site to get the password for (or q to quit): ").strip().lower()
    if site in {"q", "quit", "exit"}:
        return "quit"

    pw = pws_dict.get(site)
    if pw is None:
        return "invalid"

    pyperclip.copy(pw)
    print(f"Copying password for {site} to clipboard...")
    return "ok"


def main():
    while True:
        status = get_pw()

        if status == "quit":
            break

        if status == "invalid":
            print("Please enter a valid site name from the list, or q to quit.")
            continue

        get_another_pw = input("Do you want to get another password ? (y/n) : ").strip().lower()
        if get_another_pw != "y":
            break

    print("Exiting the program...")
    return


if __name__ == "__main__":
    cls("Pyperclip for passwords")
    main()
    end()
    exit()
