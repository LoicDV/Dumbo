# Libaririe pour prendre en ligne de commande.
import sys
import operator
from liste_chainee import *

# Librairie Lark.
from lark import Lark
from lark import UnexpectedToken
from lark import tree
from lark.visitors import Interpreter

# Classe pour gérer les scopes des différentes fonctions (dumbo_block, if, for)
class Scope():
    
    def __init__(self, dictio = {}):
        self.dictio = dictio
        self.other = LC()

    def isIn(self, obj):
        flag = False
        for keys, values in self.dictio.items():
            if (keys == obj):
                flag = True
                break
        return flag
    
    # Attention, si la key est deja présente, cela l'écrase.
    def add(self, key, value):
        self.dictio[key] = value
    
# Classe qui retournera notre solution pour le problème.
class Print():

    def __init__(self, printer=""):
        self.printer = printer

    # Ajoute du contenu à notre solution.
    # more_printer doit être un str.
    def add(self, more_printer):
        self.printer += more_printer

    def __str__(self):
        return self.printer


# Classe pour la Sémantique.
# Les fonctions commençant et finissant par un seul _ sont pour la grammaire.
# Avec la classe Interpreter de Lark, on a accès au visit_children(Tree).
# Va rentrer dans les sous-sarbres.
class OurInterpreter(Interpreter):
    
    # Démarre notre interpretteur.
    def __init__(self):
        super().__init__()
        self.scope = Scope()
        self.myPrint = Print()
    
    # Définis le mot programme dans la grammaire.
    def programme(self, tree):
        self.visit_children(tree)
    
    # Définis le mot txt dans la grammaire.
    def txt(self, tree):
        # De part le code dans tree.py, children est une liste d'éléments.
        # Ici, on est dans txt qui ne va pas se dériver autrement donc il y a qu'un seul fils.
        self.myPrint.add(str(tree.children[0].value))
    
    # Définis le mot dumbo_bloc dans la grammaire.
    def dumbo_bloc(self, tree):
        # Gérer le dumbo_bloc par rapport à un autre dumbo_bloc
        # --> créer un objet spécifique pour eux.
        self.linkedList = LC()

        # Mettre des objets Scope dans la liste chainée.

        pass

    # Définis le mot expresssion_list dans la grammaire.
    def expresssion_list(self, tree):
        pass

    # Définis le mot expression dans la grammaire.
    def expression(self, tree):
        pass

    # Définis le mot expression dans la grammaire.
    def add_expr(self, tree):
        pass

    # Définis le mot expression dans la grammaire.
    def sub_expr(self, tree):
        pass

    # Définis le mot expression dans la grammaire.
    def mul_expr(self, tree):
        pass

    # Définis le mot expression dans la grammaire.
    def div_expr(self, tree):
        pass

    # Définis le mot expression dans la grammaire.
    def inf_expr(self, tree):
        pass

    # Définis le mot expression dans la grammaire.
    def sup_expr(self, tree):
        pass

    # Définis le mot expression dans la grammaire.
    def eq_expr(self, tree):
        pass

    # Définis le mot expression dans la grammaire.
    def dif_expr(self, tree):
        pass

    # Définis le mot expression dans la grammaire.
    def bool_expr(self, tree):
        pass

    # Définis le mot expression dans la grammaire.
    def if_expression(self, tree):
        pass

    # Définis le mot string_expression dans la grammaire.
    def string_expression(self, tree):
        pass

    # Définis le mot string_list dans la grammaire.
    def string_list(self, tree):
        pass

    # Définis le mot string_list_interior dans la grammaire.
    def string_list_interior(self, tree):
        pass

    # Définis le mot variable dans la grammaire.
    def variable(self, tree):
        pass

    # Définis le mot string dans la grammaire.
    def string(self, tree):
        pass

# Classe pour mettre en évidence l'erreur lors de l'interprétation.
class InterpreterError(Exception):

    # Construit notre message d'erreur.
    def __init__(self, file, tree, message):
        super(InterpreterError, self).__init__(file + " " + self.get_line_number(tree) + ": " + message)

    # Recupère la ligne ainsi que la colonne de l'erreur.
    def get_line_number(self, tree):
        return "ligne " + str(tree.line) + ", colonne " + str(tree.column) + "."

if __name__ == '__main__':

    with open("lark_grammar.lark", "r") as grammar_file:

        # Notre grammaire.
        grammar = grammar_file.read()

        # Les 2 fichiers (data - template). 
        for file in sys.argv[1:]:
            with open(file, "r") as fileReady:

                # Test du programme
                try:
                    # Repartition des éléments suivants la grammaire.
                    tree = Lark(grammar, start="programme", parser="lalr").parse(fileReady.read())
                    # Sémantique de l'arbre.

                # Exception qu'il peut y avoir (mauvais caractère ou mauvaise interprétation)
                except UnexpectedToken as e:
                    print("error " + file + ":", file=sys.stderr)
                except InterpreterError as e:
                    print(e, file=sys.stderr)