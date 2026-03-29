from pymox_kit import cls, end
import pyperclip

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
project_root_str = str(PROJECT_ROOT)
if project_root_str not in sys.path:
    sys.path.append(project_root_str)

from tools.tools import *

def main():

    str_to_clip = "A string in the clipboard"
    pyperclip.copy(str_to_clip)
    print(" Ok, fait !\n → Do CTRL + V to paste the string in the clipboard wherever you want.")


if __name__ == "__main__":
    cls("Pyperclip")
    main()
    end()
    exit()
