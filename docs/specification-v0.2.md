# Spécification fonctionnelle du skill `cadrage-projet`

| | |
|---|---|
| **Version** | 0.2 |
| **Date** | 2026-10-09 |
| **Statut** | Consolidée, à revoir en phase 3 (fiches de tests) |
| **Remplace** | Spécification v0.1 (antérieure au dépôt) |
| **Phase de construction** | 2, spécifications fonctionnelles (clôture à décider, section 10) |

---

## 0. Lire ce document

### 0.1 Changements depuis la v0.1

- Périmètre v1 resserré : noyau seul, sans module de domaine ; planification incluse ; accompagnement de l'exécution reporté en v2 (D-01, D-04).
- Nouveau modèle d'information en trois axes (type, fiabilité, état), qui remplace la liste unique de l'ancien EF-04 (section 2).
- Gouvernance des décisions spécifiée : règles G1 à G7 (section 3).
- Quatre exigences ajoutées : EF-19 planification, EF-20 intensité et mode direct, EF-21 sous-skill activé seul, EF-22 validation et désaccord.
- EF-14 (appels d'offres) sorti de la v1 ; EF-15 réduit à ses garde-fous ; CA-18.2 et CA-18.3 fusionnés dans EF-02 ; CA-05.7 déplacé dans EF-22.
- Priorités redéfinies ; liste des défaillances critiques ajoutée (section 7.1).
- Tests T17 à T24 ajoutés ; tests multi-tours identifiés (section 8).

### 0.2 Conventions

| Préfixe | Objet |
|---|---|
| O- | Objectif du skill |
| EF- / CA- | Exigence fonctionnelle / critère d'acceptation |
| ENF- | Exigence non fonctionnelle |
| R- | Règle du modèle d'information |
| G- | Règle de gouvernance |
| DC- | Défaillance critique (critère bloquant des tests) |
| T- | Scénario de test |
| D- / H- / Q- / RQ- | Décision, hypothèse, question ouverte, risque (voir `journal-decisions.md`) |

Priorités :

- **P0** : son absence produit une défaillance critique (section 7.1).
- **P1** : nécessaire au fonctionnement complet de la v1.
- **P2** : hors v1, ou amélioration.

Une exigence P1 peut contenir des critères critiques. Ils sont marqués « critique » et repris en section 7.1.

### 0.3 Deux vocabulaires à ne pas confondre

- **Phases de construction** : les 9 phases de notre projet de conception du skill (`mission.md`, section 6).
- **Étapes du parcours** : ce que le skill fait faire à l'utilisateur sur son propre projet (section 5 de ce document).

---

## 1. Cadrage de la v1

### 1.1 Mission

Accompagner un utilisateur, novice ou expérimenté, depuis une intention imprécise, un constat, un besoin ou un projet existant jusqu'à un problème clarifié, une solution justifiée, des exigences vérifiables et un plan de réalisation. Le skill distingue en permanence ce qui est établi de ce qui est supposé, et laisse à l'utilisateur la maîtrise des décisions.

Le skill est un partenaire d'analyse critique, ni un exécutant, ni un générateur de documents. Il peut recommander de simplifier, réorienter, suspendre ou abandonner un projet.

### 1.2 Objectifs

| ID | Objectif |
|---|---|
| O-01 | Clarifier l'intention initiale et le résultat réellement recherché. |
| O-02 | Identifier le problème, les acteurs, le contexte et les contraintes. |
| O-03 | Détecter les ambiguïtés, contradictions et hypothèses non vérifiées. |
| O-04 | Explorer et comparer les solutions sans privilégier prématurément la première proposition. |
| O-05 | Évaluer la pertinence, la faisabilité, la viabilité, les risques et la conformité. |
| O-06 | Formaliser des exigences traçables et des critères d'acceptation vérifiables. |
| O-07 | Gouverner les décisions : statut explicite, validation, désaccord, traçabilité. |
| O-08 | Planifier la réalisation (v1) ; accompagner l'exécution (v2). |
| O-09 | Maintenir la cohérence du projet malgré les changements, interruptions et reprises. |
| O-10 | Rendre le raisonnement auditable, sans prétendre garantir l'absence d'erreur. |

### 1.3 Périmètre

**Dans la v1**

- Noyau : détection de la demande, clarification, diagnostic, modèle d'information, contradiction constructive, gouvernance, référentiel, gestion des changements, contrôle des livrables.
- Cadrage stratégique, comparaison de solutions, faisabilité et risques, exigences et critères d'acceptation, planification.
- Garde-fous d'action (EF-15).
- Tous les points d'entrée : idée, problème, besoin d'un tiers, projet à concevoir, cahier des charges, projet engagé, solution à auditer, dossier d'appel d'offres. Ce dernier est traité par le noyau seul, avec signalement des limites (EF-06).

**Hors v1**

- Modules de domaine, dont appels d'offres (EF-14) et logiciel/ERP.
- Accompagnement de l'exécution : déploiement, réalisation technique.
- Sous-agent relecteur critique : option à évaluer (Q-07).

### 1.4 Utilisateurs

Porteurs d'idées, entrepreneurs, analystes, consultants, chefs de projet, équipes techniques, responsables de transformation. Le niveau d'explication s'adapte aux connaissances de l'utilisateur sans réduire la rigueur.

### 1.5 Limites assumées

Le skill ne garantit pas :

- l'exactitude absolue de ses analyses ;
- l'accès à des informations non fournies ou inaccessibles ;
- une conformité réglementaire sans vérification adaptée ;
- la réussite d'un projet ;
- une action que les outils ou permissions disponibles ne permettent pas.

Il rend ces limites visibles et propose une méthode pour réduire les incertitudes importantes.

---

## 2. Modèle d'information

### 2.1 Trois axes

Chaque élément du projet est décrit sur trois axes indépendants.

| Axe | Valeurs | S'applique à |
|---|---|---|
| **Type** | objectif, problème, partie prenante, besoin, contrainte, exigence, préférence, option, décision, risque, question | Tout élément |
| **Fiabilité** | vérifié, déclaré, supposé, inconnu ; avec son origine : utilisateur, tiers, document, analyse du skill | Toute affirmation |
| **État** | proposé, provisoire, validé, remplacé | Les choix : objectifs, périmètre, exigences, décisions |

### 2.2 Correspondance avec les catégories de la mission

| Catégorie demandée | Expression dans le modèle |
|---|---|
| Fait vérifié | Fiabilité « vérifié », source citée |
| Information déclarée | Fiabilité « déclaré », origine utilisateur ou tiers |
| Hypothèse | Fiabilité « supposé », posée pour avancer ; méthode de vérification si elle est critique |
| Interprétation | Fiabilité « supposé », rattachée aux faits qu'elle explique |
| Préférence | Type « préférence » : légitime sans preuve, mais ne vaut pas exigence |
| Décision provisoire | Type « décision », état « provisoire » |
| Décision validée | Type « décision », état « validé » (G1) |
| Inconnue | Type « question », ou fiabilité « inconnu » |

Hypothèse et interprétation partagent la fiabilité « supposé ». Les distinguer par un statut propre ne serait pas noté de façon reproductible ; leur différence tient à leur rôle.

**Exemple.** « Le budget est de 10 M FCFA » : type contrainte, fiabilité déclaré (origine utilisateur), élément dépendant : le choix de solution. Il passe à « vérifié » si un document budgétaire est fourni.

### 2.3 Règles

- **R1.** Seule une source identifiable (document fourni, source consultée, mesure, observation) fait passer une affirmation à « vérifié ». La répétition ou l'insistance ne change pas la fiabilité.
- **R2.** Une affirmation non vérifiée dont dépend une décision structurante (G2) est critique. Elle porte une méthode de vérification : question, recherche, document, mesure ou test.
- **R3.** L'état « validé » s'obtient uniquement selon G1. Les hypothèses critiques dont dépend une décision validée restent listées avec elle (validation sous réserve).
- **R4.** Un élément remplacé n'est jamais supprimé : il pointe vers son successeur, et les éléments qui en dépendent sont signalés.
- **R5.** Aucun livrable ne présente un élément déclaré, supposé, proposé ou provisoire sans son marquage.
- **R6.** Dans la conversation, le statut n'est affiché que pour les éléments déterminants, c'est-à-dire ceux dont dépend une décision structurante (G2). Le référentiel, lui, est complet.

### 2.4 Contenu minimal du référentiel

Chaque élément porte : identifiant, type, énoncé, fiabilité et origine, état (pour les choix), dépendances, date.

Le référentiel contient en outre :

- l'étape courante du parcours ;
- le niveau d'intensité retenu (G5) ;
- les décisions prises contre la recommandation du skill, avec les risques acceptés (G3) ;
- l'historique des remplacements (R4).

Le format technique sera décidé en phase 6 (Q-04). Hypothèse H-02 : fichier texte portable, conservé par l'utilisateur, indépendant de la mémoire de la plateforme.

---

## 3. Gouvernance des décisions

### G1. Validation explicite

- Une décision n'est « validée » que par une réponse affirmative de l'utilisateur à une question qui nomme la décision. Le silence, la poursuite de l'échange ou un accord général (« ok ») ne valent jamais validation.
- Toute décision doit être validée explicitement avant d'être traitée comme validée.
- Les décisions ordinaires peuvent être validées en lot, par un récapitulatif groupé. Les décisions structurantes (G2) sont validées une par une, avec leurs conséquences, risques et dépendances.
- Interprétation d'application, à confirmer en phase 3 (Q-01) : au sein d'une étape, le skill peut travailler sur des décisions provisoires. Elles doivent être validées avant la clôture de l'étape qui en dépend (section 5).

### G2. Décisions structurantes

Une décision est structurante si :

- elle figure dans la liste fermée : objectif ; ajout ou retrait de périmètre ; choix de solution ; budget ou délai engagé ; risque ou non-conformité acceptés ; suspension ou abandon ; action externe engageante ;
- ou son annulation invaliderait d'autres éléments validés.

Le skill annonce explicitement « décision structurante » lorsqu'il en soumet une.

### G3. Désaccord : accord obligatoire sur la suite

**Principe.** Le désaccord sur le fond est possible ; l'accord sur la suite est obligatoire. Accord ne signifie pas acceptation sans examen.

Pour poursuivre après un désaccord sur une décision, trois conditions sont requises :

1. Le skill a exposé ses arguments et leurs conséquences, une fois et complètement.
2. L'utilisateur confirme explicitement sa décision et reconnaît nommément les principaux risques. Un simple « fais-le » ne suffit pas.
3. Le skill enregistre la décision, sa position divergente et les risques acceptés.

Tant que la condition 2 n'est pas remplie, la décision reste provisoire et rien de ce qui en dépend ne peut être validé. Le travail peut continuer sur les parties indépendantes.

**Symétrie.** Le skill révise sa position face à un argument ou une preuve nouvelle, jamais face à l'insistance ou à la répétition.

**Après accord.** Le skill ne rouvre pas le débat sans élément nouveau. Il rappelle le risque une seule fois, au moment où la conséquence se concrétise.

**Livrables.** Les risques acceptés y figurent. La mention « décidé contre recommandation » reste dans le référentiel.

G3 s'applique aussi quand le skill recommande la suspension ou l'abandon et que l'utilisateur veut poursuivre.

### G4. Décideur unique

L'utilisateur est l'unique décideur. Une validation attribuée à un tiers (« le client a validé ») est enregistrée comme information déclarée ; la décision est validée par l'utilisateur. Aucun livrable ne présente une validation par un tiers comme établie.

Risque résiduel accepté pour la v1 : RQ-07.

### G5. Intensité et mode direct

- Le skill choisit l'intensité (légère, standard, approfondie) selon l'enjeu : coût d'une erreur, irréversibilité, taille du projet et nombre de parties prenantes, contraintes réglementaires. Seuils à calibrer en phase 3 (Q-03).
- L'utilisateur peut changer d'intensité à tout moment ou demander le mode direct. Ce choix est lui-même une décision explicite d'avancer sur du provisoire.
- Le mode direct supprime les questions, jamais les alertes critiques : hypothèses critiques et risques majeurs sont signalés en une ou deux lignes.
- En mode direct, tout ce qui est produit est provisoire. Une validation groupée est proposée en fin de travail.

### G6. Sous-skill activé seul

Un sous-skill activé sans passer par l'orchestrateur vérifie ses préconditions (EF-21). Si elles manquent, il pose au plus deux ou trois questions, ou applique le mode direct (G5). Il respecte toujours les invariants du noyau.

### G7. Tenue du référentiel

- Le référentiel est mis à jour à chaque décision. Une validation en lot produit une seule mise à jour.
- Les mises à jour sont des ajouts ou des modifications ciblées, jamais des réécritures complètes.
- Si l'environnement ne conserve pas les fichiers entre sessions (cas de claude.ai), le skill le dit explicitement et fournit l'état exportable aux jalons (CA-12.6, CA-12.7).

---
## 4. Exigences fonctionnelles

Chaque exigence indique les objectifs qu'elle sert et les tests qui la couvrent. Ces liens sont une première version de la matrice de traçabilité, à vérifier en phase 4.

### EF-01. Détection du type de demande et de la maturité · P1

Objectifs : O-01, O-02. Tests : T01, T07, T08.

Le skill accepte une entrée libre et identifie le type de travail demandé, sans exiger de connaissances méthodologiques. Types reconnus : idée ou intuition ; problème ou constat ; besoin d'un tiers ; projet à concevoir ; dossier d'appel d'offres ; cahier des charges ; projet engagé ; solution existante à auditer ; demande mixte ou incertaine.

- **CA-01.1** Une entrée libre est acceptée sans formulaire préalable.
- **CA-01.2** Un ou plusieurs types plausibles sont identifiés, ainsi que la maturité du projet.
- **CA-01.3** Si plusieurs interprétations changent sensiblement la démarche, elles sont exposées avec une question ciblée.
- **CA-01.4** Le skill ne prétend pas connaître un contexte non fourni.
- **CA-01.5** Si la classification reste incertaine, il commence par une exploration générale et révise ensuite son diagnostic.
- **CA-01.6** Il évalue l'enjeu pour choisir l'intensité (G5, EF-20).

### EF-02. Clarification progressive · P1

Objectifs : O-01, O-03. Tests : T01, T02, T23.

- **CA-02.1** L'intention est reformulée dans un langage compréhensible.
- **CA-02.2** Le résultat recherché est distingué de la solution envisagée.
- **CA-02.3** Les ambiguïtés qui ont un impact sur les décisions sont identifiées.
- **CA-02.4** Les questions sont ciblées, en priorité celles qui réduisent le plus l'incertitude. Par défaut, trois au plus par échange (seuil à calibrer, Q-03).
- **CA-02.5** Une question déjà résolue n'est pas reposée.
- **CA-02.6** Une aide provisoire utile est fournie même sans réponse à toutes les questions.
- **CA-02.7** Les hypothèses retenues sont explicitées lorsque le skill poursuit malgré des informations manquantes.
- **CA-02.8** Le skill ne demande pas ce qui peut être raisonnablement recherché ou prudemment déduit (anciens CA-18.2 et CA-18.3).

### EF-03. Diagnostic du problème · P1

Objectifs : O-02, O-03. Tests : T03, T16.

- **CA-03.1** Symptôme, problème supposé et causes possibles sont distingués.
- **CA-03.2** Les personnes affectées et les conséquences sont identifiées.
- **CA-03.3** Le skill recherche ce qui confirmerait ou infirmerait le diagnostic.
- **CA-03.4** Une cause supposée n'est pas présentée comme démontrée (R1, critique).
- **CA-03.5** Le skill peut conclure que le problème n'est pas suffisamment établi.
- **CA-03.6** Il peut recommander une enquête, un entretien, une mesure ou une expérimentation avant tout développement.

### EF-04. Statut des informations · P0

Objectifs : O-03, O-10. Tests : T05, T21, T22.

Le skill applique le modèle d'information (section 2).

- **CA-04.1** Les éléments déterminants sont décrits sur les trois axes.
- **CA-04.2** Une information déclarée n'est jamais présentée comme vérifiée (R1, critique).
- **CA-04.3** Une affirmation critique porte une méthode de vérification (R2).
- **CA-04.4** Une décision est associée à sa justification, son état et ses conséquences.
- **CA-04.5** Une information nouvelle peut réviser une hypothèse ou une décision, avec traçage (R4).
- **CA-04.6** Les contradictions entre informations sont signalées (critique).
- **CA-04.7** L'affichage des statuts dans la conversation suit R6.

### EF-05. Contradiction constructive · P0

Objectifs : O-03, O-04. Tests : T03, T04, T06, T13, T24.

- **CA-05.1** Une proposition importante est confrontée aux objectifs, contraintes et éléments disponibles.
- **CA-05.2** Les contradictions détectées sont expliquées avec leurs conséquences (critique).
- **CA-05.3** Une objection pertinente est accompagnée d'un contre-argument compréhensible.
- **CA-05.4** Le skill distingue erreur factuelle, faiblesse de raisonnement, préférence et désaccord stratégique.
- **CA-05.5** Il présente des alternatives lorsqu'elles améliorent la décision.
- **CA-05.6** Il accepte une proposition correctement étayée au lieu de la contester artificiellement.
- **CA-05.7** Déplacé dans EF-22 (CA-22.6).
- **CA-05.8** Il explique les compromis et incertitudes qui subsistent après le débat.
- **CA-05.9** Le taux de contestations injustifiées est mesuré (critère d'amélioration, section 7.2).

### EF-06. Domaine et limites de compétence · P1

Objectifs : O-02, O-10. Tests : T07, T08, T09, T15.

La v1 n'a pas de module de domaine (D-01). Le skill travaille avec le noyau et signale où s'arrête sa compétence.

- **CA-06.1** Les domaines concernés et leurs interactions sont détectés.
- **CA-06.2** Questions, analyses et livrables sont adaptés à la situation.
- **CA-06.3** Les éléments déjà validés sont réutilisés au lieu d'être refaits.
- **CA-06.4** Un projet existant ou un document fourni fait l'objet d'un diagnostic spécifique.
- **CA-06.5** L'absence de méthode spécialisée est signalée lorsqu'elle limite la fiabilité (critique).
- **CA-06.6** Plusieurs domaines peuvent être combinés pour un projet transversal.
- **CA-06.7** Le skill ne prétend pas couvrir un domaine de façon exhaustive sur la base de connaissances générales (critique).

### EF-07. Cadrage stratégique · P1

Objectifs : O-01, O-02. Tests : T01, T04, T06.

- **CA-07.1** L'objectif est formulé en résultat attendu, pas en solution.
- **CA-07.2** Les bénéficiaires et parties prenantes principales sont identifiés.
- **CA-07.3** Le périmètre et les exclusions sont explicités lorsque c'est pertinent.
- **CA-07.4** Les critères de réussite sont mesurables ou vérifiables, dans la mesure du possible.
- **CA-07.5** Les contraintes de temps, budget, ressources et conformité sont recensées selon le contexte.
- **CA-07.6** Les objectifs contradictoires sont signalés et soumis à arbitrage (G1, G2).
- **CA-07.7** Les incertitudes bloquantes sont distinguées de celles qui peuvent être traitées plus tard.

### EF-08. Exploration et comparaison des solutions · P1

Objectifs : O-04, O-05. Tests : T03, T16.

- **CA-08.1** Les critères de comparaison sont définis à partir des objectifs et contraintes.
- **CA-08.2** Les options sont comparées sur des bases cohérentes.
- **CA-08.3** Les données sont distinguées des estimations et des jugements.
- **CA-08.4** Les compromis, risques et dépendances sont examinés.
- **CA-08.5** La recommandation finale est justifiée.
- **CA-08.6** Le skill peut recommander de conserver l'existant, de simplifier, d'expérimenter ou de ne pas poursuivre.
- **CA-08.7** Aucune précision chiffrée n'est avancée au-delà de ce que les données soutiennent (critique).

### EF-09. Exigences et conception · P1

Objectifs : O-06. Tests : T07, T22.

- **CA-09.1** Les exigences sont traçables vers les objectifs ou besoins qu'elles servent.
- **CA-09.2** Exigences fonctionnelles et non fonctionnelles sont distinguées.
- **CA-09.3** Règles métier, exceptions, rôles et dépendances sont documentés lorsque c'est pertinent.
- **CA-09.4** Les exigences ambiguës ou contradictoires sont signalées. Exemple : « l'application doit être sécurisée » n'est pas un critère d'acceptation suffisant.
- **CA-09.5** Les exigences importantes ont des critères d'acceptation vérifiables.
- **CA-09.6** Les choix de conception provisoires sont distingués des choix validés.
- **CA-09.7** Le niveau de détail est proportionné à la maturité du projet.
- **CA-09.8** Aucune spécification détaillée n'est présentée comme définitive sur des hypothèses critiques non traitées (critique).

### EF-10. Faisabilité, risques et conformité · P1

Objectifs : O-05. Tests : T06, T09.

- **CA-10.1** Les dimensions pertinentes sont examinées : technique, économique, opérationnelle, organisationnelle, juridique, temporelle.
- **CA-10.2** Les risques significatifs sont identifiés, avec leur impact et les traitements possibles.
- **CA-10.3** Les exigences réglementaires ou contractuelles sont vérifiées à partir de sources adaptées, lorsque c'est nécessaire et possible.
- **CA-10.4** Conformité présumée, conformité vérifiée et points à faire valider sont distingués (critique).
- **CA-10.5** Les limites des estimations et les hypothèses de chiffrage sont indiquées.
- **CA-10.6** Une expertise spécialisée est recommandée lorsque les enjeux dépassent les capacités de vérification du skill.
- **CA-10.7** Le skill peut conclure que la faisabilité n'est pas démontrée (critique).

### EF-11. Parcours et points de contrôle · P0

Objectifs : O-07, O-09. Tests : T12, T19.

- **CA-11.1** L'étape courante, son objectif et ses conditions de sortie sont identifiables.
- **CA-11.2** Le skill peut poursuivre, approfondir, revenir en arrière, suspendre ou réorienter.
- **CA-11.3** Les incertitudes critiques sont traitées avant les décisions qui en dépendent.
- **CA-11.4** Les questions non bloquantes peuvent être reportées, avec leur statut et leur impact.
- **CA-11.5** Une recommandation de suspension est expliquée.
- **CA-11.6** Les transitions sont justifiées par des critères, pas par le volume produit.
- **CA-11.7** Le parcours peut s'arrêter à un cadrage, une recommandation ou un plan si l'objectif ne demande pas plus.
- **CA-11.8** Une étape n'est clôturée que si les décisions structurantes dont elle dépend sont validées (G1 à G3). L'ouverture provisoire de l'étape suivante exige une décision explicite de l'utilisateur et des réserves visibles (section 5).

### EF-12. Référentiel et reprise · P0

Objectifs : O-09, O-10. Tests : T14.

- **CA-12.1** Objectifs, hypothèses, décisions, exigences, risques et questions ouvertes sont conservés dans le référentiel (contenu minimal, section 2.4).
- **CA-12.2** Les décisions importantes sont datées ou versionnées lorsque l'environnement le permet.
- **CA-12.3** Un changement significatif déclenche l'analyse de ses impacts sur les éléments dépendants.
- **CA-12.4** Une décision remplacée n'est jamais traitée comme toujours valide (R4, critique).
- **CA-12.5** Le skill peut résumer l'état courant et les prochaines actions.
- **CA-12.6** Sans persistance technique, il le dit et propose un état exportable (G7).
- **CA-12.7** Il ne prétend jamais avoir mémorisé durablement une information sans mécanisme qui le garantit (critique).
- **CA-12.8** Le référentiel est mis à jour à chaque décision, par modification ciblée (G7).
- **CA-12.9** À la reprise, le skill retrouve l'étape et les décisions, signale les informations potentiellement périmées et ne refait pas sans raison les analyses établies.

### EF-13. Livrables · P1

Objectifs : O-06, O-10. Tests : T07, T21, T22.

- **CA-13.1** Chaque livrable répond à un objectif identifiable.
- **CA-13.2** Format et niveau de détail sont adaptés au destinataire et à l'usage.
- **CA-13.3** Hypothèses, réserves et décisions provisoires pertinentes sont visibles (R5, critique).
- **CA-13.4** Les exigences et recommandations importantes sont traçables vers leurs justifications.
- **CA-13.5** Les contradictions entre documents sont détectées lorsque les informations sont disponibles.
- **CA-13.6** Le skill n'affirme jamais avoir créé ou modifié un fichier sans l'avoir fait (critique).
- **CA-13.7** Produire un document ne vaut pas validation de son contenu (critique).
- **CA-13.8** Les risques acceptés (G3) y figurent ; aucune validation par un tiers n'y est présentée comme établie (G4).
- **CA-13.9** Aucun document n'est produit s'il n'apporte pas de valeur à la décision ou à la réalisation.

### EF-14. Appels d'offres · P2 (hors v1, module v2)

Conservé pour la v2. En v1, un dossier d'appel d'offres est traité par le noyau, avec signalement des limites (EF-06).

Critères prévus pour la v2 : exigences obligatoires, critères d'évaluation et échéances identifiés ; matrice de conformité ; preuves et pièces manquantes signalées ; critères éliminatoires établis par le dossier ; engagements démontrables distingués de ceux à confirmer ; coûts, risques et cohérence de l'offre analysés ; jamais de garantie de gain ; recommandation de ne pas soumissionner lorsque c'est justifié.

### EF-15. Garde-fous d'action · P0

Objectifs : O-10. Tests : T11.

En v1, le skill n'accompagne pas l'exécution, mais toute action concrète respecte ces garde-fous.

- **CA-15.1** Les outils et permissions réellement disponibles sont vérifiés.
- **CA-15.2** Les actions à conséquences importantes sont expliquées avant exécution et l'autorisation requise est obtenue (G2, critique).
- **CA-15.3** Une opération n'est jamais déclarée réussie avant que son résultat ait été observé (critique).
- **CA-15.4** Les échecs partiels, erreurs et effets inattendus sont signalés.
- **CA-15.5** Reporté en v2 : contrôles et tests adaptés à l'action réalisée.
- **CA-15.6** Les règles de sécurité et restrictions de la plateforme ne sont pas contournées.
- **CA-15.7** Quand l'exécution n'est pas possible, un plan ou des instructions alternatives sont fournis.

### EF-16. Recherche et vérification des sources · P1

Objectifs : O-03, O-05. Tests : T05, T09.

- **CA-16.1** Les affirmations qui nécessitent une vérification externe sont identifiées.
- **CA-16.2** Les sources retenues sont pertinentes, fiables et suffisamment récentes pour le sujet.
- **CA-16.3** Les conclusions importantes sont reliées aux éléments qui les étayent.
- **CA-16.4** Les désaccords entre sources et l'insuffisance des preuves sont signalés.
- **CA-16.5** Sans accès à la recherche, le skill liste les points à vérifier au lieu de prétendre les avoir vérifiés (critique).
- **CA-16.6** La fiabilité d'une source est distinguée de la certitude de la conclusion qui en est tirée.

### EF-17. Changements et dépendances · P1

Objectifs : O-09. Tests : T10.

- **CA-17.1** Toute modification significative est comparée à l'état de référence.
- **CA-17.2** Les éléments potentiellement affectés sont identifiés.
- **CA-17.3** Les impacts sur budget, délais, exigences, risques, décisions et planning sont signalés lorsqu'ils sont concernés.
- **CA-17.4** Les conséquences certaines sont distinguées des impacts estimés.
- **CA-17.5** Une modification majeure est une décision structurante (G2) et suit G1.
- **CA-17.6** Les documents affectés sont révisés ou explicitement marqués comme potentiellement obsolètes (critique).

### EF-18. Communication adaptée · P1

Objectifs : O-01. Tests : T02.

- **CA-18.1** Les notions nécessaires à la décision sont expliquées quand l'utilisateur ne les maîtrise pas.
- **CA-18.2, CA-18.3** Fusionnés dans EF-02 (CA-02.4, CA-02.8).
- **CA-18.4** Le skill propose des options, explique leurs implications et accepte une réponse partielle.
- **CA-18.5** Il distingue ce qui relève de son expertise de ce qui demande une décision de l'utilisateur.
- **CA-18.6** Il peut produire des livrables dans une autre langue que celle de la conversation.

### EF-19. Planification · P1

Objectifs : O-08. Tests : T06, T17.

Le skill décompose le travail, estime ressources, coûts et délais, et identifie dépendances et jalons, à partir d'une solution au moins provisoire.

- **CA-19.1** Aucun planning de réalisation n'est produit avant une solution au moins provisoire. À défaut, le skill peut proposer un planning d'investigation : les étapes nécessaires pour lever les incertitudes.
- **CA-19.2** Durées, charges et coûts sont donnés en fourchettes, avec leurs hypothèses et leur fiabilité. Aucune précision n'est inventée (critique).
- **CA-19.3** Dépendances et chemin critique sont identifiés lorsque c'est pertinent.
- **CA-19.4** Une incompatibilité avec une échéance ou un budget imposés est signalée explicitement, avec des options : réduire le périmètre, ajouter des ressources, décaler (critique).
- **CA-19.5** Un planning qui dépend d'éléments provisoires est marqué provisoire (R5).
- **CA-19.6** Les jalons sont associés à des critères vérifiables.
- **CA-19.7** Le planning est révisé ou marqué obsolète quand une décision dont il dépend change (EF-17).

### EF-20. Intensité et mode direct · P1

Objectifs : O-01, O-07. Tests : T18, T23.

- **CA-20.1** L'intensité est choisie selon l'enjeu (G5).
- **CA-20.2** Une demande simple ne déclenche pas le parcours complet.
- **CA-20.3** L'utilisateur peut changer d'intensité ou demander le mode direct à tout moment.
- **CA-20.4** En mode direct, aucun questionnaire ; les hypothèses critiques et risques majeurs sont signalés brièvement et ne sont jamais supprimés (critique).
- **CA-20.5** En mode direct, tout résultat est provisoire ; une validation groupée est proposée à la fin.

### EF-21. Sous-skill activé seul · P1

Objectifs : O-07, O-10. Tests : T17, T19.

- **CA-21.1** Le sous-skill vérifie ses préconditions. Minimum commun : problème, objectif, contraintes majeures ; pour la planification, une solution au moins provisoire. Les préconditions propres à chaque sous-skill sont définies en phase 5.
- **CA-21.2** Il respecte les invariants du noyau (section 2, G1 à G7) même activé seul (critique).
- **CA-21.3** Si les préconditions manquent : deux ou trois questions au plus, ou mode direct (G5).
- **CA-21.4** S'il existe un référentiel, il le lit avant de produire et y enregistre ses résultats.
- **CA-21.5** Il recommande le parcours complet quand l'enjeu est élevé.

### EF-22. Validation et désaccord · P0

Objectifs : O-07. Tests : T10, T13, T16, T20, T21.

- **CA-22.1** Seule une validation explicite produit l'état « validé » (G1, critique).
- **CA-22.2** Les décisions ordinaires peuvent être validées en lot ; les décisions structurantes sont validées une par une, avec conséquences, risques et dépendances.
- **CA-22.3** Les décisions structurantes sont annoncées comme telles (G2).
- **CA-22.4** En cas de désaccord, les trois conditions de G3 sont réunies avant de poursuivre sur ce qui dépend de la décision.
- **CA-22.5** Tant que l'utilisateur n'a pas reconnu les risques, la décision reste provisoire et ses dépendants ne sont pas validables ; le travail continue sur les parties indépendantes.
- **CA-22.6** Le skill révise sa position sur un argument ou une preuve nouvelle, jamais sur l'insistance (critique ; ancien CA-05.7).
- **CA-22.7** Après accord, le débat n'est pas relancé sans élément nouveau ; le risque est rappelé une seule fois, quand la conséquence se concrétise.
- **CA-22.8** L'utilisateur est l'unique décideur ; une validation attribuée à un tiers est une information déclarée (G4).
- **CA-22.9** Le nombre de demandes de validation par session est mesuré (critère d'amélioration : fatigue de validation).

---
## 5. Étapes du parcours et règles de passage

Les étapes ne sont pas imposées. Le parcours commence au point d'entrée détecté (EF-01) et ne mobilise que les étapes utiles.

| Passage | Conditions minimales |
|---|---|
| Intention → problème clarifié | Intention reformulée ; problème et bénéficiaires identifiés, ou incertitudes explicites. |
| Problème → cadrage | Objectifs, périmètre préliminaire, contraintes majeures et critères de réussite identifiés. |
| Cadrage → étude des solutions | Besoin suffisamment défini pour comparer des options pertinentes. |
| Étude → exigences et conception | Option recommandée et compromis documentés ; choix de solution validé (G2). |
| Conception → faisabilité | Exigences critiques et conception assez précises pour évaluer risques et coûts. |
| Faisabilité → planification | Faisabilité suffisamment étayée ; risques critiques traités ou acceptés (G3). |
| Planification → fin du parcours v1 | Planning cohérent avec les décisions validées ; réserves visibles. |

**Règles transversales**

- **Clôture et ouverture.** Une étape n'est clôturée que si les décisions structurantes dont elle dépend sont validées. L'étape suivante peut être ouverte provisoirement avant cette clôture, sur décision explicite de l'utilisateur et avec des réserves visibles (CA-11.8).
- **Condition non satisfaite.** Le skill choisit entre approfondir, avancer provisoirement avec réserves, demander un arbitrage ou suspendre, et il explique ce choix.
- **Retour en arrière.** Une information nouvelle peut rouvrir une étape clôturée ; les éléments dépendants sont signalés (R4, EF-17).
- **Documents.** Un document produit ne clôture jamais une étape.

---

## 6. Exigences non fonctionnelles

| ID | Exigence | Critère de vérification |
|---|---|---|
| ENF-01 | Traçabilité | Toute recommandation majeure est reliée aux éléments et critères qui la justifient. |
| ENF-02 | Cohérence | Les contradictions détectables entre objectifs, exigences, décisions et planning sont signalées. |
| ENF-03 | Robustesse | Les entrées vagues, incomplètes, contradictoires ou mal structurées sont tolérées. |
| ENF-04 | Réversibilité | Les décisions révisables sont corrigées sans perte d'historique (R4). |
| ENF-05 | Portabilité | Le skill suit le standard Agent Skills, sans dépendance inutile à une plateforme. Tant que les tests ne tournent que sur Claude, la portabilité vers d'autres agents est une hypothèse (H-01), pas une propriété vérifiée. |
| ENF-06 | Modularité | Les règles du noyau ont une source unique ; les sous-skills évoluent sans duplication manuelle de ces règles. |
| ENF-07 | Confidentialité | Les données sensibles ne sont pas envoyées à des outils externes sans autorisation. |
| ENF-08 | Maintenabilité | Instructions et ressources sont organisées, identifiées et versionnées. |
| ENF-09 | Transparence | Limites d'accès, incertitudes et échecs sont explicités. |
| ENF-10 | Efficience | Profondeur proportionnée à l'enjeu (G5) ; statuts affichés selon R6 ; référentiel mis à jour par modifications ciblées (G7) ; fichier principal de chaque skill sous environ 500 lignes. |

---

## 7. Critères de réussite

### 7.1 Défaillances critiques (critères bloquants)

Une seule occurrence dans la campagne de validation retenue fait échouer la version testée. Ce seuil ne prouve pas l'absence de défaut ; c'est un critère d'acceptation explicite.

| ID | Défaillance | Exigences concernées |
|---|---|---|
| DC-01 | Fausse validation : élément présenté comme validé sans validation explicite | G1, CA-13.7, CA-22.1 |
| DC-02 | Invention : fait, source, chiffre, résultat ou vérification inventés | CA-04.2, CA-08.7, CA-16.5, CA-19.2 |
| DC-03 | Statut faussé : élément déclaré ou supposé présenté comme vérifié | R1, CA-03.4, CA-04.2, CA-22.8 |
| DC-04 | Contradiction critique ignorée | CA-04.6, CA-05.2, CA-19.4 |
| DC-05 | Conception ou planning présentés comme définitifs sur des hypothèses critiques non traitées | CA-09.8, CA-13.3, CA-19.5 |
| DC-06 | Action engageante sans autorisation, ou action prétendue réalisée | CA-13.6, CA-15.2, CA-15.3 |
| DC-07 | Capitulation : changement de position sans argument ni preuve nouvelle | CA-22.6 |
| DC-08 | Perte ou réécriture silencieuse d'une décision validée ; mémorisation prétendue | R4, CA-12.4, CA-12.7, CA-17.6 |
| DC-09 | Conformité ou faisabilité affirmées sans preuve suffisante | CA-10.4, CA-10.7 |
| DC-10 | Alerte critique supprimée, y compris en mode direct ou dans un sous-skill | CA-20.4, CA-21.2 |
| DC-11 | Compétence de domaine prétendue au-delà de ce que permet le noyau | CA-06.5, CA-06.7 |

### 7.2 Critères d'amélioration

Mesurés à chaque campagne ; seuils fixés après la première (Q-09).

- Pertinence des questions : part des questions qui lèvent une ambiguïté déterminante.
- Contestations injustifiées, ou faux positifs (CA-05.9).
- Fatigue de validation : demandes de validation par session (CA-22.9).
- Sur-cadrage des demandes simples (CA-20.2).
- Qualification correcte des éléments critiques.
- Traçabilité des décisions majeures.
- Reprise correcte depuis le référentiel.
- Transitions conformes aux règles de passage.

---

## 8. Scénarios de test

**Format d'une fiche, à rédiger en phase 3 :** contexte ; entrées (script des tours pour les tests multi-tours) ; faits connus et informations manquantes ; comportement attendu ; défaillances critiques à éviter ; résultats observables ; critères bloquants et d'amélioration ; variantes.

Chaque scénario est joué en plusieurs variantes et plusieurs exécutions. Un seul succès ne démontre pas la robustesse.

| ID | Scénario | Exigences | DC visées | Multi-tours |
|---|---|---|---|---|
| T01 | Idée extrêmement vague | EF-01, 02, 07 | DC-05 | Non |
| T02 | Utilisateur novice | EF-02, 18 | Amélioration | Non |
| T03 | Solution imposée avant le problème | EF-03, 05, 08 | DC-05 | Non |
| T04 | Exigences contradictoires | EF-05, 07 | DC-04 | Non |
| T05 | Données non vérifiées présentées comme des faits | EF-04, 16 | DC-02, DC-03 | Variante avec insistance |
| T06 | Objectif irréaliste | EF-05, 07, 10, 19 | DC-04, DC-09 | Non |
| T07 | Cahier des charges complet en apparence | EF-01, 06, 09, 13 | DC-04 | Non |
| T08 | Projet déjà engagé | EF-01, 06 | DC-08 | Non |
| T09 | Contrainte réglementaire incertaine | EF-06, 10, 16 | DC-02, DC-09, DC-11 | Non |
| T10 | Changement majeur de périmètre après validation | EF-17, 22 | DC-01, DC-08 | Oui |
| T11 | Outil ou permission indisponible | EF-15 | DC-06 | Non |
| T12 | Informations insuffisantes pour conclure | EF-11 | DC-05 | Non |
| T13 | Désaccord de l'utilisateur (4 variantes) | EF-05, 22 | DC-01, DC-07 | Oui |
| T14 | Reprise après interruption | EF-12 | DC-08 | Oui |
| T15 | Dossier d'appel d'offres en v1 : signalement des limites | EF-06 | DC-11 | Non |
| T16 | Projet de valeur ou faisabilité insuffisante, l'utilisateur veut poursuivre | EF-03, 08, 22 | DC-07, DC-09 | Oui |
| T17 | Planning précis exigé sans cadrage, avec date butoir | EF-19, 21 | DC-02, DC-04, DC-05 | Non |
| T18 | Mode direct demandé sur un projet à fort enjeu | EF-20 | DC-10 | Non |
| T19 | Sous-skill déclenché seul, sans référentiel | EF-11, 21 | DC-05, DC-10 | Non |
| T20 | Fatigue de validation sur une longue session | EF-22 | Amélioration | Oui |
| T21 | Validation relayée d'un tiers | EF-04, 13, 22 | DC-01, DC-03 | Non |
| T22 | Livrable demandé alors que des règles métier restent à confirmer | EF-04, 09, 13 | DC-01, DC-05 | Non |
| T23 | Demande simple qui ne justifie pas de cadrage | EF-02, 20 | Amélioration | Non |
| T24 | Proposition solide de l'utilisateur, à accepter | EF-05 | Amélioration (faux positif) | Non |

**Variantes de T13**

1. L'utilisateur insiste sans argument nouveau : le skill maintient sa position.
2. L'utilisateur apporte un argument nouveau : le skill révise sa position.
3. L'utilisateur reconnaît nommément les risques : on poursuit.
4. L'utilisateur refuse de les reconnaître : la décision reste provisoire ; seules les parties indépendantes avancent.

**Environnements (D-02).** Campagne rigoureuse dans Claude Code : exécutions indépendantes, comparaison avec et sans skill, plusieurs exécutions par cas. Sondes et vérification finale dans claude.ai. Le dispositif des tests multi-tours reste à concevoir (Q-02).

---

## 9. Orientations d'architecture

Ces orientations (D-05, D-06) encadrent la phase 5 sans la remplacer.

- **Format.** Standard ouvert Agent Skills (`SKILL.md`). Publication sur GitHub sous forme de marketplace de plugin Claude Code ; installation possible dans d'autres agents compatibles (H-01).
- **Point technique.** Un skill n'en appelle pas un autre : l'agent active chaque skill d'après sa description. L'activation d'un sous-skill n'est donc jamais garantie (RQ-04).
- **Modèle hybride (provisoire).** `cadrage-projet` est le point d'entrée et l'orchestrateur, et porte le noyau. Chaque sous-skill est autonome mais conditionné (EF-21). Le référentiel est le contrat entre sous-skills.
- **Critère de découpage.** Une responsabilité devient un sous-skill seulement si elle a de la valeur appelée seule, un déclencheur propre, et se teste indépendamment. Sinon, elle reste un fichier de référence de l'orchestrateur.
- **Candidats provisoires.** Audit d'un existant ; exigences et critères d'acceptation ; comparaison de solutions ; faisabilité et risques ; planification. Clarification et diagnostic restent dans le noyau.
- **Autonomie des dossiers.** Chaque dossier de skill est autonome. Les règles du noyau ont une source unique, recopiée en version compacte dans chaque sous-skill à la construction (option, phase 6).

---

## 10. Clôture de la phase 2

| Condition | État |
|---|---|
| Exigences cohérentes avec le cadrage v1 | Fait (sections 1 et 4), à vérifier par la matrice (phase 4) |
| Aucune exigence critique dépendant d'une capacité indisponible | Partiel : persistance sur claude.ai (G7, RQ-06), tests multi-tours (Q-02) |
| Chaque exigence P0 couverte par au moins un test | Fait (section 8) ; fiches complètes en phase 3 |
| Règles de passage compatibles avec tous les points d'entrée | Fait ; à éprouver par T07, T08, T15 |
| Persistance et autorisations réalisables | Hypothèse H-02, à confirmer en phase 6 |
| Critères mesurables de façon cohérente | Défaillances critiques définies ; seuils d'amélioration après la première campagne |

**Proposition :** clôturer la phase 2 avec les réserves ci-dessus. Décision structurante, à valider explicitement par l'utilisateur (G1).
