# Architecture du scraper yt_videos

## Objectif

Le script privilégie les chemins rapides, puis dégrade proprement vers un scan plus complet uniquement quand nécessaire.

## Composants clés

1. Orchestration
- scrap_some: pilote le flux global.

2. Décision cache et stratégie
- try_return_valid_ttl_cache: retour immédiat si cache TTL valide et complet.
- decide_post_ttl_strategy: décide sortie anticipée après probe ou poursuite.
- fetch_playlist_batch: choisit incrémental ou complet, avec fallback.

3. Traitement des résultats playlist
- resolve_total_playlist_from_batch: met à jour total_playlist avec garde-fou de baisse.
- remove_stale_adult_ids: nettoie les IDs adults obsolètes.
- handle_no_missing_ids_case: gère le cas sans IDs manquants.
- process_missing_entries_detailed: traite les détails yt-dlp pour les vidéos manquantes.

## Scénarios principaux

### 1) Cache hit

Condition:
- Cache TTL valide et cache complet.

Chemin:
1. try_return_valid_ttl_cache valide le cache.
2. Retour immédiat sans requête lourde.

Effet:
- Exécution la plus rapide.
- Markdown régénéré uniquement si absent.

### 2) Probe hit

Condition:
- Cache TTL expiré, mais cache précédent complet.
- Probe ultra-léger: dernier ID publié identique au premier ID du cache.

Chemin:
1. decide_post_ttl_strategy lance le probe.
2. Si ID identique: refresh du cache + sortie anticipée.

Effet:
- Pas de pagination massive.
- Pas de scraping détaillé.

### 3) Incrémental puis fallback

Condition:
- Cache expiré et dernier ID changé, ou probe non concluant.

Chemin:
1. fetch_playlist_batch tente un scan incrémental du haut de playlist.
2. Si 7 IDs connus consécutifs sont trouvés: traitement des manquants uniquement.
3. Sinon: fallback automatique en scan complet.
4. process_missing_entries_detailed enrichit les vidéos manquantes.

Effet:
- Coût réseau limité quand la dérive est faible.
- Robustesse conservée grâce au fallback complet.

## Invariants de conception

1. Un seul orchestrateur, plusieurs fonctions spécialisées.
2. Toute décision de stratégie est explicite dans les logs.
3. Le fallback complet reste disponible pour garantir la complétude.
