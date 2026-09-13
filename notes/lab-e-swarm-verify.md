# Lab E — swarm × verify summary

**Date:** 2026-09-13  
**Issue:** GTM-359  
**Stamp:** `20260913T174204`  
**Harness:** `.cursor/skills/verify-hermes/scripts/control-hermes`  
**Recipes:** version · doctor · config path/set/get/show (`display.skin=default`)

## Contrast captured

| Forma no recomendada | Forma pstack (este lab) |
|---|---|
| Una sola corrida → “pasó” (anécdota) | 3 homes aislados en paralelo → muestra |
| Un `HERMES_HOME` compartido puede contaminar | Cada worker: `labe-wN-<stamp>` propio |
| Fallo efímero invisible | Cada fallo tendría ruta de evidencia |

## Summary table

| Worker | RUN_ID | Result | Evidence dir |
|---|---|---|---|
| 1 | `labe-w1-20260913T174204` | GREEN | `/tmp/hermes-verify-evidence/labe-w1-20260913T174204/` |
| 2 | `labe-w2-20260913T174204` | GREEN | `/tmp/hermes-verify-evidence/labe-w2-20260913T174204/` |
| 3 | `labe-w3-20260913T174204` | GREEN | `/tmp/hermes-verify-evidence/labe-w3-20260913T174204/` |

**Aggregate:** 3/3 green. Config mutation proven on each worker (`config get display.skin` → `default`). Homes cleaned; evidence kept.

## Notes

- No worktrees. Parallel local shells (swarm sample-size pattern).
- No product code change in this lab — confidence in the lever after Lab D.
