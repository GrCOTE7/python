from fastapi import FastAPI
from flet import app as flet_app, Text, Page

# FastAPI app
api = FastAPI()


@api.get("/")
def read_root():
    return {"message": "Bienvenue depuis FastAPI avec Flet 123 !"}


# Flet UI
def main(page: Page):
    page.title = "Hello Flet"
    t = read_root()
    page.add(Text(str(t['message']) + '\n'+'-'*55 + "\nBienvenue dans l'interface et fenêtre Flet 777 !"))


# Lancer Flet uniquement si exécuté via `flet run`
def run_flet():
    print ('Lancé !')
    flet_app(target=main)


# Point d’entrée pour Flet
if __name__ == "__main__":
    run_flet()

# Alias pour Uvicorn
app = api
