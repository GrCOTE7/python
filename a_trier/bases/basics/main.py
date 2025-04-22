# 2do https://www.youtube.com/results?search_query=tuto+python+en+fran%C3%A7ais

# Solution 1
import sys, os
from pathlib import Path

tools_path = Path(__file__).parent.parent.parent.parent / "tools"
tools_path1 = "c:\\laragon\\www\\PYTHON\\python\\tools"

tools_path3 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tools")

sys.path.append(str(tools_path))

from cls import cls

cls("Script tuto/")

if __name__ == "__main__":

    print("{0: ^55}".format("Path"))
    print()

    width = 8
    print(f"{'File':<{width}}:", str(Path(__file__))[15:])
    print(f"{'Dossier':<{width}}:", str(Path(__file__).resolve().parent)[15:])
    print("-" * 55)
    print("Ready.")
    print()
