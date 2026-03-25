from email.policy import HTTP
from fastapi import FastAPI, Path, HTTPException
from dataclasses import asdict
from pydantic.dataclasses import dataclass
from typing import Union, List, Optional
import json, math

import flet as ft

# uvicorn main:app --reload

with open("data/pokemons.json", "r") as f:
    pokemons_list = json.load(f)
list_pokemons = {k + 1: v for k, v in enumerate(pokemons_list)}


@dataclass
class Pokemon:
    id: int
    name: str
    types: List[str]
    total: int
    hp: int
    attack: int
    defense: int
    speed: int
    attack_special: int
    defense_special: int
    evolution_id: Optional[int] = None


app = FastAPI()


@app.get("/")
def hello() -> str:
    return "Salut !"


@app.get("/total_pokemons")
def get_total_pokemons() -> dict:
    return {"total": len(pokemons_list)}


@app.get("/pokemons")
def get_all_pokemons() -> list[Pokemon]:
    return [Pokemon(**list_pokemons[id]) for id in list_pokemons]


@app.get("/pokemon/{id}")
def get_pokemon_by_id(id: int = Path(ge=1)) -> Pokemon:
    if id not in list_pokemons:
        raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas")
    return Pokemon(**list_pokemons[id])


@app.post("/pokemon/")
def create_pokemon(pokemon: Pokemon) -> Pokemon:
    if pokemon.id in list_pokemons:
        raise HTTPException(
            status_code=400, detail=f"Le pokemon {pokemon.id} existe déjà"
        )
    list_pokemons[pokemon.id] = asdict(pokemon)
    return pokemon


@app.put("/pokemon/{id}")
def update_pokemon(pokemon: Pokemon, id: int = Path(ge=1)) -> Pokemon:
    if id not in list_pokemons:
        raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas")

    list_pokemons[id] = asdict(pokemon)
    return pokemon


@app.delete("/pokemon/{id}")
def delete_pokemon(id: int = Path(ge=1)) -> Pokemon:
    if id in list_pokemons:
        pokemon = Pokemon(**list_pokemons[id])
        del list_pokemons[id]
        return pokemon

    raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas")


@app.get("/types")
def get_all_types() -> list[str]:
    types = []
    for pokemon in pokemons_list:
        for t in pokemon["types"]:
            if t not in types:
                types.append(t)
    types.sort()
    return types


@app.get("/pokemons/search/")
def search_pokemons(
    types: Union[str, None] = None,
    evo: Union[str, None] = None,
    totalgt: Union[int, None] = None,
    totallt: Union[int, None] = None,
    sortby: Union[str, None] = None,
    order: Union[str, None] = None,
) -> Union[list[Pokemon], None]:

    filtered_list = []
    res = []

    # On filtre les types
    if types is not None:
        for pokemon in pokemons_list:
            if set(types.split(",")).issubset(pokemon["types"]):
                filtered_list.append(pokemon)

    # On filtre les evolutions
    if evo is not None:
        tmp = filtered_list if filtered_list else pokemons_list
        new = []

        for pokemon in tmp:
            if evo == "true" and "evolution_id" in pokemon:
                new.append(pokemon)
            if evo == "false" and "evolution_id" not in pokemon:
                new.append(pokemon)

        filtered_list = new

    # On filtre sur greater than total
    if totalgt is not None:
        tmp = filtered_list if filtered_list else pokemons_list
        new = []

        for pokemon in tmp:
            if pokemon["total"] > totalgt:
                new.append(pokemon)

        filtered_list = new

    # On filtre sur less than total
    if totallt is not None:
        tmp = filtered_list if filtered_list else pokemons_list
        new = []

        for pokemon in tmp:
            if pokemon["total"] < totallt:
                new.append(pokemon)

        filtered_list = new

    # On gére le tri
    if sortby is not None and sortby in ["id", "name", "total"]:
        filtered_list = filtered_list if filtered_list else pokemons_list
        sorting_order = False
        if order == "asc":
            sorting_order = False
        if order == "desc":
            sorting_order = True

        filtered_list = sorted(
            filtered_list, key=lambda d: d[sortby], reverse=sorting_order
        )

    # Réponse
    if filtered_list:
        for pokemon in filtered_list:
            res.append(Pokemon(**pokemon))
        return res

    raise HTTPException(
        status_code=404, detail="Aucun Pokemon ne répond aux critères de recherche"
    )


# =====Tous les Pokémons avec la pagination=====
@app.get("/pokemons2/")
def get_all_pokemons(page: int = 1, items: int = 10) -> list[Pokemon]:

    items = min(items, 20)
    max_page = math.ceil(len(list_pokemons) / items)
    current_page = min(page, max_page)
    start = (current_page - 1) * items
    stop = start + items if start + items <= len(list_pokemons) else len(list_pokemons)
    sublist = (list(list_pokemons))[start:stop]

    res = []

    for id in sublist:
        res.append(Pokemon(**list_pokemons[id]))

    return res


if __name__ == "__main__":
    poks = get_all_pokemons()

    print("─" * 9, "\b→", len(poks))

    for i in range(150, 150):
        print(i, (poks[i].attack_special, poks[i].defense_special))
