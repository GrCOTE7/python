import json
from typing import Any, Optional


def pjson(v: Optional[Any] = None, sortV: bool = False) -> None:
    print(json.dumps(v, indent=2, sort_keys=sortV))
    print()


def msg():
    print()

    voiture = {"marque": "Toyota", "modele": "Yaris", "annee": 2019, "couleur": "rouge"}

    pjson(voiture)

    print(voiture["modele"])
    print(voiture.get("modele"))

    voiture["annee"] = 2025

    pjson(voiture)

    voiture["puissance"] = 100
    voiture["places"] = "7".zfill(3)
    pjson(voiture)

    voiture.pop("places")
    # del voiture["puissance"]
    pjson(voiture)

    # del voiture
    # pjson(voiture) # → UnboundLocalError: cannot access local variable 'voiture' where it is not associated with a value
    # pjson("voiture" in locals() and voiture or "voiture undefined")

    # voiture.clear()
    # pjson(voiture) # → {}

    print()


if __name__ == "__main__":
    msg()
