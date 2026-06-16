# Se placer dans le dossier "tutos"
Set-Location -Path "$PSScriptRoot\src"

# Lancer l'app Flet via uv
uv run --active flet run -r
