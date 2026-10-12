"""Synchronise le noyau commun dans chaque skill de la famille cadrage-*.

Source unique (ENF-06) : le dossier `commun/` du dépôt.
- `commun/invariants.md` est injecté dans chaque SKILL.md entre les marqueurs
  `<!-- invariants:debut -->` et `<!-- invariants:fin -->` ;
- `commun/noyau.md` est copié dans `references/noyau.md` de chaque skill ;
- `commun/referentiel-modele.md` est copié dans `assets/referentiel-modele.md`.

Usage :
    python outils/synchroniser.py             # écrit les copies
    python outils/synchroniser.py --verifier  # contrôle seulement ; code 1 si écart
"""

import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
COMMUN = RACINE / "commun"
SKILLS = RACINE / "plugins" / "cadrage-projet" / "skills"

DEBUT = "<!-- invariants:debut -->"
FIN = "<!-- invariants:fin -->"
BLOC = re.compile(re.escape(DEBUT) + r".*?" + re.escape(FIN), re.DOTALL)

MAX_LIGNES_SKILL = 500  # ENF-10
MAX_DESCRIPTION = 1024  # standard Agent Skills
NOM_VALIDE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
CARACTERES_INTERDITS = {"—": "tiret cadratin"}


def lire(chemin: Path) -> str:
    return chemin.read_text(encoding="utf-8")


def ecrire(chemin: Path, contenu: str) -> None:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    chemin.write_text(contenu, encoding="utf-8", newline="\n")


def frontmatter(texte: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", texte, re.DOTALL)
    if not m:
        return {}
    champs = {}
    for ligne in m.group(1).splitlines():
        if ":" in ligne:
            cle, valeur = ligne.split(":", 1)
            champs[cle.strip()] = valeur.strip()
    return champs


def attendu(skill: Path, invariants: str, noyau: str, modele: str) -> dict:
    texte = lire(skill / "SKILL.md")
    if not BLOC.search(texte):
        raise SystemExit(f"Marqueurs d'invariants absents : {skill / 'SKILL.md'}")
    bloc = f"{DEBUT}\n{invariants.strip()}\n{FIN}"
    return {
        skill / "SKILL.md": BLOC.sub(lambda _: bloc, texte),
        skill / "references" / "noyau.md": noyau,
        skill / "assets" / "referentiel-modele.md": modele,
    }


def controles(skill: Path, contenu_skill: str) -> list:
    erreurs = []
    champs = frontmatter(contenu_skill)
    nom = champs.get("name", "")
    description = champs.get("description", "")
    if nom != skill.name:
        erreurs.append(f"{skill.name} : name « {nom} » différent du nom de dossier")
    if not NOM_VALIDE.match(nom) or len(nom) > 64:
        erreurs.append(f"{skill.name} : name invalide")
    if not description:
        erreurs.append(f"{skill.name} : description absente")
    if len(description) > MAX_DESCRIPTION:
        erreurs.append(f"{skill.name} : description de {len(description)} caractères (max {MAX_DESCRIPTION})")
    if "<" in description or ">" in description:
        erreurs.append(f"{skill.name} : chevrons interdits dans la description")
    lignes = contenu_skill.count("\n") + 1
    if lignes > MAX_LIGNES_SKILL:
        erreurs.append(f"{skill.name} : SKILL.md de {lignes} lignes (max {MAX_LIGNES_SKILL})")
    return erreurs


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    verifier = "--verifier" in sys.argv
    invariants = lire(COMMUN / "invariants.md")
    noyau = lire(COMMUN / "noyau.md")
    modele = lire(COMMUN / "referentiel-modele.md")

    skills = sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").is_file())
    if not skills:
        raise SystemExit(f"Aucun skill trouvé dans {SKILLS}")

    ecarts, erreurs = [], []
    for skill in skills:
        fichiers = attendu(skill, invariants, noyau, modele)
        erreurs += controles(skill, fichiers[skill / "SKILL.md"])
        for chemin, contenu in fichiers.items():
            actuel = lire(chemin) if chemin.exists() else None
            if actuel != contenu:
                ecarts.append(chemin.relative_to(RACINE))
                if not verifier:
                    ecrire(chemin, contenu)

    for chemin in sorted(RACINE.rglob("*.md")):
        if ".git" in chemin.parts or "results" in chemin.parts:
            continue
        texte = lire(chemin)
        for car, libelle in CARACTERES_INTERDITS.items():
            if car in texte:
                erreurs.append(f"{chemin.relative_to(RACINE)} : {libelle}")

    for e in erreurs:
        print(f"ERREUR  {e}")
    if verifier:
        for c in ecarts:
            print(f"ÉCART   {c} n'est pas synchronisé avec commun/")
        ok = not ecarts and not erreurs
        print(f"{len(skills)} skills contrôlés : {'conformes' if ok else 'non conformes'}")
        return 0 if ok else 1
    for c in ecarts:
        print(f"ÉCRIT   {c}")
    print(f"{len(skills)} skills synchronisés")
    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
