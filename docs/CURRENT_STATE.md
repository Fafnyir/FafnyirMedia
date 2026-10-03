# Current state — 2026-10-03

User requested moving addon development here, following FafnyirTools with automated GitHub and CurseForge uploads.
Baseline: Desktop/FafnyirMedia_v1.1.0.zip, fingerprinted in docs/baselines/v1.1.0.json. All 28 addon files retain exact bytes. Existing upstream Git history retained; source moved under src/FafnyirMedia.
GitHub already has v1.1.0; migration does not create another release or bump the version.
Release workflow prepared; CurseForge secret must be configured in this repository. No in-game validation performed during migration.

Known baseline issue: embeds.xml declares xmlGUIS:xsi rather than xmlns:xsi. Reference checks normalize this declaration in memory; the source remains untouched. In-game XML loading is unverified.
