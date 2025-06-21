import os
import shutil
import subprocess
import sys
from pathlib import Path

# v 0.00.001


def detect_terminal():
    if os.environ.get("TERM_PROGRAM") == "vscode":
        return "vscode"
    elif "WT_SESSION" in os.environ:
        return "windows_terminal"
    else:
        return "classic"


# def relaunch_global_console():
#     script = Path(__file__).resolve()
#     print("🧼 Console saine invoquée... 🚀")

#     subprocess.run([
#     "powershell",
#     "-NoExit",
#     "-Command",
#     f"$env:VIRTUAL_ENV=$null; py \"{script}\""
#     ])

#     sys.exit()

if os.environ.get("VIRTUAL_ENV"):
    print("⛔ Tu es déjà dans un .venv → arrêt par sécurité.")
    sys.exit()
    # relaunch_global_console()


def restore():
    root = Path.cwd()
    venv = root / "venv"
    scripts = venv / ("Scripts" if os.name == "nt" else "bin")
    python = scripts / ("python.exe" if os.name == "nt" else "python")
    pip = scripts / ("pip.exe" if os.name == "nt" else "pip")

    print("🔍 Nettoyage...")
    for folder in ["venv", "__pycache__", "storage"]:
        path = root / folder
        if path.exists():
            print(f"🧹 Suppression de {folder}")
            shutil.rmtree(path, ignore_errors=True)

    print("🐍 Création de venv/...")
    subprocess.run([sys.executable, "-m", "venv", str(venv)], check=True)

    print("⬆️  Mise à jour de pip...")
    subprocess.run(
        [str(python), "-m", "pip", "install", "--upgrade", "pip"], check=True
    )

    if (root / "requirements.txt").exists():
        print("📦 Installation : requirements.txt")
        subprocess.run([str(pip), "install", "-r", "requirements.txt"], check=True)
    else:
        print("📦 Installation par défaut : flet")
        subprocess.run([str(pip), "install", "flet"], check=True)

    print(f"\n✅ Environnement prêt : {venv}")
    if os.name == "nt":
        print("🎯 Pour l’activer ⚡, call : venv\\Scripts\\activate.bat")
    else:
        print("🎯 Pour l’activer : source .venv/bin/activate")


if __name__ == "__main__":

    if os.environ.get("VIRTUAL_ENV"):
        sys.exit(
            "⛔ Le script doit être lancé hors de l’environnement virtuel : 'deactivate' !"
        )

    restore()
