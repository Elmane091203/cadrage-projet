# Journal des décisions : `cadrage-projet`

**Règles de tenue.** Ce journal applique au projet les règles du skill.

- Seule une réponse affirmative explicite de l'utilisateur à une question qui nomme la décision la fait passer à « validé » (G1). Le silence ou l'absence d'objection laisse la décision « provisoire ».
- Une entrée validée n'est jamais modifiée ni supprimée. Elle est remplacée par une nouvelle entrée qui la référence (R4).
- L'utilisateur est l'unique décideur (G4).

**Phase de construction en cours :** 2, spécifications fonctionnelles. Spécification en vigueur : `specification-v0.2.md`.

---

## Décisions

### D-01. V1 limitée au noyau

- **État :** validé, 2026-10-09
- **Décision :** la v1 ne comporte aucun module de domaine.
- **Options écartées :**
  - noyau + logiciel/ERP, recommandé par l'assistant parce que les scénarios existants y étaient déjà centrés ;
  - noyau + appels d'offres.
- **Conséquences :**
  - EF-14 sort de la v1 ;
  - EF-06 est recentré sur le signalement des limites ;
  - les tests doivent couvrir plusieurs domaines pour éprouver le noyau.

### D-02. Environnements de test

- **État :** validé, 2026-10-09
- **Décision :**
  - Claude Code pour la campagne de tests rigoureuse : exécutions indépendantes, comparaison avec et sans skill ;
  - claude.ai pour les sondes et la vérification finale en conditions réelles.
- **Conséquences :**
  - tests multi-tours à outiller (Q-02) ;
  - persistance différente selon l'environnement (H-02, G7).

### D-03. Abandon des niveaux L1, L3, L5

- **État :** provisoire. Non objecté, jamais validé explicitement (Q-08).
- **Contexte :** notion évoquée dans des échanges antérieurs sans être définie, absente de la mission.

### D-04. Planification incluse dans la v1

- **État :**
  - planification en v1 : validé, 2026-10-09 ;
  - accompagnement de l'exécution reporté en v2, garde-fous d'action conservés en v1 : provisoire, non objecté (Q-08).
- **Conséquences :**
  - ajout d'EF-19 ;
  - EF-15 réduit à ses garde-fous ;
  - O-08 couvre la planification en v1 et l'exécution en v2.

### D-05. Architecture granulaire en sous-skills

- **État :**
  - orientation validée, 2026-10-09 ;
  - forme hybride provisoire, à valider en phase 5. Elle comprend un orchestrateur porteur du noyau, des sous-skills autonomes mais conditionnés, et un critère de découpage (spécification, section 9).
- **Contexte :** dans le standard Agent Skills, un skill n'en appelle pas un autre. L'agent active chaque skill d'après sa description.
- **Conséquences :**
  - ajout d'EF-21 ;
  - risque d'activation incertaine (RQ-04) ;
  - le référentiel devient le contrat entre sous-skills.

### D-06. Implémentation et publication

- **État :** validé, 2026-10-09
- **Décision :** implémentation dans Claude Code web, dépôt GitHub, skill installable (marketplace de plugin Claude Code, standard Agent Skills).
- **Conséquences :** ce dépôt est aussi le référentiel du projet de conception. La mémoire du projet claude.ai n'est pas accessible depuis Claude Code.

### D-07. Nom du skill

- **État :** validé (fixé par la mission)
- **Décision :** `cadrage-projet`.

### D-08. Démarche en 9 phases de construction

- **État :** validé (fixé par la mission)
- **Décision :** analyse du besoin, spécifications, critères et tests, traçabilité, architecture, choix techniques, implémentation, tests et optimisation, documentation et validation finale (`mission.md`, section 6).

### D-09. Gouvernance des décisions (G1 à G7)

- **État :** validé, 2026-10-09
- **Arbitrages de l'utilisateur :**

| Point | Choix | Règle |
|---|---|---|
| B1. Forme de la validation | A, avec lecture 1 confirmée : toute décision validée explicitement ; décisions ordinaires validables en lot, décisions structurantes une par une | G1 |
| B2. Décisions à valider | C : liste fermée + critère d'impact | G2 |
| B3. Désaccord | Formulation de l'utilisateur : « il faut un accord pour continuer, et accord ne signifie pas accepter sans broncher ». Formalisée et confirmée | G3 |
| B4. Décideur | A : l'utilisateur est l'unique décideur | G4 |
| B5. Intensité | B : intensité selon l'enjeu, mode direct possible sans supprimer les alertes | G5 |
| B6. Sous-skill seul | B : vérification des préconditions, questions limitées ou mode direct | G6 |
| B7. Référentiel | A : mise à jour à chaque décision | G7 |

- **Écarts avec les recommandations de l'assistant :**
  - B1 : l'assistant recommandait de ne valider explicitement que les décisions structurantes ;
  - B3 : il recommandait de s'incliner après un exposé unique ;
  - B4 : il recommandait de tracer le titulaire de chaque décision ;
  - B7 : il recommandait des jalons quand l'environnement ne conserve pas les fichiers.
- **Conséquences :**
  - risque de fatigue de validation (RQ-02, T20) ;
  - validation par un consultant à la place du client (RQ-07) ;
  - interprétation d'application de G1 à confirmer (Q-01).

### D-10. Modèle d'information en trois axes (R1 à R6)

- **État :** provisoire. Présenté le 2026-10-09, non objecté, jamais validé explicitement (Q-08).
- **Décision proposée :** type, fiabilité avec origine, état ; règles R1 à R6 (spécification, section 2).

---

## Hypothèses

| ID | Hypothèse | Vérification |
|---|---|---|
| H-01 | Cible : standard Agent Skills, premier environnement Claude. Noyau rédigé de façon portable. La portabilité vers d'autres agents n'est pas vérifiée. | Phase 6 ; tests sur d'autres agents avant toute promesse de portabilité |
| H-02 | Le référentiel d'un projet utilisateur est un fichier texte portable, conservé par l'utilisateur, indépendant de la mémoire de la plateforme. | Phase 6 |

---

## Questions ouvertes

| ID | Question | Échéance |
|---|---|---|
| Q-01 | Application de G1 : travail sur des décisions provisoires au sein d'une étape, validation avant sa clôture. | Phase 3 |
| Q-02 | Dispositif des tests multi-tours : tours scriptés ou utilisateur simulé. | Phases 3 et 6 |
| Q-03 | Calibrage des seuils d'intensité (G5) et du nombre de questions par échange (CA-02.4). | Phase 3 |
| Q-04 | Format du référentiel : Markdown, YAML ou autre. | Phase 6 |
| Q-05 | Langue des instructions du skill. | Phase 6 |
| Q-06 | Nommage des sous-skills. | Phase 5 |
| Q-07 | Sous-agent relecteur critique, propre à Claude Code. | Phase 5 |
| Q-08 | Validation explicite de D-03, de D-04 (exécution en v2) et de D-10. | Revue de la v0.2 |
| Q-09 | Seuils des critères d'amélioration. | Après la première campagne |

---

## Risques

| ID | Risque | Traitement |
|---|---|---|
| RQ-01 | Capitulation du modèle sous l'insistance de l'utilisateur | G3, CA-22.6, T13 |
| RQ-02 | Sur-questionnement et fatigue de validation, accentués par B1-A | G5, validation en lot, T20, T23 |
| RQ-03 | Volume d'instructions qui dilue les règles et coûte des tokens | ENF-10, découpage en sous-skills |
| RQ-04 | Activation incertaine des sous-skills | EF-21, tests de déclenchement |
| RQ-05 | Portabilité non vérifiée vers d'autres agents | ENF-05, H-01 |
| RQ-06 | Absence de persistance entre sessions sur claude.ai | G7, CA-12.6, CA-12.7 |
| RQ-07 | Validation par un consultant à la place du client réel (B4-A) | G4 ; à revoir en v2 |

---

## Prochaines étapes

1. Revue de la v0.2 par l'utilisateur : décider de la clôture de la phase 2 (spécification, section 10) et traiter Q-08.
2. Phase 3 : fiches de tests complètes T01 à T24, protocole de notation, dispositif multi-tours. En option, une sonde de comportement sur T03, T05, T13 et T17, jouée contre un simple énoncé des principes du noyau.
3. Phase 4 : matrice de traçabilité objectifs → exigences → critères → tests.
4. Phases 5 à 9 selon `mission.md`.

---

## Historique

| Date | Événement |
|---|---|
| 2026-10-09 | Création du dépôt ; spécification v0.2 ; décisions D-01 à D-10 |
