# 2do https://www.youtube.com/results?search_query=tuto+python+en+fran%C3%A7ais

# Solution 1
import sys

# Solution 1
tools_path1 = "c:\\laragon\\www\\PYTHON\\python\\tools"
# sys.path.append("c:\\laragon\\www\\PYTHON\\python\\tools")
print(f"{sys.path}")
# quit()

# Solution 2 - La + performante (Path + légers eet rapides que str)
from pathlib import Path

tools_path2 = Path(__file__).parent.parent.parent.parent / "tools"

# Solution 3
import os, time

tools_path3 = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
    "tools",
)

sys.path.append(str(tools_path1))  # Choix du path

from tools import cls

cls("Pathes/")

if __name__ == "__main__":
    time.sleep(1)
    print("\033[1;36;40m", end="\r")  # Remonte d'une ligne
    print("{0: >55}".format("Chemins de base :"))
    print("\033[0;37;40m")

    mea = "\033[1;33;40m"  # Mise En Avant
    normal = "\033[0;37;40m"
    # 0 : noir - 1 : rouge - 2 : vert - 3 : jaune - 4 : bleu - 5 : magenta - 6 : cyan - 7 : blanc
    # 3x pour encre, 4x pour fond

    widthHead = 8
    widthTxt = 22
    print(f"{'File':<{widthHead}}:", str(Path(__file__))[widthTxt:])
    print(f"{'Dossier':<{widthHead}}:", str(Path(__file__).resolve().parent)[widthTxt:])
    time.sleep(1)
    print("-" * 55)
    print(
        f"1 - Absolu :\n{' '*4}tools_path1 = {mea}\"c:\\laragon\\www\\PYTHON\\python\\tools\"{normal}\n{' '*2}→ tools_path1 = {tools_path1[widthTxt:]}"
    )
    print("-" * 55)
    time.sleep(1)
    print(
        f"2 - Relatif :\n{' '*4}tools_path2 = {mea}Path(__file__).parent.parent.parent.parent / \"tools\"{normal}\n{' '*2}→ tools_path2 = {str(tools_path2)[widthTxt:]}"
    )
    print("-" * 55)
    time.sleep(1)
    print(
        f"3 - Relatif (Avec os) :\n{' '*4}tools_path3 = {mea}os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),\"tools\",){normal}\n{' '*2}→ tools_path3 = {str(tools_path3)[widthTxt:]}"
    )
    print(f"\n{os.path.dirname(__file__) = }")
    print("-" * 55)
    time.sleep(1)
    s = "Code retrait du chariot"
    print(f"{s} → {s.replace('du', '\b')}: \033[1;33;40m\\b\033[0;37;40m")
    print("-" * 55)
    time.sleep(1)
    print(f"{sys.path=}")
    print()
