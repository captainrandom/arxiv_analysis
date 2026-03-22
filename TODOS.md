# TODOS

## High Priority

### Startup cleanup for __SubgraphTemp labels
**What:** Add `MATCH (p:__SubgraphTemp) REMOVE p:__SubgraphTemp` at startup in `query.py`
**Why:** If query.py crashes between `SET p:__SubgraphTemp` and `REMOVE p:__SubgraphTemp`, stale labels persist and contaminate future GDS projections with wrong nodes. Silent correctness bug.
**How to apply:** Add this Cypher call at the top of `query.py`'s main() before any projection work. One query, ~2ms overhead.
**Depends on:** Nothing — implement when writing query.py

---

## Before Starting Implementation

### Read exploration/explore_open_alex_data.ipynb before writing load_openalex.py
**What:** The notebook likely has OpenAlex parquet field names already mapped out.
**Why:** The parquet schema has fields like `referenced_works` (list of OpenAlex IDs) and `concepts` (embedded array with id, display_name, level, score). Wrong column names in the loader = 2+ hours of debugging.
**How to apply:** Open the notebook, confirm: (1) field name for citations (`referenced_works`? `references`?), (2) structure of the `concepts` array, (3) whether `cited_by_count` is a top-level field.
**Depends on:** Nothing — do this first

---

## Low Priority (polish, non-blocking)

### Handle OSError (disk full) in load_openalex.py
**What:** Add try/except OSError around the Neo4j batch write in load_openalex.py — print a friendly message and exit 1 instead of a raw traceback.
**Why:** Initial bulk load is a multi-hour operation. A disk-full mid-load on a developer laptop produces a confusing Python traceback; a clean message is much easier to act on.
**How to apply:** Wrap `session.run(...)` batch writes in `try/except OSError as e: print(f"[error] Disk full or write error: {e}"); sys.exit(1)`. The checkpoint file means the load is resumable after freeing disk space.
**Depends on:** Nothing — implement when writing load_openalex.py

---

## Post-V1 (after PageRank baseline is validated)

### LeaderRank as PageRank replacement
**What:** Implement LeaderRank on the citation subgraph as an alternative to GDS PageRank.
**Why:** Peer-reviewed finding: LeaderRank (and local variants) outperform PageRank and citation count for identifying expert-selected milestone papers in citation networks.
**How to apply:** GDS supports custom Pregel algorithms. LeaderRank can be implemented as a Pregel procedure. A/B test against PageRank output on the same concept to validate improvement.
**Depends on:** V1 end-to-end working + qualitative validation that PageRank output feels right
