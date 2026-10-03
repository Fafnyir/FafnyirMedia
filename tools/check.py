#!/usr/bin/env python3
"""Validate addon inventory, load references, media assets and optional exact baseline."""
from pathlib import Path
import hashlib,json,re,sys,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
ADDON=ROOT/'src/FafnyirMedia'
def check(baseline=False):
    files={p.relative_to(ADDON).as_posix():p for p in ADDON.rglob('*') if p.is_file()}
    assert files and all(not p.is_symlink() for p in ADDON.rglob('*')), 'Missing addon or unexpected symlink'
    assert all(p.suffix in {'.lua','.toc','.txt','.xml','.tga','.ttf',''} for p in files.values()), 'Unexpected asset type'
    toc=(ADDON/'FafnyirMedia.toc').read_text()
    version=re.search(r'^## Version: (v\d+\.\d+\.\d+)\s*$',toc,re.M)
    assert version, 'Missing semantic version'
    def reference(value,base=ADDON):
        path=base/value.replace('\\','/')
        assert path.resolve().is_relative_to(ADDON.resolve()), f'External load path: {value}'
        assert path.is_file(), f'Missing referenced file: {value}'
        return path
    for line in toc.splitlines():
        if line.strip() and not line.startswith('#'): reference(line.strip())
    for path in ADDON.rglob('*.xml'):
        # Supplied embeds.xml has a legacy namespace declaration typo.
        # Normalize only in memory to validate references without altering the baseline.
        xml=path.read_text().replace('xmlGUIS:xsi=', 'xmlns:xsi=')
        tree=ET.ElementTree(ET.fromstring(xml))
        for node in tree.iter():
            if node.get('file'): reference(node.get('file'),path.parent)
    media=(ADDON/'FafnyirMedia.lua').read_text()
    assets=re.findall(r'\[\[Interface\\Addons\\FafnyirMedia\\([^\]]+)\]\]',media,re.I)
    assert len(assets)==10, 'Review changed media registration inventory'
    for asset in assets: reference(asset)
    assert 'LICENSE' in files and 'fonts/LG - LICENSE.txt' in files, 'Missing licenses'
    if baseline:
        expected=json.loads((ROOT/'docs/baselines/v1.1.0.json').read_text())['files']
        actual={name:hashlib.sha256(path.read_bytes()).hexdigest() for name,path in files.items()}
        assert actual==expected, 'Addon differs from supplied v1.1.0 archive'
    print(f'Passed: {len(files)} addon files, load paths, 10 media references, licenses, version {version.group(1)}'+(' and exact baseline' if baseline else ''))
if __name__=='__main__': check('--baseline' in sys.argv)
