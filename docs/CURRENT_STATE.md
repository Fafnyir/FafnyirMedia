# Current state — 2026-10-03

User requested moving addon development here, following FafnyirTools with automated GitHub and CurseForge uploads.
Baseline: Desktop/FafnyirMedia_v1.1.0.zip, fingerprinted in docs/baselines/v1.1.0.json. All 28 addon files retain exact bytes. Existing upstream Git history retained; source moved under src/FafnyirMedia.
GitHub already has v1.1.0; migration does not create another release or bump the version.
Release workflow active; CURSEFORGE_API_TOKEN repository secret presence verified on 2026-10-03. Token validity and upload permission will be verified by the first authorized release upload. No in-game validation performed during migration.

Known baseline issue: embeds.xml declares xmlGUIS:xsi rather than xmlns:xsi. Reference checks normalize this declaration in memory; the source remains untouched. In-game XML loading is unverified.

Migration validation: exact baseline check and local package verification passed; GitHub validation run 37139879846 passed for commit e50e733. No new release was published.

Development update: registered the five bundled arrow, combat, and role textures as LibSharedMedia backgrounds; the logo remains unregistered. There are now 15 registrations. Asset bytes and version v1.1.0 remain unchanged, but the edited Lua source no longer matches the original archive baseline. In-game verification remains pending.
