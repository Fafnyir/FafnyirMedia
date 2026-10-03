# Fafnyir Media

Fonts and textures used by Fafnyir for select UI projects, accessible through LibSharedMedia.

Canonical local repository: `/Users/fpatten/Documents/Codex/FafnyirMedia`.
Active addon source: `src/FafnyirMedia`. The supplied v1.1.0 ZIP is imported without changing addon bytes. Original Git history is preserved.

## Development

Run `python3 tools/check.py`. Use `--baseline` to compare every addon file with the supplied archive fingerprint. After reviewing and committing changes, run `python3 tools/package.py` to build a verified ZIP and SHA-256 manifest in `dist/`. Packages contain only the top-level `FafnyirMedia/` addon folder.

## Releases

In GitHub Actions, run **Build GitHub Release** on the desired revision. Confirm the exact TOC version and choose draft, prerelease, or final. Draft is the default. Draft creates a GitHub release only; prerelease uploads the same ZIP to CurseForge as Beta; final uploads it as Release. Existing version tags are rejected, including the already published v1.1.0.

Configure repository Actions secret `CURSEFORGE_API_TOKEN` with your CurseForge upload token. GitHub authentication uses the workflow token. GitHub secrets cannot be copied out of FafnyirTools; add the token directly to this repository. No secrets belong in source control.

Update `docs/RELEASE-NOTES.txt`, CHANGELOG.md, and the TOC together when a new version is authorized. Review supported game version names in the workflow when updating Interface metadata. Current upload targets are 12.1.0 and 1.60.1, matching the supplied TOC; this does not establish in-game compatibility.

If GitHub publishing succeeds but CurseForge fails, recover the exact ZIP from that GitHub release and upload it to CurseForge; do not rerun the release job and overwrite a tag.

GitHub: https://github.com/Fafnyir/FafnyirMedia
CurseForge: https://www.curseforge.com/wow/addons/fafnyir-media (project 1442918).
