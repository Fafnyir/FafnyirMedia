# Current state — 2026-10-03

User requested moving addon development here, following FafnyirTools with automated GitHub and CurseForge uploads.
Baseline: Desktop/FafnyirMedia_v1.1.0.zip, fingerprinted in docs/baselines/v1.1.0.json. All 28 addon files retain exact bytes. Existing upstream Git history retained; source moved under src/FafnyirMedia.
GitHub already has v1.1.0; migration does not create another release or bump the version.
Release workflow active; CURSEFORGE_API_TOKEN repository secret presence verified on 2026-10-03. Token validity and upload permission confirmed by the successful v1.1.1 upload. No in-game validation performed during migration.

Known baseline issue: embeds.xml declares xmlGUIS:xsi rather than xmlns:xsi. Reference checks normalize this declaration in memory; the source remains untouched. User reported v1.1.1 works in-game without errors on 2026-10-03.

Migration validation: exact baseline check and local package verification passed; GitHub validation run 37139879846 passed for commit e50e733. No new release was published.

Development update: registered the five bundled arrow, combat, and role textures as LibSharedMedia backgrounds; the logo remains unregistered. There are now 15 registrations. Asset bytes remain unchanged, but the edited Lua source no longer matches the original archive baseline.

Release: v1.1.1 final published on 2026-10-03 from commit 05eb40e. GitHub release workflow 37141670865 passed, including CurseForge upload (file 9049781).

In-game verification: user confirmed v1.1.1 works without errors on 2026-10-03. Game client version and individual media checks were not specified.

Release preparation — 2026-10-14: user requested a final release for the 120105 TOC update. Version advanced to v1.1.2; Forever 16001 and all media retained. CurseForge metadata targets 12.1.5 and 1.60.1. Offline checks passed; no new in-game confirmation.
