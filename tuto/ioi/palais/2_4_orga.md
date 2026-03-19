# Organigramme final (simple)

Ce document reflète le flux réel du script `2_4_bth_parity_coins.py` (sans `pymox`, `cls()` et `end()`).

```mermaid
flowchart TD
    %% ----- Sections -----
    subgraph S1["Initialisation"]
        A["Début script"] --> B["__main__"]
        B --> C["Fixer ROWS et COLS"]
        C --> D["main(aff=1)"]
    end

    subgraph S2["Recherche du cycle"]
        E["find_one_cycle_parity(START)"] --> K{"ROWS x COLS pair ?"}
        K -- "Oui" --> L["build_graph"]
        L --> M["DFS avec parité + tri Warnsdorff"]
        M --> N{"DFS succès ?"}
        N -- "Oui" --> O["Construire le tuple du cycle"]
        O --> F{"Cycle trouvé ?"}
        K -- "Non" --> G["Afficher: Aucun cycle"]
        N -- "Non" --> G
        F -- "Non" --> G
        F -- "Oui" --> H["Afficher: Cycle trouvé"]
    end

    subgraph S3["Affichage conditionnel"]
        H --> I{"aff == 1 ?"}
        I -- "Oui" --> J["print_cycle(cycle)"]
        I -- "Non" --> Z["Fin"]
        J --> P["Pour chaque case: direction entrante/sortante"]
        P --> Q{"Case START ?"}
        Q -- "Oui" --> R["Afficher la flèche de sortie"]
        Q -- "Non" --> S["Mapper vers ┌ ┐ └ ┘ ─ │"]
        R --> T["Imprimer la grille"]
        S --> T
    end

    D --> E
    G --> Z
    T --> Z

    %% ----- Styles -----
    classDef io fill:#f3f7ff,stroke:#3c5a99,stroke-width:1.5px,color:#15203b;
    classDef action fill:#eafbf1,stroke:#1f7a46,stroke-width:1.5px,color:#103a22;
    classDef decision fill:#fff4db,stroke:#9c6500,stroke-width:1.5px,color:#4d3200;
    classDef terminal fill:#ffe9ec,stroke:#b4233c,stroke-width:2px,color:#4a0f1a;

    class A,B,C,D,E,H,J,P,R,S,T io;
    class L,M,O action;
    class F,K,N,I,Q decision;
    class G,Z terminal;
```
