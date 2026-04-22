from datetime import date, datetime, timedelta as datedelta
from os import name

if __name__ == "__main__":

    # Obtenir la date actuelle
    today = date.today()
    print("Date actuelle:", today)

    # Obtenir la date et l'heure actuelles
    now = datetime.now()
    print("Date et heure actuelles:", now)

    # Créer une date spécifique
    specific_date = date(2026, 2, 28)
    print("Date spécifique:", specific_date)

    date2 = date(2026, 3, 2)

    # Calculer la différence entre deux dates
    delta = date2 - specific_date
    print("Différence en jours:", delta.days)

    # Ajouter des jours à une date
    future_date = today + datedelta(days=30)
    print("Date dans 30 jours:", future_date)

    # date du jour en toutes lettres
    print("Date du jour en toutes lettres:", today.strftime("%A %d %B %Y"))
    print("Date du jour en chiffres:", today.strftime("%d/%m/%Y"))

    txt = "01/07/2026"
    date_from_txth = datetime.strptime(txt, "%d/%m/%Y")
    date_from_txt = date_from_txth.date()
    print("Date à partir du texte:", date_from_txth, "-", date_from_txt)
