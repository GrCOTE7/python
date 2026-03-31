import flet, sys
from pathlib import Path

tools_path = Path(__file__).parent.parent.parent / "tools"
sys.path.append(str(tools_path))
from tools import *

if __name__ == "__main__":
    cls("*args & **kwargs")

    # *args = Accept any number of positional arguments as tuple
    cls("Example of *args")

    def my_function(*args):
        for arg in args:
            print(arg)

    my_function("Hello", "World", 123, [1, 2, 3], "ok")

    # **kwargs = Accept any number of keyword arguments as dictionary
    cls("Example of **kwargs")

    def plan_party(host_name, **kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    plan_party("Alice", status="single", age=30, city="New York")

    exit()
