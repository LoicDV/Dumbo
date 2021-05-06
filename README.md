# <u> __Dumbo__ </u> 

### Projet créé par Loïc Dupont et Clément Durieux.

## <u> ___Utilisation du programme___ </u>:
```
python dumbo.py fichier_data fichier_template
```
**fichier_data** : fichier contenant le code en dumbo avec les variables.

**fichier_template** : fichier qui contient le texte (html) et du dumbo où
on injecte les données reçues à partir du fichier data.

## <u> ___2 Avril 2021.___ </u>

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

## <u> ___17 Avril 2021.___ </u>

Résolution des premiers exercices pour compléter la grammaire.

- [Synthèse Lark](https://lark-parser.readthedocs.io/_/downloads/en/latest/pdf/)

Mise en place de la grammaire (manque le txt).

Mise en place des expressions for, if et des booleans.

==> Regarder pour le txt et continuer les questions.

## <u> ___24 Avril 2021.___ </u>

Résolution complète de la grammaire.

Début du reste de l'analyse syntaxique.

- [Interpreteur de Lark](https://pastebin.com/y5rryEvE)

Etant donné que notre code utilisera en partie l'interpreteur déjà présent, autant avoir un moyen de le retrouver facilement. (__ligne 310__)

## <u> ___30 Avril 2021.___ </u>

Recherche de moyen pour écrire les fonctions + gérer les différentes scopes.

`visit` et `visit_children`, 2 fonctions qu'on doit utiliser pour chercher les différents noeuds.

Utilisation de liste chainée pour gérer les scopes ? \
Pas de résultat concret donc laissé de coté.

Utilisation d'un objet Scope qui contiendrait un dictionnaire (clé : la variable, valeur : la donnée ) ainsi qu'une liste chainée avec les précédents dictionnaire (permet de faire des pseudo-rollback pour récupérer les données avant d'entrer dans un autre scope qui peuvent être utilisée).

**TODO** Faire le reste des fonctions sans oublier d'inclure l'objet Scope.

## <u> ___1 Mai 2021.___ </u>

Fin du Scope + discussion entre nous pour valider le 30 Avril.

Fin des définitions pour la grammaire. \
Début des tests sur Moodle.

## <u> ___4 Mai 2021.___ </u>

Suite des debugs concernants les templates.

Template 1 ok. \
Debut du template 2.

Probleme de détection avec le symbole "+" dans les assignations.

Séparation de l'assignement pour les variables et la partie arithmétique.

## <u> ___5 Mai 2021.___ </u>

Complication avec le template 2. \
Résoud des bugs avec les strings_expression.

Template 2 se compile mais des problèmes sont remarqués dans la output.

**TODO** Corriger les bugs du template 2 pour passer au 3eme template.

## <u> ___6 Mai 2021.___ </u>

Suite des corrections des bugs du template 2.

Output sortie : 
```
<html><head><title> Mes plus belles vacances </title></head><body><h1> Mes plus belles vacances </h1> <a href ="  <a href ="  <a href ="  <a href =" <br/><br/>Ilya i1 photosdanslalbum" Coucher de soleil.png ".</body></html>
```

Output attendue : 
```
<html><head><title>Mes plus belles vacances</title></head><body><h1>Mes plus belles vacances</h1><a href ="Mon beau bateau.png">Mon beau bateau.png</a><a href ="Belle maman.png">Belle maman.png</a><a href ="Apero.png">Apero.png</a><a href ="Coucher de soleil.png">Coucher de soleil.png</a><br /><br />Il y a 4 photos dans l album "Mes plus belles vacances".</body></html>
```

## <u> ___Fin du projet.___ </u>

- [x] Documentation Lark.
- [ ] Code Python.
	- [x] Lexèmes.
	- [ ] Grammaires.
- [ ] Exemples.
	- [x] Exemple 1.
	- [x] Exemple 2.
	- [ ] Exemple 3.
	- [x] Exemple 1 (sans bug).
	- [ ] Exemple 2 (sans bug).
	- [ ] Exemple 3 (sans bug).
- [ ] Rapport.
- [ ] Tests.