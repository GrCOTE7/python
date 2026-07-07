# --- CLEAN C: INTELLIGENT POUR LIONEL ---
[System.Console]::InputEncoding = [System.Text.Encoding]::UTF8
[System.Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "=== Nettoyage intelligent du disque C: ===" -ForegroundColor Cyan

# --- Analyse WinSxS avant nettoyage ---
Write-Host "`nAnalyse du magasin de composants (WinSxS)..." -ForegroundColor Cyan
Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore

# --- Nettoyage WinSxS ---
Write-Host "`nNettoyage des composants Windows (StartComponentCleanup)..." -ForegroundColor Cyan
Dism.exe /Online /Cleanup-Image /StartComponentCleanup

# --- Cibles à nettoyer ---
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

$totalFreed = 0

Write-Host "`nAnalyse des dossiers lourds..." -ForegroundColor Cyan

foreach ($path in $targets) {
    if (Test-Path $path) {

        $size = (Get-ChildItem -Recurse -Force $path | Measure-Object -Property Length -Sum).Sum
        $sizeGB = [math]::Round($size / 1GB, 3)

        Write-Host "`n$path : $sizeGB Go"

        try {
            Remove-Item -Recurse -Force $path
            Write-Host "→ Supprimé" -ForegroundColor Green
            $totalFreed += $size
        }
        catch {
            Write-Host "→ Impossible de supprimer (droits ou fichiers verrouillés)" -ForegroundColor Yellow
        }
    }
}

# --- Résultat final ---
$freedGB = [math]::Round($totalFreed / 1GB, 2)
Write-Host "`n=== Nettoyage terminé ===" -ForegroundColor Cyan
Write-Host "Espace libéré : $freedGB Go" -ForegroundColor Green

# --- Analyse WinSxS après nettoyage ---
Write-Host "`nAnalyse finale du magasin de composants (WinSxS)..." -ForegroundColor Cyan
Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore
