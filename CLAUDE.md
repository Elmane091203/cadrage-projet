# CLAUDE.md

Ce dépôt contient la conception du skill `cadrage-projet`. Avant toute action, lire dans cet ordre :

1. `docs/mission.md` : rôle, posture, démarche en 9 phases de construction (texte de référence).
2. `docs/journal-decisions.md` : décisions, hypothèses, questions ouvertes, risques.
3. `docs/specification-v0.2.md` : spécification fonctionnelle en vigueur.

## État du projet

- Phase 2 (spécifications fonctionnelles) : v0.2 consolidée ; clôture à décider par l'utilisateur.
- Prochaine phase : 3, critères d'acceptation et stratégie de tests.
- Aucune implémentation du skill avant la phase 7.

## Règles de travail sur ce dépôt

- Appliquer à ce projet les règles que le skill devra appliquer : distinguer vérifié, déclaré et supposé ; ne jamais présenter une décision provisoire comme validée.
- Une décision n'est validée que par une réponse affirmative explicite de l'utilisateur à une question qui la nomme. Le silence ne vaut pas validation (G1).
- Ne pas rouvrir une décision validée sans élément nouveau. La remplacer par une nouvelle entrée du journal, jamais la réécrire (R4).
- Toute modification de la spécification incrémente sa version et donne lieu à une entrée dans le journal.
- Ne pas passer à la phase suivante si une incertitude critique l'empêche ; sinon, avancer avec des réserves explicites.
- Poser peu de questions, ciblées, qui changent réellement la décision.
- Contredire l'utilisateur quand des éléments sérieux le justifient ; ne pas céder à l'insistance sans argument nouveau.

## Style

- Français professionnel, précis et naturel.
- Aucun tiret cadratin dans les textes produits.

## Repères techniques

- Format cible : standard Agent Skills (`SKILL.md`), publication GitHub en marketplace de plugin Claude Code (D-06, H-01).
- Les campagnes de tests rigoureuses se font dans Claude Code (D-02).
