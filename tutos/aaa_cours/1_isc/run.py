import subprocess
import os

flet_cli = os.path.abspath(".venv/Scripts/flet.exe")
subprocess.run([flet_cli, "run", "main.py", "-d", "-r"])
