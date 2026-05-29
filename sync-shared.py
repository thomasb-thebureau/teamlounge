#!/usr/bin/env python3
"""
Socle commun The Bureau — synchronisation de la charte partagee.

Copie les fichiers canoniques (theme.css, core.js) du repo Team Lounge
vers le repo Broker Lounge, a l'octet pres, pour eviter toute derive.

Usage : depuis le repo teamlounge :
    python sync-shared.py

Le repo brokerlounge doit etre a cote (../brokerlounge).
"""
import hashlib
import sys
from pathlib import Path

SHARED_FILES = ["theme.css", "core.js"]

HERE = Path(__file__).resolve().parent           # teamlounge (canonique)
BROKER = (HERE.parent / "brokerlounge").resolve()  # ../brokerlounge


def md5(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def main() -> int:
    if not BROKER.is_dir():
        print(f"ERREUR : repo Broker introuvable : {BROKER}")
        return 1

    changed = 0
    for name in SHARED_FILES:
        src = HERE / name
        if not src.is_file():
            print(f"ERREUR : fichier canonique manquant : {src}")
            return 1
        dst = BROKER / name
        if dst.is_file() and md5(dst) == md5(src):
            print(f"  =  {name} deja a jour")
            continue
        dst.write_bytes(src.read_bytes())
        changed += 1
        print(f"  ->  {name} copie vers brokerlounge")

    print(f"\nTermine. {changed} fichier(s) mis a jour.")
    print("Pense a commit/push les deux repos si quelque chose a change.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
