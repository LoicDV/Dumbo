# Dumbo

### Projet créé par Loïc Dupont et Clément Durieux.

## Utilisation du programme :
```
python dumbo.py fichier_data fichier_template
```
**fichier_data** : fichier contenant le code en dumbo avec les variables.

**fichier_template** : fichier qui contient le texte (html) et du dumbo où
on injecte les données reçues à partir du fichier data.

## 2 Avril 2021.

Début du projet de compilation sur le dumbo.

Création des différents répertoire + compréhension du PDF.

Lecture de la documentation de Lark.

Pour installer Lark :

```
pip install lark-parser
```

Concernant la grammaire, nous nous baserons sur ce lien :
- [Documentation Lark](https://lark-parser.readthedocs.io/en/latest/grammar.html)
- [Cheat Sheet](https://lark-parser.readthedocs.io/en/latest/_static/lark_cheatsheet.pdf)
- [Exemple](https://github.com/lark-parser/lark/blob/master/examples/fruitflies.py)
- [Hello World](https://dev.to/vicentemaldonado/python-lark-parser-introduction-2g4e)
- [common.lark](https://github.com/lark-parser/lark/blob/master/lark/grammars/common.lark)

Début de création du fichier _lark_grammar.py_ pour se familiariser avec Lark.

## 17 Avril 2021.

Résolution des premiers exercices pour compléter la grammaire.

- [Synthèse Lark](https://lark-parser.readthedocs.io/_/downloads/en/latest/pdf/)

Mise en place de la grammaire (manque le txt).

Mise en place des expressions for, if et des booleans.

==> Regarder pour le txt et continuer les questions.

## 24 Avril 2021.

Résolution complète de la grammaire.

Début du reste de l'analyse syntaxique.

- [Interpreteur de Lark](https://pastebin.com/y5rryEvE)

Etant donné que notre code utilisera en partie l'interpreteur déjà présent, autant avoir un moyen de le retrouver facilement. (__ligne 310__)

## 30 Avril 2021.

Recherche de moyen pour écrire les fonctions + gérer les différentes scopes.

`visit` et `visit_children`, 2 fonctions qu'on doit utiliser pour chercher les différents noeuds.

Utilisation de liste chainée pour gérer les scopes ? \
Pas de résultat concret donc laissé de coté.

Utilisation d'un objet Scope qui contiendrait un dictionnaire (clé : la variable, valeur : la donnée ) ainsi qu'une liste chainée avec les précédents dictionnaire (permet de faire des pseudo-rollback pour récupérer les données avant d'entrer dans un autre scope qui peuvent être utilisée).

**TODO** Faire le reste des fonctions sans oublier d'inclure l'objet Scope.

## 1 Mai 2021.

Fin du Scope + discussion entre nous pour valider le 30 Avril.

Fin des définitions pour la grammaire. \
Début des tests sur Moodle.

## Fin du projet.

- [x] Documentation Lark.
- [ ] Code Python.
	- [x] Lexèmes.
	- [ ] Grammaires.
- [ ] Rapport.
- [ ] Tests.