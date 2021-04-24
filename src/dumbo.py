# Libaririe pour prendre en ligne de commande.
import sys
import operator

# Librairie Lark.
from lark import Lark
from lark import UnexpectedToken
from lark import tree
from lark.visitors import Interpreter

# Classe pour la Sémantique.
# Les fonctions commençant et finissant par un seul _ sont pour la grammaire.
class OurInterpreter(Interpreter):
    
    # Définis les opérations.
    OPERATORS = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv,
                 '<' : operator.lt, '<=': operator.le, '>' : operator.gt, '>=': operator.ge,
                 '!=': operator.ne, '=' : operator.eq, '&' : operator.and_, '|' : operator.or_
    }
    
    # Démarre notre interpretteur.
    def __init__(self, tree):
        super().__init__()
    
    #
    def _programme_(self, tree):
        self.visit_children(tree)

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