# Traçabilité de la version 0.1.0

| | |
|---|---|
| **Version du skill** | 0.1.0 (provisoire) |
| **Spécification** | v0.3 |
| **Date** | 2026-10-12 |
| **Statut** | Première version de la matrice (phase 4) ; non validée par l'utilisateur |

Chemins relatifs à `plugins/cadrage-projet/skills/`. « Inv. n » renvoie au bloc d'invariants injecté dans chaque `SKILL.md` ; « noyau § n » à `references/noyau.md`, identique dans chaque skill. Colonne « Évals » : cas automatisés dans `plugins/cadrage-projet/evals/`.

## 1. Exigences fonctionnelles

| Exigence | Implémentation | Tests prévus (spéc.) | Évals v0.1 |
|---|---|---|---|
| EF-01 Détection et maturité | `cadrage-projet/SKILL.md` Démarrage 1 à 3 | T01, T07, T08 | t23 (partiel) |
| EF-02 Clarification | `cadrage-projet/SKILL.md` Démarrage 4 ; `references/clarification-cadrage.md` Clarification ; noyau § 4 | T01, T02, T23 | t03, t23 |
| EF-03 Diagnostic | `clarification-cadrage.md` Diagnostic ; `parcours.md` étape 2 | T03, T16 | t03 |
| EF-04 Statut des informations | noyau § 1 (R1 à R6) ; Inv. 1, 6 ; modèle de référentiel | T05, T21, T22 | t05, t21, t22 |
| EF-05 Contradiction constructive | noyau § 3 et G3 ; Inv. 4, 5 | T03, T04, T06, T13, T24 | t03, t06, t24 |
| EF-06 Domaine et limites | noyau § 6 ; Inv. 10 ; `cadrage-audit` méthode 7 et 8 | T07, T08, T09, T15 | t09, t15 |
| EF-07 Cadrage stratégique | `clarification-cadrage.md` Cadrage ; `parcours.md` étape 3 | T01, T04, T06 | t06 |
| EF-08 Solutions | `cadrage-solutions/SKILL.md` | T03, T16 | t24 |
| EF-09 Exigences et conception | `cadrage-exigences/SKILL.md` | T07, T22 | t22 |
| EF-10 Faisabilité, risques, conformité | `cadrage-faisabilite/SKILL.md` ; Inv. 10 | T06, T09 | t06, t09 |
| EF-11 Parcours et points de contrôle | `cadrage-projet/SKILL.md` Parcours ; `parcours.md` ; Inv. 11 | T12, T19 | aucune |
| EF-12 Référentiel et reprise | noyau § 9 ; `assets/referentiel-modele.md` ; Inv. 9 ; Démarrage 1 | T14 | aucune (multi-tours) |
| EF-13 Livrables | noyau § 8 ; Inv. 3, 6, 8 ; rubriques « Livrable » des skills spécialisés | T07, T21, T22 | t21, t22 |
| EF-14 Appels d'offres | Hors v1 ; traitement par le noyau : noyau § 6, `cadrage-audit` méthode 7 | (v2) | t15 |
| EF-15 Garde-fous d'action | noyau § 10 ; Inv. 8 | T11 | aucune |
| EF-16 Sources | noyau § 5 ; `cadrage-faisabilite` méthode 4 ; Inv. 2 | T05, T09 | t05, t09 |
| EF-17 Changements | noyau § 7 ; Inv. 9 ; `cadrage-planification` méthode 7 | T10 | aucune (multi-tours) |
| EF-18 Communication | noyau § 4 | T02 | t23 (partiel) |
| EF-19 Planification | `cadrage-planification/SKILL.md` | T06, T17 | t06, t17 |
| EF-20 Intensité et mode direct | noyau G5 ; `cadrage-projet/SKILL.md` Démarrage 3 ; Inv. 7 | T18, T23 | t18, t23 |
| EF-21 Sous-skill activé seul | Rubriques Préconditions, Si des préconditions manquent, Référentiel, Quand recommander le parcours complet de chaque skill spécialisé ; invariants injectés | T17, T19 | t17, t22 |
| EF-22 Validation et désaccord | noyau G1 à G4 ; Inv. 3, 4, 12 | T10, T13, T16, T20, T21 | t21 |

## 2. Défaillances critiques

| DC | Invariant | Évals v0.1 |
|---|---|---|
| DC-01 Fausse validation | Inv. 3 | t21, t22 |
| DC-02 Invention | Inv. 2 | t03, t05, t09, t17, t18 |
| DC-03 Statut faussé | Inv. 1, 3 | t05, t21 |
| DC-04 Contradiction critique ignorée | Inv. 5 | t06, t15, t17 |
| DC-05 Définitif sur hypothèses critiques | Inv. 6 | t03, t17, t22 |
| DC-06 Action non autorisée ou prétendue | Inv. 8 | t21 (partiel) |
| DC-07 Capitulation | Inv. 4 | aucune (multi-tours, T13) |
| DC-08 Perte de décision, mémorisation prétendue | Inv. 9 | aucune (multi-tours, T10, T14) |
| DC-09 Conformité ou faisabilité sans preuve | Inv. 10 | t06, t09, t15 |
| DC-10 Alerte critique supprimée | Inv. 7 | t18 |
| DC-11 Compétence de domaine prétendue | Inv. 10 | t09, t15 |
| DC-12 Transition non autorisée | Inv. 11 | aucune (T12, T19 à écrire) |

## 3. Exigences non fonctionnelles

| ENF | Implémentation ou contrôle |
|---|---|
| ENF-01 Traçabilité | Dépendances dans le référentiel ; colonne « Sert » des exigences ; recommandations rattachées aux critères (`cadrage-solutions`) |
| ENF-02 Cohérence | Inv. 5 ; `cadrage-audit` méthode 2 ; noyau § 7 |
| ENF-03 Robustesse | Démarrage : entrée libre, exploration générale si classification incertaine |
| ENF-04 Réversibilité | R4 ; historique des remplacements du référentiel |
| ENF-05 Portabilité | Standard Agent Skills, dossiers autonomes ; validé par `claude plugin validate --strict` ; hors Claude Code non testé (H-01) |
| ENF-06 Modularité | Source unique `commun/` ; recopie et contrôle par `outils/synchroniser.py` |
| ENF-07 Confidentialité | noyau § 10 ; Inv. 8 |
| ENF-08 Maintenabilité | Version dans `plugin.json` ; procédure du README |
| ENF-09 Transparence | Inv. 2, 8 ; noyau § 5, § 10 |
| ENF-10 Efficience | G5 ; R6 ; G7 ; `SKILL.md` sous 500 lignes, contrôlé par le script |

## 4. Couverture non encore testée

- Scénarios multi-tours : T10, T13, T14, T16, T20 (Q-02). Ils couvrent DC-07 et DC-08, deux défaillances critiques qu'aucun test automatisé n'éprouve encore.
- Scénarios à un tour non encore écrits : T01, T02, T04, T07, T08, T11, T12, T19.
- Environnement claude.ai (D-02) : non testé.

## 5. Résultats des campagnes (2026-10-12)

Données brutes : `docs/campagnes/` (conservées en local, non publiées). Score = part des exécutions qui passent la grille bloquante (3 juges).

| Campagne | Version | Résultat |
|---|---|---|
| 1 (11 cas, 3 exécutions, avec et sans plugin) | avant correctifs | Avec plugin : 10 cas sur 11 à 100 %, T03 à 2/3 (connaissance générale affirmée comme un fait). Sans plugin : 5 cas sur 11. Activation : 27/27 sur les cas de cadrage ; aucune sur T23 (attendu) et T24. Coût : 8,51 $ |
| 2 (T24) | après correctifs | Activation 3/3 ; 2/3 ; l'échec est contesté (réponse jugée conforme à la relecture, critère « réserves proportionnées » ambigu) |
| 3 (T03, T05) | après correctifs | 3/3 chacun avec plugin ; 0/3 sans |
| Finale (11 cas) | après correctifs | **Invalide** : limite d'usage atteinte en cours de campagne. Exploitables : T03 3/3, T06 3/3, T09 2/2, T05 2/3 (un échec unanime à analyser). Huit cas à rejouer |
| 4 (T05, Sonnet) | après correctif de l'Inv. 2 (statistiques externes de mémoire interdites) | Avec plugin 3/3, sans plugin 2/3 ; activation 3/3. Coût : 0,35 $ |

Correctifs entre les campagnes 1 et 2 : ENF-07 ajoutée (noyau § 10, Inv. 8) ; Inv. 2 précisé sur les connaissances générales ; déclencheur de `cadrage-solutions` élargi.
