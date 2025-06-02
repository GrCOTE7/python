# Python & Django

## Bases

[ ] [Série Algos féroces](https://www.youtube.com/watch?v=Njpy0kguSfM&list=PLZZpsVWcTOhEtUyJKPvFuJ53g7bVAZDTy&index=2&ab_channel=ThinhNguyen)

[Super outil pour debug](https://pythontutor.com)

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
