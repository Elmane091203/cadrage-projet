# cadrage-projet

Skill d'IA qui accompagne la clarification, le cadrage, la conception et la planification de projets. Il distingue ce qui est établi de ce qui est supposé, contredit quand c'est justifié et laisse à l'utilisateur la maîtrise des décisions.

> **Statut : version 0.1.0, provisoire.** Implémentée sur la base de la spécification v0.3. Une première campagne d'évaluation a été jouée ; les scénarios multi-tours restent à outiller. Voir `docs/journal-decisions.md` et `docs/tracabilite-v0.1.md`.

## Installation (Claude Code)

```
/plugin marketplace add Elmane091203/cadrage-projet
/plugin install cadrage-projet@cadrage-projet
```

Les skills sont au standard Agent Skills : chaque dossier de `plugins/cadrage-projet/skills/` est autonome et peut être installé seul dans un autre environnement compatible (par exemple en téléversant le dossier zippé sur claude.ai). Le fonctionnement hors de Claude Code n'est pas encore testé.

## Skills

| Skill | Rôle |
|---|---|
| `cadrage-projet` | Point d'entrée et orchestrateur : détection de la demande, intensité, clarification, diagnostic, cadrage, parcours et référentiel |
| `cadrage-audit` | Audit d'un existant : cahier des charges, projet engagé, solution, dossier d'appel d'offres |
| `cadrage-solutions` | Exploration et comparaison de solutions |
| `cadrage-exigences` | Exigences, règles métier et critères d'acceptation |
| `cadrage-faisabilite` | Faisabilité, risques et conformité |
| `cadrage-planification` | Planification de la réalisation, ou d'investigation |

## Contenu du dépôt

| Chemin | Rôle |
|---|---|
| `docs/mission.md` | Mission et démarche de conception |
| `docs/specification-v0.3.md` | Spécification fonctionnelle en vigueur |
| `docs/journal-decisions.md` | Décisions, hypothèses, questions ouvertes, risques |
| `docs/tracabilite-v0.1.md` | Correspondance exigences, implémentation et tests ; résultats de campagne |
| `commun/` | Source unique du noyau, recopiée dans chaque skill |
| `outils/synchroniser.py` | Recopie et contrôle du noyau dans les skills |
| `plugins/cadrage-projet/` | Plugin publié : skills et évaluations |
| `.claude-plugin/marketplace.json` | Marketplace Claude Code |

## Maintenance

1. Modifier le noyau uniquement dans `commun/`, jamais dans les copies.
2. `python outils/synchroniser.py` pour propager, puis `python outils/synchroniser.py --verifier`.
3. `claude plugin validate --strict plugins/cadrage-projet` et `claude plugin validate --strict .`
4. `claude plugin eval plugins/cadrage-projet --no-publish` pour rejouer les évaluations (avec et sans plugin).

## Feuille de route

| Phase | Objet | État |
|---|---|---|
| 1 | Analyse et consolidation du besoin | Faite |
| 2 | Spécifications fonctionnelles | Faite (v0.3, avec réserves) |
| 3 | Critères d'acceptation et stratégie de tests | Partielle : 11 cas à un tour automatisés ; multi-tours à outiller (Q-02) |
| 4 | Matrice de traçabilité | Première version (`docs/tracabilite-v0.1.md`) |
| 5 | Architecture fonctionnelle et orchestration | Choix provisoires (D-14) |
| 6 | Choix techniques et interfaces | Choix provisoires (D-15) |
| 7 | Implémentation | Version 0.1.0, provisoire |
| 8 | Tests, évaluation, optimisation | Première campagne |
| 9 | Documentation et validation finale | À faire |
