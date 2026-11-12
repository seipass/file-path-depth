from __future__ import annotations
def run(paths):
 from pathlib import PurePath
 return [len(PurePath(p).parts) for p in paths]
