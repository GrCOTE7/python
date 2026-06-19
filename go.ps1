# Se placer dans le dossier "tutos"
Set-Location -Path "$PSScriptRoot\src"

$env:UV_LINK_MODE = "copy"

# Lancer l'app Flet via uv
uv run --active flet run -r
