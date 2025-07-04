---
markmap:
  duration: 2100
  initialExpandLevel: -1
---

# Python & Django & Flet (Flutter)
<!-- Effacer toutes les libs de la racine
py -m pip freeze | ForEach-Object { py -m pip uninstall -y $_ } 
-->

## Bases <!-- markmap: fold -->

* [CheatSheet](https://www.cheatsheet.fr/2024/06/05/creer-une-application-android-avec-flet)
→ Utile pour embarquer en APK

[ ] [Série Algos féroces](https://www.youtube.com/watch?v=Njpy0kguSfM&list=PLZZpsVWcTOhEtUyJKPvFuJ53g7bVAZDTy&index=2&ab_channel=ThinhNguyen)

[ ] ∃ [Super outil pour debug](https://pythontutor.com)

[ ] [Snake - 1H](https://www.youtube.com/watch?v=1zVlRXd8f7g)


* Création PUIS Lancement de l'environnement virtuel :

  ```python
  py -m venv env
  PUIS
  .\env\Scripts\activate
    ```

* Installation de Django et Sav des versions des librairies :

  ```python
  pip install django
  pip freeze > requirements.txt
  ```

* Création de l'application :

  ```python
  django-admin startproject merchex
  ```

* Démarrage du serveur :

  ```python
  cd merchex
  py manage.py migrate (La 1ère fois)
  py manage.py runserver
  ```

* Exermples de script :

  ```python
  import os
  # Réinitialiser la console
  os.system("cls" if os.name == "nt" else "clear")
  print()
  a = ["Mary", "had", "a", "little", "lamb"]
  for i in range(len(a)):
      print(i, a[i], end=",")
  print()
  print("-" * 55)
  s = ", ".join(f"{i}: {word}" for i, word in enumerate(a))  # print(i, "word", end=",")
  print(s)
  ```
  
  ```python
  def cheeseshop(kind, *arguments, **keywords):
    <!-- Optional: / for pos or kwd args and * for kwf only args -->
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

  cheeseshop(
    "Limburger",
    "It's very runny, sir.",
    "It's really very, VERY runny, sir.",
    shopkeeper="Michael Palin",
    client="John Cleese",
    sketch="Cheese Shop Sketch",
  )
  ```

* Alignement de texte :
  
  ```python
  print("{0:b}".format(8))
  print(int("1000", 2))
  print("{:,.2f}".format(123456789.456789).replace(",", " "))
  print("-" * 55)

  for i, j in zip(range(1, 11), range(101, 999)):
      print(f"{i:>2} * {j:>3} = {i * j:>4}")
  print("-" * 55)

  for align, text in zip("<^>", [" left ", " center ", " right "]):
      print(
          "{0:{fill}{align}55}".format(
              text, fill="-" if align == "^" else align, align=align
          )
      )
    print("-" * 55)

    width = 7
    print("  Decimal   Hexa    Octal Binary")
    for num in range(5, 13):
        # print("{0: >55}".format(num))
        for base in "dXob":
            print("{0:{width}{base}}".format(num, base=base, width=width), end=" ")
        print()
    print("-" * 55)
    print("-" * 55)
    table = {"Sjoerd": 7, "Jack": 123, "Dcab": 7678}
    for name, phone in table.items():
        print(f"{name:7} ==> {phone:7d}")
    print("-" * 55)

    var = 123.456
    print(f"var={var:.2f}")
    print(f"{var=:.2f}")
    print()
  ```

* Dans un module pour exécution en script, en module ou en CLI :
  
  ```python
  if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        fib(int(sys.argv[1]))
    else:
        fib(50)
  ```

## gsm_app

### Flet (Sur-couche Flutter - Dart)

```python
flet create gsm_app

py -m venv env
pip install flet

pip freeze > requirements.txt
(pip install -r requirements.txt)
```

#### Tutos

* [/] [Priorité LineIndent - Série 64 épisodes](https://www.youtube.com/watch?v=4sHrAZFY08E&list=PLDHA4931gtc4g57ARUkh5AeeSmfdI8WhF)

* [ ] [Quizz - FR](https://www.youtube.com/watch?v=4aiNStwq8oU)

* [ ] [Série Ressource illimitée - Flet-API-APK](https://www.youtube.com/playlist?list=PL8duS-2ZfBKZcxXz0t_4LYtfQM7Qd--je)
  * [x] Last done # 99 (ONLINE or OFFLINE)

* [/] [Flet Tuto](https://www.youtube.com/watch?v=6Tj8_iKqh_k) - Commencé, à reprendre et finir après d'autre tutos de bases de flet

### Resources

* [ ] [Controls](https://flet-controls-gallery.fly.dev/layout)
* [ ] [Icons](https://fonts.google.com/icons)
  * ft.Icons.*NAME*

* [ ] [Community examples](https://github.com/flet-dev/examples/tree/main/python/community)
* [ ] [Contrib](https://github.com/flet-dev/flet-contrib/tree/main/flet_contrib)

### BeeWare

#### BeeWare Base

* [ ] [Doc](https://beeware.org/)

* [ ] [GH](https://github.com/beeware)

* → BriefCase(Py → IOS, Andr, etc...), Toga (GUI), Batavia(JS) et Cricket (Tests suites)
