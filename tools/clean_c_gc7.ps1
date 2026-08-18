# ============================================================
# NETTOYAGE SYSTEMATIQUE MULTI-DISQUES (C:, D:, E:)
# ============================================================

[System.Console]::InputEncoding = [System.Text.Encoding]::UTF8
[System.Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "      NETTOYAGE SYSTÉMATIQUE DES DISQUES C:, D: ET E:" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# ============================================================
# VERIFICATION ADMINISTRATEUR
# ============================================================

$currentIdentity = [Security.Principal.WindowsIdentity]::GetCurrent()
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal($currentIdentity)

$isAdmin = $currentPrincipal.IsInRole(
    [Security.Principal.WindowsBuiltInRole]::Administrator
)

if ($isAdmin) {
    Write-Host "Droits administrateur : OK" -ForegroundColor Green
}
else {
    Write-Host "Droits administrateur : NON" -ForegroundColor Yellow
    Write-Host "Certains éléments système ne pourront pas être nettoyés." -ForegroundColor DarkYellow
}

# ============================================================
# CONFIGURATION
# ============================================================

$drives = @("C:", "D:", "E:")
$userProfile = $env:USERPROFILE

# ============================================================
# COMPTEURS
#
# Structure :
#
# C:
#   Temp
#   Caches
#   __pycache__
#
# D:
#   Temp
#   Caches
#   __pycache__
#
# E:
#   Temp
#   Caches
#   __pycache__
# ============================================================

$categories = @(
    "Temp",
    "Caches",
    "__pycache__"
)

$freedByDrive = @{}

foreach ($drive in $drives) {

    $freedByDrive[$drive] = @{}

    foreach ($category in $categories) {
        $freedByDrive[$drive][$category] = [int64]0
    }
}

# Compteurs séparés pour les opérations dont la taille exacte
# n'est pas directement mesurable.
$recycleBinFreed = [int64]0
$winSxsFreed = [int64]0

# Total réellement mesuré par le script
$totalFreed = [int64]0

# ============================================================
# FONCTION : TAILLE D'UN DOSSIER
# ============================================================

function Get-FolderSize {

    param (
        [string]$Path
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        return [int64]0
    }

    $result = (
        Get-ChildItem `
            -LiteralPath $Path `
            -File `
            -Recurse `
            -Force `
            -ErrorAction SilentlyContinue |
        Measure-Object -Property Length -Sum
    )

    if ($null -eq $result.Sum) {
        return [int64]0
    }

    return [int64]$result.Sum
}

# ============================================================
# FONCTION : ENREGISTRER L'ESPACE LIBÉRÉ
# ============================================================

function Add-FreedSpace {

    param (
        [int64]$Size,
        [string]$Path,
        [string]$Category
    )

    if ($Size -le 0) {
        return
    }

    $script:totalFreed += $Size

    # Déterminer le disque à partir du chemin
    if ($Path -match '^([A-Za-z]):') {

        $drive = "$($Matches[1].ToUpper()):"

        if (
            $script:freedByDrive.ContainsKey($drive) -and
            $script:freedByDrive[$drive].ContainsKey($Category)
        ) {

            $script:freedByDrive[$drive][$Category] += $Size
        }
    }
}

# ============================================================
# FONCTION : NETTOYER LE CONTENU D'UN DOSSIER
# ============================================================

function Clear-FolderContents {

    param (
        [string]$Path,
        [string]$Category
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        return [int64]0
    }

    $freed = [int64]0

    $items = Get-ChildItem `
        -LiteralPath $Path `
        -Force `
        -ErrorAction SilentlyContinue

    foreach ($item in $items) {

        if ($item.PSIsContainer) {
            $sizeBefore = Get-FolderSize $item.FullName
        }
        else {
            $sizeBefore = [int64]$item.Length
        }

        try {

            Remove-Item `
                -LiteralPath $item.FullName `
                -Recurse `
                -Force `
                -ErrorAction Stop

            Add-FreedSpace `
                -Size $sizeBefore `
                -Path $item.FullName `
                -Category $Category

            $freed += $sizeBefore

            Write-Host `
                "  Supprimé : $($item.Name) ($([math]::Round($sizeBefore / 1MB, 2)) Mo)" `
                -ForegroundColor DarkGreen
        }
        catch {

            Write-Host `
                "  Ignoré   : $($item.Name)" `
                -ForegroundColor DarkYellow
        }
    }

    return $freed
}

# ============================================================
# 1. VIDAGE DE LA CORBEILLE
# ============================================================

Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "VIDAGE DE LA CORBEILLE" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

try {

    # Mesure avant suppression.
    # Cette valeur est informative uniquement : Windows ne permet
    # pas toujours de répartir proprement la taille par disque.

    $recycleBefore = [int64]0

    foreach ($drive in $drives) {

        $recyclePath = "${drive}\`$Recycle.Bin"

        if (Test-Path -LiteralPath $recyclePath) {

            $recycleBefore += Get-FolderSize $recyclePath
        }
    }

    Clear-RecycleBin -Force -ErrorAction Stop

    $recycleBinFreed = $recycleBefore

    Write-Host "Corbeille vidée." -ForegroundColor Green

    if ($recycleBefore -gt 0) {

        Write-Host `
            "Taille estimée libérée : $([math]::Round($recycleBefore / 1GB, 3)) Go" `
            -ForegroundColor Green
    }
    else {

        Write-Host "Corbeille déjà vide." -ForegroundColor DarkGray
    }
}
catch {

    Write-Host `
        "Impossible de vider automatiquement la corbeille." `
        -ForegroundColor DarkYellow
}

# ============================================================
# 2. NETTOYAGE WinSxS
# ============================================================

if ($isAdmin) {

    Write-Host "`n============================================================" -ForegroundColor Cyan
    Write-Host "NETTOYAGE DU MAGASIN DE COMPOSANTS (WinSxS)" -ForegroundColor Cyan
    Write-Host "============================================================" -ForegroundColor Cyan

    Write-Host "Lancement de DISM..." -ForegroundColor White

    # DISM ne fournit pas de manière fiable la quantité exacte
    # réellement libérée à notre script.
    #
    # On ne l'intègre donc PAS dans les compteurs de taille.

    Dism.exe /Online /Cleanup-Image /StartComponentCleanup

    Write-Host ""
    Write-Host "Nettoyage WinSxS terminé." -ForegroundColor Green
    Write-Host "Espace libéré par WinSxS : non mesuré précisément." -ForegroundColor DarkGray
}

# ============================================================
# 3. NETTOYAGE DES CACHES
# ============================================================

Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "NETTOYAGE DES CACHES" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

$cacheTargets = @(
    "$userProfile\AppData\Local\pip\Cache",
    "$userProfile\AppData\Roaming\Code\Cache",
    "$userProfile\AppData\Roaming\Code\CachedData",
    "$userProfile\AppData\Roaming\Code\GPUCache",
    "$userProfile\AppData\Local\Code\Cache",
    "$userProfile\AppData\Roaming\flet\cache",
    "$userProfile\AppData\Roaming\npm-cache"
)

foreach ($path in $cacheTargets) {

    if (-not (Test-Path -LiteralPath $path)) {
        continue
    }

    $sizeBefore = Get-FolderSize $path

    if ($sizeBefore -le 0) {
        continue
    }

    Write-Host "`n$path" -ForegroundColor White

    Write-Host `
        "  Taille avant : $([math]::Round($sizeBefore / 1MB, 2)) Mo"

    $freed = Clear-FolderContents `
        -Path $path `
        -Category "Caches"

    Write-Host `
        "  Libéré       : $([math]::Round($freed / 1MB, 2)) Mo" `
        -ForegroundColor Green
}

# ============================================================
# 4. TEMP UTILISATEUR
# ============================================================

Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "NETTOYAGE DU TEMPORAIRES UTILISATEUR" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

$userTemp = "$userProfile\AppData\Local\Temp"

if (Test-Path -LiteralPath $userTemp) {

    $sizeBefore = Get-FolderSize $userTemp

    if ($sizeBefore -gt 0) {

        Write-Host "`n$userTemp" -ForegroundColor White

        Write-Host `
            "  Taille avant : $([math]::Round($sizeBefore / 1MB, 2)) Mo"

        $freed = Clear-FolderContents `
            -Path $userTemp `
            -Category "Temp"

        Write-Host `
            "  Libéré       : $([math]::Round($freed / 1MB, 2)) Mo" `
            -ForegroundColor Green
    }
}

# ============================================================
# 5. TEMP À LA RACINE DES DISQUES
# ============================================================

Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "NETTOYAGE DES TEMP DES DISQUES" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

foreach ($drive in $drives) {

    $tempPath = "${drive}\Temp"

    if (-not (Test-Path -LiteralPath $tempPath)) {
        continue
    }

    $sizeBefore = Get-FolderSize $tempPath

    if ($sizeBefore -le 0) {
        continue
    }

    Write-Host "`n$tempPath" -ForegroundColor White

    Write-Host `
        "  Taille avant : $([math]::Round($sizeBefore / 1MB, 2)) Mo"

    $freed = Clear-FolderContents `
        -Path $tempPath `
        -Category "Temp"

    Write-Host `
        "  Libéré       : $([math]::Round($freed / 1MB, 2)) Mo" `
        -ForegroundColor Green
}

# ============================================================
# 6. WINDOWS TEMP
# ============================================================

if ($isAdmin -and (Test-Path -LiteralPath "C:\Windows\Temp")) {

    Write-Host "`n============================================================" -ForegroundColor Cyan
    Write-Host "NETTOYAGE DE C:\Windows\Temp" -ForegroundColor Cyan
    Write-Host "============================================================" -ForegroundColor Cyan

    $path = "C:\Windows\Temp"

    $sizeBefore = Get-FolderSize $path

    if ($sizeBefore -gt 0) {

        Write-Host ""
        Write-Host $path -ForegroundColor White

        Write-Host `
            "  Taille avant : $([math]::Round($sizeBefore / 1MB, 2)) Mo"

        $freed = Clear-FolderContents `
            -Path $path `
            -Category "Temp"

        Write-Host `
            "  Libéré       : $([math]::Round($freed / 1MB, 2)) Mo" `
            -ForegroundColor Green
    }
}

# ============================================================
# 7. RECHERCHE ET SUPPRESSION DES __pycache__
# ============================================================

Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "SUPPRESSION DES DOSSIERS __pycache__" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

# C:
# Pour éviter une recherche extrêmement longue sur tout Windows,
# on limite C: au profil utilisateur.

$searchLocations = @(
    $userProfile
)

# D: et E:
# Recherche complète sur les disques.

# foreach ($drive in @("C:", "D:", "E:")) {
foreach ($drive in @("C:", "D:")) {

    if (Test-Path -LiteralPath "${drive}\") {
        $searchLocations += "${drive}\"
    }
}

foreach ($location in $searchLocations) {

    Write-Host "`nAnalyse de : $location ..." -ForegroundColor White

    $pyCaches =
    Get-ChildItem `
        -Path $location `
        -Directory `
        -Recurse `
        -Force `
        -ErrorAction SilentlyContinue |
    Where-Object {

        $_.Name -eq "__pycache__" -and
        $_.FullName -notmatch "System Volume Information" -and
        $_.FullName -notmatch "\\`$Recycle\.Bin"
    }

    if ($pyCaches) {

        foreach ($cache in $pyCaches) {

            $cacheSize = Get-FolderSize $cache.FullName

            try {

                Remove-Item `
                    -LiteralPath $cache.FullName `
                    -Recurse `
                    -Force `
                    -ErrorAction Stop

                Add-FreedSpace `
                    -Size $cacheSize `
                    -Path $cache.FullName `
                    -Category "__pycache__"

                # Write-Host `
                #     "  Supprimé : $($cache.FullName) ($([math]::Round($cacheSize / 1MB, 2)) Mo)" `
                #     -ForegroundColor Green
            }
            catch {

                Write-Host `
                    "  Ignoré   : $($cache.FullName)" `
                    -ForegroundColor DarkYellow
            }
        }
    }
    else {

        Write-Host `
            "  Aucun dossier __pycache__ trouvé." `
            -ForegroundColor DarkGray
    }
}

# ============================================================
# 8. BILAN DÉTAILLÉ PAR DISQUE
# ============================================================

Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "BILAN DÉTAILLÉ PAR DISQUE" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

foreach ($drive in $drives) {

    Write-Host ""
    Write-Host $drive -ForegroundColor Yellow

    $driveTotal = [int64]0

    foreach ($category in $categories) {

        $size = $freedByDrive[$drive][$category]

        $driveTotal += $size

        Write-Host `
        ("    {0,-12}: {1,10:N2} Go  ({2,12:N2} Mo)" -f `
                $category,
            ($size / 1GB),
            ($size / 1MB))
    }

    Write-Host `
    ("    {0,-12}  {1,10:N2} Go  ({2,12:N2} Mo)" -f `
            "--------------------------------",
        0,
        0) `
        -ForegroundColor DarkGray

    Write-Host `
    ("    TOTAL {0,-5}: {1,10:N2} Go  ({2,12:N2} Mo)" -f `
            $drive,
        ($driveTotal / 1GB),
        ($driveTotal / 1MB)) `
        -ForegroundColor Green
}

# ============================================================
# 9. BILAN PAR CATÉGORIE
# ============================================================

Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "BILAN PAR CATÉGORIE" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

foreach ($category in $categories) {

    $categoryTotal = [int64]0

    foreach ($drive in $drives) {

        $categoryTotal += $freedByDrive[$drive][$category]
    }

    Write-Host `
    ("{0,-15}: {1,10:N2} Go  ({2,12:N2} Mo)" -f `
            $category,
        ($categoryTotal / 1GB),
        ($categoryTotal / 1MB)) `
        -ForegroundColor Green
}

# ============================================================
# 10. CORBEILLE
# ============================================================

Write-Host ""
Write-Host `
("{0,-15}: {1,10:N2} Go  (estimation)" -f `
        "Corbeille",
    ($recycleBinFreed / 1GB)) `
    -ForegroundColor DarkCyan

# ============================================================
# 11. TOTAL GÉNÉRAL
# ============================================================

Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "TOTAL GÉNÉRAL" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

Write-Host ""

Write-Host `
    "Espace mesuré libéré : $([math]::Round($totalFreed / 1GB, 3)) Go" `
    -ForegroundColor Green

Write-Host `
    "                        $([math]::Round($totalFreed / 1MB, 2)) Mo" `
    -ForegroundColor Green

if ($recycleBinFreed -gt 0) {

    Write-Host ""
    Write-Host `
        "Corbeille (estimation) : $([math]::Round($recycleBinFreed / 1GB, 3)) Go" `
        -ForegroundColor DarkCyan
}

Write-Host ""
Write-Host "WinSxS : nettoyage effectué par DISM." -ForegroundColor DarkGray
Write-Host "        La quantité exacte libérée n'est pas intégrée au total." -ForegroundColor DarkGray

# ============================================================
# FIN
# ============================================================

Write-Host "`n============================================================" -ForegroundColor Cyan
Write-Host "NETTOYAGE GLOBAL TERMINÉ" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "Appuyez sur une touche pour fermer..." -ForegroundColor Cyan

$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")