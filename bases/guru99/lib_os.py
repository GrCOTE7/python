from os import path

names = ["README.md", "__pycache__", "nothing"]

for name in names:
    print(f"{name} exists: {path.exists(name)}")
    print(f"{name} is a Files: {path.isfile(name)}")
    print(f"{name} is a directory: {path.isdir(name)}\n")
print("-" * 72)

from pathlib import (
    Path,
    PurePath,
    PureWindowsPath,
)  # More recent and others functionalities

p = Path(names[0])
if p.exists():
    print("Le fichier existe")

print("PurePath() = '", PurePath(), "'")
print(PurePath("README.md"))

print(PurePath("dir/dir2/README.md").parts)
print("Name:", PurePath("dir/dir2/README.md").name)
print("Name without suffix:", PurePath("dir/dir2/README.md").stem)
print("Suffix:", PurePath("dir/dir2/README.md").suffix)
print(PurePath("c:/Jeux/ABWFR/Age of Empires HD/").root)
print(PurePath("c:/Jeux/ABWFR/Age of Empires HD/").match("*Empir*"))

file = "c:/foo/bar/setup.py"
pw = PureWindowsPath(file)
print(pw.parents[0])
print(pw.parents[0].anchor)
print(pw.parents[1])
# print(p.parents[1].anchor)
print(pw.parents[2])
print(file, "→", pw.with_stem("changed"))
print(file, "→", pw.with_suffix(".txt"), end="\n\n")

print("Active directory:", Path.cwd())
print("User's home directory:", Path.home())
print(f"File {p.absolute()}'s size:", p.stat().st_size, "\n")

print(f"Files in th current dir:", *sorted(Path(".").glob("**/*.py")))

print("\nFiles in doc/ :")
pdoc = Path("../doc")
for child in pdoc.iterdir():
    print(child.stem, f"({child.suffix})", end="\n")

import time

puuu = Path("uuu.txt")
print(puuu)
if p.is_file():
    puuu.write_text("Hello, world!")
    print(puuu.read_text())
    time.sleep(7)
    if (not Path('uuu.txto').is_file()):
      pooo = puuu.rename("uuu.txto")
    else:
      pooo= Path('uuu.txto')
    time.sleep(7)
    pooo.unlink()  # delete uuu.txt
    print(puuu, pooo)
# puuu.unlink() # delete uuu
