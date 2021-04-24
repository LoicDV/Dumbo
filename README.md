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

## Fin du projet.

- [x] Documentation Lark.
- [ ] Code Python.
	- [x] Lexèmes.
	- [ ] Grammaires.
- [ ] Rapport.
- [ ] Tests.