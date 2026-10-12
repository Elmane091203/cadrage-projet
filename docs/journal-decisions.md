# Journal des décisions : `cadrage-projet`

**Règles de tenue.** Ce journal applique au projet les règles du skill.

- Seule une réponse affirmative explicite de l'utilisateur à une question qui nomme la décision la fait passer à « validé » (G1). Le silence ou l'absence d'objection laisse la décision « provisoire ».
- Une entrée validée n'est jamais modifiée ni supprimée. Elle est remplacée par une nouvelle entrée qui la référence (R4).
- L'utilisateur est l'unique décideur (G4).

**Phase de construction en cours :** 3 à 8 menées de front depuis le 2026-10-12 (D-13) ; version 0.1.0 du skill implémentée, provisoire. Phase 2 clôturée avec réserves le 2026-10-12 (D-12). Spécification en vigueur : `specification-v0.3.md`.

---

## Décisions

### D-01. V1 limitée au noyau

- **État :** validé, 2026-10-09
- **Décision :** la v1 ne comporte aucun module de domaine.
- **Options écartées :**
  - noyau + logiciel/ERP, recommandation initiale de conception, parce que les scénarios existants y étaient déjà centrés ;
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

- **État :** validé, 2026-10-12 (Q-08). Auparavant provisoire, non objecté.
- **Contexte :** notion évoquée dans des échanges antérieurs sans être définie, absente de la mission.
- **Conséquence :** le besoin de graduation est couvert par l'intensité légère, standard ou approfondie (G5).

### D-04. Planification incluse dans la v1

- **État :**
  - planification en v1 : validé, 2026-10-09 ;
  - accompagnement de l'exécution reporté en v2, garde-fous d'action conservés en v1 : validé, 2026-10-12 (Q-08), décision structurante (retrait de périmètre). Auparavant provisoire, non objecté.
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

- **Écarts avec les recommandations initiales :**
  - B1 : la recommandation initiale était de ne valider explicitement que les décisions structurantes ;
  - B3 : la recommandation initiale était de s'incliner après un exposé unique ;
  - B4 : la recommandation initiale était de tracer le titulaire de chaque décision ;
  - B7 : la recommandation initiale était de prévoir des jalons quand l'environnement ne conserve pas les fichiers.
- **Conséquences :**
  - risque de fatigue de validation (RQ-02, T20) ;
  - validation par un consultant à la place du client (RQ-07) ;
  - interprétation d'application de G1 à confirmer (Q-01).

### D-10. Modèle d'information en trois axes (R1 à R6)

- **État :** validé, 2026-10-12 (Q-08), décision structurante. Présenté le 2026-10-09, resté provisoire jusque-là.
- **Décision :** type, fiabilité avec origine, état ; règles R1 à R6 (spécification, section 2).
- **Réserve connue :** hypothèse et interprétation partagent la fiabilité « supposé », pour que la notation reste reproductible.

### D-11. EF-11 : critère critique et défaillance DC-12

- **État :** validé, 2026-10-12, décision structurante.
- **Constat :** EF-11 était classée P0 sans aucun critère critique ni défaillance associée, contrairement à la définition de P0 (« son absence produit une défaillance critique »).
- **Décision :** CA-11.8 est marqué critique ; création de DC-12, transition non autorisée (étape clôturée sans validation des décisions structurantes, ou étape suivante ouverte sans décision explicite et réserves visibles).
- **Options écartées :**
  - rattacher CA-11.8 à DC-01 : la fausse validation est une notion voisine, et l'élargir la rendrait moins nette à noter ;
  - passer EF-11 en P1 : une transition prématurée cesserait d'être bloquante.
- **Conséquences :** spécification v0.3 ; T12 et T19 visent DC-12 ; les fiches de tests de la phase 3 doivent l'observer.

### D-12. Clôture de la phase 2

- **État :** validé, 2026-10-12, décision structurante.
- **Décision :** la phase 2 est clôturée sur la base de la spécification v0.3 ; la phase 3 est ouverte.
- **Réserves acceptées :**
  - la persistance sur claude.ai n'est pas garantie (RQ-06) et le format du référentiel reste une hypothèse (H-02, Q-04), à traiter en phase 6 ;
  - le dispositif des tests multi-tours n'est pas conçu (Q-02), à traiter en phase 3.
- **Conséquence :** la phase 3 peut rouvrir la spécification si une fiche de test révèle un critère intestable ; toute modification donnera une nouvelle version.

### D-13. Implémentation anticipée de la version 0.1.0

- **État :** décidé par l'utilisateur, 2026-10-12, par instruction explicite : « Agis de manière autonome et produis un skill correct et valide couvrant exactement les exigences, sans être superficiel ni superflu ».
- **Décision :** implémenter le skill sans attendre la clôture formelle des phases 3 à 6. Les choix que ces phases auraient dû soumettre sont pris à titre provisoire (D-14 à D-16) et restent à valider.
- **Conséquences :**
  - la règle « aucune implémentation avant la phase 7 » de `CLAUDE.md` est levée ;
  - la version 0.1.0 est provisoire : aucun de ses choix n'est validé, et sa validité n'est démontrée que par les contrôles et la campagne décrits dans `tracabilite-v0.1.md` ;
  - risque : une décision de phase 5 ou 6 refusée par l'utilisateur obligera à reprendre une partie de l'implémentation.

### D-14. Architecture de la version 0.1.0 (phase 5)

- **État :** provisoire, proposé le 2026-10-12, à valider (décision structurante).
- **Décision proposée :**
  - un plugin `cadrage-projet` qui contient six skills : l'orchestrateur `cadrage-projet`, qui porte le noyau (détection, intensité, clarification, diagnostic, cadrage, parcours, référentiel), et cinq skills spécialisés : `cadrage-audit`, `cadrage-solutions`, `cadrage-exigences`, `cadrage-faisabilite`, `cadrage-planification` ;
  - nommage (Q-06) : préfixe commun `cadrage-`, pour éviter les collisions quand un skill est installé seul ;
  - les cinq candidats de la spécification (section 9) satisfont le critère de découpage : chacun a de la valeur appelé seul, un déclencheur propre et des tests dédiés ; clarification et diagnostic restent dans le noyau ;
  - pas de sous-agent relecteur (Q-07), hors v1 selon la spécification (section 1.3).
- **Options écartées :** un skill unique avec fichiers de référence. Il serait plus simple et éviterait la recopie du noyau, mais il contredit l'orientation validée en D-05 et ne permet pas de tester EF-21.
- **Risque :** activation concurrente ou absente des skills (RQ-04), mesurée par l'indicateur d'activation des évals.

### D-15. Choix techniques de la version 0.1.0 (phase 6)

- **État :** provisoire, proposé le 2026-10-12, à valider.
- **Décisions proposées :**
  - Q-04 : référentiel en Markdown à tableaux, une ligne par élément, à `cadrage/referentiel.md` dans le répertoire de travail ; modèle `commun/referentiel-modele.md`. Markdown plutôt que YAML, parce qu'il est lisible par un utilisateur novice et facile à modifier ligne par ligne (G7) ;
  - Q-05 : instructions en français ; le skill répond dans la langue de l'utilisateur ; descriptions en français avec quelques mots-clés anglais pour le déclenchement ;
  - ENF-06 : le noyau a une source unique, `commun/`. `outils/synchroniser.py` injecte les invariants dans chaque `SKILL.md` et copie `noyau.md` et le modèle de référentiel dans chaque skill ; son mode `--verifier` contrôle la synchronisation et les contraintes de format ;
  - tests (Q-02, en partie) : `claude plugin eval`, avec un bras sans plugin, des grilles bloquantes notées par un modèle et un indicateur d'activation. Les scénarios multi-tours ne sont pas couverts.
- **Hypothèse :** le format `prompt.md` des évals ne joue qu'un tour ; la prise en charge d'un dialogue scripté n'est pas vérifiée.

### D-16. Application de G1 et calibrage de G5 (Q-01, Q-03)

- **État :** provisoire, proposé le 2026-10-12, à valider.
- **Décisions proposées :**
  - Q-01 : l'interprétation de la spécification est retenue (décisions provisoires au sein d'une étape, validées avant sa clôture). Un « ok » ou « continue » ne vaut validation que s'il répond clairement à la question de validation ; en cas de doute, le skill demande une confirmation courte ;
  - Q-03 : critères qualitatifs d'intensité (noyau, G5) ; au plus trois questions par échange en standard et approfondie, une en légère, aucune en mode direct.

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
| Q-01 | Application de G1 : travail sur des décisions provisoires au sein d'une étape, validation avant sa clôture. | Réponse provisoire D-16, à valider |
| Q-02 | Dispositif des tests multi-tours : tours scriptés ou utilisateur simulé. | Ouverte : tests à un tour seulement (D-15) |
| Q-03 | Calibrage des seuils d'intensité (G5) et du nombre de questions par échange (CA-02.4). | Réponse provisoire D-16, à valider |
| Q-04 | Format du référentiel : Markdown, YAML ou autre. | Réponse provisoire D-15, à valider |
| Q-05 | Langue des instructions du skill. | Réponse provisoire D-15, à valider |
| Q-06 | Nommage des sous-skills. | Réponse provisoire D-14, à valider |
| Q-07 | Sous-agent relecteur critique, propre à Claude Code. | Hors v1 (spécification, section 1.3) |
| Q-08 | Validation explicite de D-03, de D-04 (exécution en v2) et de D-10. | Résolue le 2026-10-12 : les trois sont validées |
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

1. Phase 2 clôturée (D-12).
2. Phase 3 : traiter Q-01, Q-02 et Q-03 ; fiches de tests complètes T01 à T24, protocole de notation, dispositif multi-tours. En option, une sonde de comportement sur T03, T05, T13 et T17, jouée contre un simple énoncé des principes du noyau.
3. Phase 4 : matrice de traçabilité objectifs → exigences → critères → tests.
4. Phases 5 à 9 selon `mission.md`.

---

## Historique

| Date | Événement |
|---|---|
| 2026-10-09 | Création du dépôt ; spécification v0.2 ; décisions D-01 à D-10 |
| 2026-10-12 | Neutralisation rédactionnelle des mentions d'auteur, sans changement de fond (y compris dans D-01 et D-09, par exception à R4 sur instruction de l'utilisateur) |
| 2026-10-12 | Validation de D-03, D-04 (exécution en v2) et D-10 ; Q-08 résolue ; D-11 ; spécification v0.3 ; clôture de la phase 2 avec réserves (D-12) |
