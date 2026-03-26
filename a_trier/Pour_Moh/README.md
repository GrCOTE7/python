# Installation

## 1. Crée l'environement virtuel

```bash
python -m venv .venv
```

## 2. Active l'environement virtuel

* Windows :

```bash
.venv/Scripts/activate
```
  
* Linux/MacOSX :

```bash
source ./.venv/bin/activate
```

## 3. Installe les dépendances

```bash
pip install -r requirements.txt
```

N.B.: Si **pip** absent:

```bash
python -m pip install --upgrade pip
```

Et si ça ne marche pas:

```bash
py tools/get-pip.py
```

## 4. Exécute le programme

```bash
flet run -r
```
