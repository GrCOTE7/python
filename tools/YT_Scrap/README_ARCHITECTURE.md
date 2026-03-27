# Architecture du scraper yt_videos

## Objectif

Le pipeline privilegie les chemins rapides (TTL/probe), puis degrade proprement vers un scan plus complet uniquement quand necessaire.

## Flux reel (niveau service)

1. Entree CLI
- `main.py` parse `--selection`.
- Par defaut, la selection vient de `build_bpl.get_default_target_scrape_ids()`.
- Le flux lance `run_scrap(selection)`.

2. Orchestration par auteur
- `inc/runner.py` valide les IDs puis appelle `run_selected_authors`.
- `inc/manager.py:scrap_some` pilote tout le cycle auteur.

3. Initialisation et hygiene cache
- `init_ops.build_init_context` charge chemins + constantes runtime.
- `cache.bootstrap_missing_cache_from_legacy` restaure un JSON legacy si besoin.
- `cache.auto_heal_cache_invariants` corrige les invariants de structure.

4. Decision TTL
- `ttl_ops.try_return_valid_ttl_cache` accepte uniquement un cache valide et complet.
- Si hit TTL: sortie immediate (avec regeneration Markdown seulement si absent).

5. Strategie post-TTL
- `ttl_ops.decide_post_ttl_strategy` fait un probe leger du dernier ID publie.
- Si ID inchange: refresh cache + sortie anticipee.
- Sinon: activation du mode incremental (ou flux normal si probe non concluant).

6. Boucle de scraping
- `flow_ops.fetch_playlist_batch`: incremental d'abord, fallback full si signal insuffisant.
- `flow_ops.resolve_total_playlist_from_batch`: garde-fou de baisse sur `total_playlist`.
- `flow_ops.extract_playlist_ids` puis dedup stable.
- `flow_ops.remove_stale_excluded_ids` retire les exclus obsoletes.
- Si trous detectes: `detail_ops.process_missing_entries_detailed` enrichit les manquants.
- Si pas de trous: `flow_ops.handle_no_missing_ids_case` ajuste l'etat partiel/complet.

7. Erreurs, pause, reprise
- Les erreurs 403/rate-limit sont cumulees (`CountedErrorTracker`).
- En seuil atteint: persistance intermediaire via `persist_ops.persist_intermediate_state` puis pause/reprise.
- Un controle de stall stoppe apres plusieurs passes sans progression.

8. Finalisation auteur
- `persist_ops.finalize_scrap_state` ecrit JSON final + Markdown conditionnel + resume.
- Sync tracking sqlite via `_sync_tracking_after_scrap` (si module `suivi` disponible).

9. Post-run global
- `main.py` importe les etats de `BPL.md` vers tracking (`import_states_into_tracking`).
- `main.py` regenere `BPL.md` (`build_bpl`).

## Fonctions et noms canoniques

- `try_return_valid_ttl_cache`
- `decide_post_ttl_strategy`
- `fetch_playlist_batch`
- `resolve_total_playlist_from_batch`
- `remove_stale_excluded_ids`
- `handle_no_missing_ids_case`
- `process_missing_entries_detailed`
- `persist_intermediate_state`
- `finalize_scrap_state`

Note: le nom correct est `remove_stale_excluded_ids` (et non `remove_stale_adult_ids`).

## Scenarios principaux

### 1) TTL hit

Condition:
- Cache TTL valide, marque `cache_valid`, et complet.

Chemin:
1. `try_return_valid_ttl_cache` valide le cache.
2. Sortie immediate sans playlist full.

Effet:
- Execution la plus rapide.
- Markdown regenere seulement si absent.

### 2) Probe hit

Condition:
- Cache TTL expire mais cache precedent complet.
- Probe: dernier ID publie == dernier ID cache en tete.

Chemin:
1. `decide_post_ttl_strategy` lance le probe.
2. Si ID identique: refresh metadata cache + sortie anticipee.

Effet:
- Pas de pagination massive.
- Pas de detail sur tous les manquants.

### 3) Incremental puis fallback full

Condition:
- Cache expire et changement detecte, ou probe non concluant.

Chemin:
1. `fetch_playlist_batch` tente un scan incremental du haut de playlist.
2. Si streak d'IDs connus suffisant: traitement des manquants seulement.
3. Sinon: bascule automatique en scan complet.
4. `process_missing_entries_detailed` enrichit les videos manquantes.

Effet:
- Cout reseau reduit quand la derive est faible.
- Robustesse preservee grace au fallback complet.

## Invariants de conception

1. L'orchestrateur reste unique (`scrap_some`) et delegue aux modules `ops`.
2. Les videos indisponibles/private ne sont pas comptees comme adult.
3. `excluded_count >= len(excluded_ids)` est maintenu avant ecriture JSON.
4. Toute bascule de strategie est journalisee (TTL/probe/incremental/fallback/pause).
5. Le fallback full reste disponible pour garantir la completude metier.
