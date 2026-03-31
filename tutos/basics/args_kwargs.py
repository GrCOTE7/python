import flet, sys
from pathlib import Path

tools_path = Path(__file__).parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import *

if __name__ == "__main__":
    cls("*args & **kwargs")
