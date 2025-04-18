# Django

## Tutos

* [/] [debutez-avec-le-framework-django - OCR](https://openclassrooms.com/fr/courses/7172076-debutez-avec-le-framework-django)

* [ ] [Doc](https://docs.djangoproject.com/fr/5.1/)

## Résumé

* Création PUIS Lancement de l'environnement virtuel :

  ```python
  python -m venv env
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
  py manage.py runserver
  ```
