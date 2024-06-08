# Cours OpenClassRooms


## Bases


### Suivis:

https://www.guru99.com/fr/python-tutorials.html

https://openclassrooms.com/fr/courses/7168871-apprenez-les-bases-du-langage-python

https://openclassrooms.com/fr/courses/6951236-mettez-en-place-votre-environnement-python

https://openclassrooms.com/fr/courses/7150616-apprenez-la-programmation-orientee-objet-avec-python

https://openclassrooms.com/fr/courses/5647281-appliquez-le-principe-du-domain-driven-design-a-votre-application

https://openclassrooms.com/fr/courses/7160741-ecrivez-du-code-python-maintenable

### 2do Tutos OCRooms


https://openclassrooms.com/fr/courses/7771531-decouvrez-les-librairies-python-pour-la-data-science


## 2do Zen Python

https://python-guide-fr.readthedocs.io/fr/latest/

https://docs.python.org/fr/3/


---

### Annuaire des packages

https://pypi.org/

```
pip install nom_package

pip uninstall nom_package

pip freeze --local | xargs pip uninstall -y


pip freeze (List installed packages)
pip list

```

### venv

```
 py -m venv env
 
 .\env\Scripts\activate.bat
deactivate
```
NB: Dans Cmder pas besoin du .bat + indique l'environment

### Start tests:

```
pytest tests.py
```

Note: If not exists: 

```
pip install pytest
```
