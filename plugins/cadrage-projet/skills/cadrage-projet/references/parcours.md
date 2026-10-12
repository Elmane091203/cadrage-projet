# Parcours de cadrage

Les étapes ne sont pas imposées : le parcours commence au point d'entrée détecté et ne mobilise que les étapes utiles. Chaque étape indique son objectif, ses entrées, ses activités, ses résultats et ses conditions de sortie.

## Points d'entrée

| Point d'entrée | Étape de départ habituelle |
|---|---|
| Idée ou intuition | 1. Clarification |
| Problème ou constat | 1, puis 2 sans tarder |
| Besoin d'un tiers (client, direction, usager) | 1, en distinguant le besoin du tiers de sa demande de solution |
| Projet à concevoir, déjà clarifié | 3. Cadrage, après contrôle rapide des étapes 1 et 2 |
| Cahier des charges, projet engagé, solution à auditer, dossier d'appel d'offres | Audit (`cadrage-audit`), puis l'étape où apparaissent les premières lacunes |
| Solution déjà choisie par l'utilisateur | 1 et 2 d'abord : vérifier le problème avant de travailler la solution |

Contrôle rapide d'une étape : vérifier que ses conditions de sortie sont remplies à partir de ce qui est fourni, sans refaire le travail. Ce qui manque est signalé, pas reconstruit en entier.

---

## 1. Clarification de l'intention

- **Objectif** : comprendre ce que l'utilisateur cherche réellement à obtenir.
- **Entrées** : la demande, les documents fournis, le contexte déclaré.
- **Activités** : reformuler ; séparer résultat recherché et solution envisagée ; repérer les ambiguïtés qui changent les décisions ; questions ciblées.
- **Résultats** : intention reformulée ; premières hypothèses explicites ; questions ouvertes.
- **Sortie vers 2** : intention reformulée et acceptée par l'utilisateur ; problème et bénéficiaires identifiés, ou incertitudes explicitement listées.

## 2. Diagnostic du problème

- **Objectif** : établir que le problème existe, pour qui, et pourquoi.
- **Entrées** : intention clarifiée, faits disponibles.
- **Activités** : distinguer symptôme, problème supposé et causes possibles ; identifier personnes affectées et conséquences ; chercher ce qui confirmerait ou infirmerait le diagnostic.
- **Résultats** : diagnostic avec son niveau de preuve ; investigations recommandées si besoin (enquête, entretien, mesure, expérimentation).
- **Sortie vers 3** : problème suffisamment établi pour fixer des objectifs, ou décision explicite de l'utilisateur d'avancer avec un diagnostic provisoire. Le skill peut conclure que le problème n'est pas établi et recommander d'investiguer avant tout développement.

## 3. Cadrage stratégique

- **Objectif** : fixer ce que le projet doit atteindre et dans quelles limites.
- **Entrées** : problème diagnostiqué, contraintes déclarées.
- **Activités** : objectif formulé en résultat ; bénéficiaires et parties prenantes ; périmètre et exclusions ; critères de réussite mesurables ou vérifiables ; contraintes de temps, budget, ressources, conformité ; arbitrage des objectifs contradictoires ; tri des incertitudes bloquantes et reportables.
- **Résultats** : fiche de cadrage (objectifs, périmètre, contraintes, critères de réussite, incertitudes).
- **Sortie vers 4** : objectifs, périmètre préliminaire, contraintes majeures et critères de réussite identifiés ; besoin assez défini pour comparer des options. Objectif et périmètre sont des décisions structurantes à valider.

## 4. Étude des solutions (`cadrage-solutions`)

- **Objectif** : choisir une solution justifiée sans privilégier la première proposée.
- **Entrées** : cadrage, critères de réussite, contraintes.
- **Activités** : critères de comparaison issus du cadrage ; options pertinentes, y compris conserver l'existant, simplifier, expérimenter ou ne pas poursuivre ; comparaison sur des bases cohérentes ; compromis et risques.
- **Résultats** : comparaison argumentée ; recommandation justifiée.
- **Sortie vers 5** : option recommandée et compromis documentés ; **choix de solution validé** (décision structurante).

## 5. Exigences et conception (`cadrage-exigences`)

- **Objectif** : rendre la solution vérifiable.
- **Entrées** : solution choisie, cadrage, règles métier connues.
- **Activités** : exigences fonctionnelles et non fonctionnelles traçables ; règles métier, exceptions, rôles ; critères d'acceptation ; signalement des ambiguïtés ; choix de conception provisoires distingués des validés.
- **Résultats** : exigences et critères d'acceptation, au niveau de détail que justifie la maturité.
- **Sortie vers 6** : exigences critiques et conception assez précises pour évaluer risques et coûts.

## 6. Faisabilité, risques et conformité (`cadrage-faisabilite`)

- **Objectif** : savoir si le projet peut et doit être réalisé tel quel.
- **Entrées** : exigences, conception, contraintes.
- **Activités** : examen des dimensions technique, économique, opérationnelle, organisationnelle, juridique, temporelle ; risques et traitements ; conformité présumée, vérifiée ou à faire valider.
- **Résultats** : verdict de faisabilité argumenté ; registre des risques ; points de conformité.
- **Sortie vers 7** : faisabilité suffisamment étayée ; risques critiques traités, ou acceptés selon G3.

## 7. Planification (`cadrage-planification`)

- **Objectif** : organiser la réalisation de façon réaliste.
- **Entrées** : solution au moins provisoire, exigences, risques, contraintes de délai et de budget.
- **Activités** : découpage ; estimations en fourchettes ; dépendances et chemin critique ; jalons vérifiables ; confrontation aux échéances et budgets imposés.
- **Résultats** : planning provisoire ou validé, avec ses hypothèses.
- **Fin du parcours v1** : planning cohérent avec les décisions validées ; réserves visibles.

---

## Règles transversales

- **Clôture et ouverture.** Une étape n'est clôturée que si les décisions structurantes dont elle dépend sont validées. L'étape suivante peut être ouverte provisoirement avant cette clôture, sur décision explicite de l'utilisateur, avec des réserves visibles, notées dans le référentiel (« ouverte provisoirement, réserves : … »).
- **Condition non satisfaite.** Choisir entre approfondir, avancer provisoirement avec réserves, demander un arbitrage ou suspendre ; expliquer ce choix.
- **Incertitudes.** Les incertitudes critiques sont traitées avant les décisions qui en dépendent ; les questions non bloquantes sont reportées avec leur statut et leur impact.
- **Retour en arrière.** Une information nouvelle peut rouvrir une étape clôturée ; les éléments dépendants sont signalés et traités selon R4.
- **Suspension, réorientation, abandon.** Si la valeur ou la faisabilité est insuffisante, le recommander en l'expliquant (faits, hypothèses, ce qui changerait la conclusion). Si l'utilisateur veut poursuivre, appliquer G3.
- **Arrêt anticipé.** Le parcours peut s'arrêter à un cadrage, une recommandation ou un plan si l'objectif de l'utilisateur ne demande pas plus.
- **Documents.** Un document produit ne clôture jamais une étape.
