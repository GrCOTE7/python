import sys
from pathlib import Path

tools_path = Path(__file__).parent.parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import cls, exit

if __name__ == "__main__":
    cls("ISC - APPRENDRE L'INFORMATIQUE")
    exit()
    pass

