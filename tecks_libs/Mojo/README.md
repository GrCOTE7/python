# Installation

## 1. Crée l'environement virtuel

```bash
python -m venv .venv
```

## 2. Active l'environement virtuel

* Windows (Note: Mojo ne marche pas sous windows
  ou alors, avec **WSL**)

```bash
.venv/Scripts/activate
```
  
* **Linux**/**MacOSX** (Ou **WSL**):

```bash
source ./.venv/bin/activate
```

## 3. Installe les dépendances

```bash
pip install -r requirements.txt
```

(*requirements.txt* généré par:)
```bash
pip freeze > requirements.txt
```

N.B.: Si **pip** absent:

```bash
python -m pip install --upgrade pip
```

Et si ça ne marche pas:

```bash
py tools/get-pip.py
```

## 4. Exécute le programme si flet

```bash
flet run -r
```

## Divers tips

* Installer un 'vieux' python dans une venv

```bash
virtualenv .venv --python="D:\chemin\vers\python310\python.exe"
```
