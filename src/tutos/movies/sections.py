from flet import *  # type: ignore[import]
import json
from pathlib import Path

################# SECTION 1 #################
################ COMING SOON ################

base_url = "https://image.tmdb.org/t/p/original"
allmovies = Row(scroll=ScrollMode.AUTO)

s = []

json_path = Path(__file__).with_name("coming_soon.json")
with json_path.open("r", encoding="utf-8") as json_file:
    data = json.load(json_file)
    s = data["results"]

for x in s:
    allmovies.controls.append(
        Card(
            elevation=20,
            width=160,
            height=330,
            bgcolor="white",
            content=Container(
                padding=Padding.all(10),
                content=Column(
                    [
                        Image(
                            src=base_url + x["poster_path"],
                            # width=150,
                            height=200,
                            border_radius=BorderRadius.all(20),
                            # fit=BoxFit.COVER,
                            fit=BoxFit.CONTAIN,
                        ),
                        Text(
                            x["original_title"],
                            size=18,
                            weight=FontWeight.BOLD,
                            text_align=TextAlign.CENTER,
                            color="black",
                        ),
                        Text(x["release_date"], size=12, color="black"),
                    ],
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                ),
            ),
        )
    )

################# SECTION 2 #################
################ A FILM (af) ################

json_path = Path(__file__).with_name("data.json")
with json_path.open("r", encoding="utf-8") as json_file:
    data = json.load(json_file)
    s = data["title"]
    
af= Text(f'A film: {s}')

################# AFFICHAGE #################

section1 = Column(
    [
        Text("Trending", size=20, weight=FontWeight.BOLD),
        allmovies,
        af
    ]
)
