# --- CLEAN C: INTELLIGENT POUR LIONEL ---

$targets = @(
    "$env:LOCALAPPDATA\uv",
    "$env:LOCALAPPDATA\pip\Cache",
    "$env:LOCALAPPDATA\Python",
    "$env:APPDATA\Code\Cache",
    "$env:APPDATA\Code\CachedData",
    "$env:APPDATA\Code\GPUCache",
    "$env:LOCALAPPDATA\Code\Cache",
    "$env:APPDATA\flet\cache",
    "$env:APPDATA\npm-cache",
    "$env:TEMP",
    "C:\Windows\Temp"
)

Write-Host "Analyse des dossiers lourds..." -ForegroundColor Cyan

foreach ($path in $targets) {
    if (Test-Path $path) {
        $size = (Get-ChildItem -Recurse -Force $path | Measure-Object -Property Length -Sum).Sum
        $sizeGB = [math]::Round($size / 1GB, 2)

        Write-Host "`n$path : $sizeGB Go"

        $choice = Read-Host "Supprimer ce dossier ? (o/n)"
        if ($choice -eq "o") {
            try {
                Remove-Item -Recurse -Force $path
                Write-Host "→ Supprimé" -ForegroundColor Green
            }
            catch {
                Write-Host "→ Impossible de supprimer (droits ou fichiers verrouillés)" -ForegroundColor Yellow
            }
        }
    }
}
