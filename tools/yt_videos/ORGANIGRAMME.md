# Organigramme final (simple)

Ce document reflète le flux réel du code refactoré dans `scrap.py`.

```mermaid
flowchart TD
    A[Début scrap_some] --> B[Init auteur et chemins]
    B --> C[try_return_valid_ttl_cache]
    C --> D{Résumé immédiat disponible ?}
    D -- Oui --> Z[Fin]
    D -- Non --> E[Charger état local: videos ids adults compteurs]

    E --> F[decide_post_ttl_strategy]
    F --> G{Sortie anticipée après probe ?}
    G -- Oui --> Z
    G -- Non --> H[Boucle de collecte]

    H --> I{Complet après au moins 1 fetch ?}
    I -- Oui --> N[Finaliser JSON/Markdown/résumé]
    I -- Non --> J[fetch_playlist_batch]

    J --> K{Mode incrémental actif ?}
    K -- Oui --> L[Scan haut playlist]
    L --> M{7 IDs connus consécutifs ?}
    M -- Oui --> O[Traiter IDs manquants]
    M -- Non --> P[Fallback playlist complète]
    P --> O

    K -- Non --> P
    O --> Q[Évaluer erreurs/pauses/retry]
    Q --> H
    N --> Z
```

## Règles fonctionnelles

1. `try_return_valid_ttl_cache` évite toute requête lourde si le cache TTL est valide et complet.
2. `decide_post_ttl_strategy` décide entre sortie anticipée (dernier ID inchangé) et suite du scraping.
3. `fetch_playlist_batch` encapsule la stratégie incrémentale et son fallback complet.
4. Le mode incrémental ne valide que sur 7 IDs connus consécutifs (`videos` ou `adults`).
5. En cas d'échec du mode incrémental, le fallback complet reste automatique.
6. `resolve_total_playlist_from_batch` centralise le calcul de `total_playlist` + garde-fou de baisse.
7. `remove_stale_adult_ids` nettoie les IDs adults obsolètes de façon dédiée.
8. `handle_no_missing_ids_case` gère explicitement la branche "aucun ID manquant".

## Invariant de lisibilité

1. Une fonction de stratégie = une responsabilité claire.
2. `scrap_some` reste l'orchestrateur, pas l'implémentation détaillée.
3. Chaque bascule de stratégie est explicitement loggée.
