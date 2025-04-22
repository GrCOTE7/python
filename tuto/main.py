# Solution 1
import sys

# Solution 1
# sys.path.append("c:\\laragon\\www\\PYTHON\\python\\tools")
# print(sys.path)
# quit()

# Solution 2
from pathlib import Path

tools_path = Path(__file__).parent.parent / "tools"

# Solution 3
import os

tools_path2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tools")
sys.path.append(str(tools_path2))

from cls import cls

cls("Script tuto/")

if __name__ == "__main__":

    print("{0: ^55}".format("x"))
    print()

    print(f"{tools_path = }")
    print(f"{tools_path2 = }")
    print()
