# Libaririe pour prendre en ligne de commande.
import sys
from liste_chainee import *

# Librairie Lark.
from lark import Lark, Token
from lark import UnexpectedToken
from lark import tree as Tree
from lark.visitors import Interpreter

# Classe pour gérer les scopes des différentes fonctions (dumbo_block, if, for)
class Scope():
    
    def __init__(self, dictio = {}):
        self.dictio = {}
        self.other = LC()

    def isIn(self, obj):
        flag = False
        for elem in self.dictio.items():
            if (elem[0] == obj):
                flag = True
                break
        return flag
    
    # Attention, si la key est deja présente, cela l'écrase.
    def add(self, key, value):
        self.dictio[key] = value

    def search(self, obj):
        res = None
        if self.isIn(obj):
            res = self.dictio[obj]
        return res
    
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
# Avec la classe Interpreter de Lark, on a accès au visit_children(Tree).
# Va rentrer dans les sous-sarbres.
class OurInterpreter(Interpreter):
    
    # Lance la sémantique.
    def display(self, tree):
        super(OurInterpreter, self).visit(tree)
        return self.myPrint.printer

    # Démarre notre interpretteur.
    def __init__(self, scope):
        super().__init__()
        self.scope = scope
        self.myPrint = Print()
    
    def __str__(self):
        return self.myPrint
    
    # Définis le mot programme dans la grammaire.
    def programme(self, tree):
        self.visit_children(tree)
    
    # Définis le mot txt dans la grammaire.
    def txt(self, tree):
        for elem in tree.children:
            self.myPrint.add(elem.value)
        
    # Définis le mot dumbo_bloc dans la grammaire.
    def dumbo_bloc(self, tree):
        self.visit_children(tree)

    # Définis le mot expresssion_list dans la grammaire.
    def expresssion_list(self, tree):
        self.visit_children(tree)

    # Définis le mot expression dans la grammaire.
    def expression(self, tree):
        expression = tree.children[0].data
        # Avec la grammaire, on a que 4 possibilités.
        if expression == "for_expr" or expression == "if_expr":
            self.scope.other.begin_insert(self.scope.dictio)
            self.visit_children(tree)
            self.scope.dictio = self.scope.other.begin_remove().data
        # cas assignement de variable ou print.
        else:
            self.visit_children(tree)

    # Définis le mot add_expr dans la grammaire.
    def add_expr(self, tree):
        # On initialise avec le premier élément.
        first_under_tree = self.visit(tree.children[0])
        if self.scope.search(first_under_tree) != None:
            res = self.scope.search(first_under_tree)
        else:
            res = first_under_tree
        # On itère par deux avec en i l'opérateur et en i+1 le prochain entier.
        for i in range(1, len(tree.children), 2):
            next_int = self.visit(tree.children[i+1])
            operator = tree.children[i].value
            if (operator == "+"):
                res += next_int
            else:
                res -= next_int
        return res

    # Définis le mot mul_expr dans la grammaire.
    def mul_expr(self, tree):
        # On initialise avec le premier élément.
        first_int = tree.children[0]
        if self.scope.search(first_int) != None:
            res = int(self.scope.search(first_int))
        else:
            res = int(first_int)
        # On itère par deux avec en i l'opérateur et en i+1 le prochain entier.
        for i in range(1, len(tree.children), 2):
            next_int = tree.children[i+1].value
            if (self.scope.search(next_int) != None):
                next_int = int(self.scope.search(next_int))
            else:
                next_int = int(next_int)
            operator = tree.children[i].value
            if (operator == "*"):
                res *= next_int
            else:
                res //= next_int
        return res

    # Définis le mot inf_expr dans la grammaire.
    def inf_expr(self, tree):
        flag = False
        if (self.visit(tree.children[0]) < self.visit(tree.children[1])):
            flag = True
        return flag

    # Définis le mot sup_expr dans la grammaire.
    def sup_expr(self, tree):
        flag = False
        if (self.visit(tree.children[0]) > self.visit(tree.children[1])):
            flag = True
        return flag

    # Définis le mot eq_expr dans la grammaire.
    def eq_expr(self, tree):
        flag = False
        if (self.visit(tree.children[0]) == self.visit(tree.children[1])):
            flag = True
        return flag

    # Définis le mot dif_expr dans la grammaire.
    def dif_expr(self, tree):
        flag = False
        if (self.visit(tree.children[0]) != self.visit(tree.children[1])):
            flag = True
        return flag

    # Définis le mot mul_int dans la grammaire.
    def mul_int(self, tree):
        # De part la grammaire, si on a qu'un element dans children.
        if (len(tree.children) == 1):
            if (tree.children[0].type == "INT"):
                res = int(tree.children[0].value)
            elif (tree.children[0].type == "VARIABLE"):
                res = int(self.scope.search(tree.children[0].value))
            else:
                raise InterpreterError(sys.argv[1], tree.children[0], "Doit être une variable ou un int.")
        else:
            # Plusieurs éléments dans le children.
            # On initialise la premiere valeur.
            pot_int = tree.children[0].value
            if (self.scope.search(pot_int) != None):
                res = int(self.scope.search(pot_int))
            else:
                res = int(pot_int)
            # On itère par deux avec en i l'opérateur et en i+1 le prochain entier.
            for i in range(1, len(tree.children), 2):
                operator = tree.children[i].value
                pot_int = tree.children[i+1].value
                if (self.scope.search(pot_int) != None):
                    pot_int = self.scope.search(pot_int)
                if operator == "*":
                    res *= int(pot_int)
                else:
                    res //= int(pot_int)
        return res
    
    # Définis le mot print_expr dans la grammaire.
    def print_expr(self, tree):
        res = self.visit_children(tree)[0]
        # Si on tombe sur une variable.
        if (self.scope.search(res) != None):
            self.myPrint.add(self.scope.search(res))
        else:
            self.myPrint.add(res)

    # Définis le mot add_int dans la grammaire.
    def add_int(self, tree):
        if (len(tree.children) == 1):
            # Element seul donc par la grammaire c'est un token variable ou int. 
            if isinstance(tree.children[0], Token):
                res = int(tree.children[0].value)
            else:
                res = self.visit_children(tree)[0]
        else:
            # Plusieurs élements.
            # On initialise le premier int.
            res = int(self.visit(tree.children[0]))
            # On itère par deux avec en i l'opérateur et en i+1 le prochain entier.
            for i in range(1, len(tree.children), 2):
                operator = tree.children[i].value
                if operator == "+":
                    res += int(self.visit(tree.children[i+1]))
                else:
                    res -= int(self.visit(tree.children[i+1]))
        return res

    # Définis le mot bool_expr dans la grammaire.
    def bool_expr(self, tree):
        if (len(tree.children) > 1):
            # On initialise le premier booléen.
            if (isinstance(tree.children[0], Token)):
                flag = tree.children[0].value
            else:
                flag = self.visit(tree.children[0])
            # On itère par deux avec en i l'opérateur et en i+1 le prochain booléen.
            for i in range(1, len(tree.children), 2):
                operator = tree.children[i].value
                next_flag = self.visit(tree.children[i+1])
                if (operator == "or"):
                    flag = flag or next_flag
                else:
                    flag = flag and next_flag
            return flag
        else:
            # Soit une variable, True ou False.
            if isinstance(tree.children[0], Token):
                flag = tree.children[0].value
                if (self.scope.search(flag) != None):
                    flag = self.scope.search(flag)
                if (flag == "true"):
                    flag = True
                elif (flag == "false"):
                    flag = False
                else:
                    raise InterpreterError(sys.argv[1], tree.children[0], "Doit être une variable ou un booléen.")
            else:
                flag = self.visit(tree.children[0])
        return flag

    # Définis le mot if_expr dans la grammaire.
    def if_expr(self, tree):
        flag = self.visit(tree.children[0])
        if (flag):
            self.visit(tree.children[1])

    # Définis le mot for_expr dans la grammaire.
    def for_expr(self, tree):
        # var : Token, liste_elem : Token/Tree, liste_expr: Tree.
        var, liste_elem, liste_expr = tree.children
        var_stock = self.scope.search(tree.children[0])
        if (isinstance(liste_elem, Token)):
            # Si liste_elem est un Token.
            for i in range(len(self.scope.search(liste_elem))):
                self.scope.add(var.value, self.scope.search(liste_elem)[i])
                self.visit_children(liste_expr)
                self.scope.add(var.value, var_stock)
                self.scope.dictio = self.scope.other.head.data
        else:
            # Si liste_elem est un Tree.
            for elem in liste_elem.children[0].children:
                self.scope.add(var.value, self.visit_children(elem)[0])
                self.visit_children(liste_expr)
                self.scope.add(var.value, var_stock)
                self.scope.dictio = self.scope.other.head.data

    # Définis le mot assign_expr dans la grammaire.
    def assign_expr(self, tree):
        self.visit_children(tree)

    # Définis le mot assign_expr_var dans la grammaire.
    def assign_expr_var(self, tree):
        if (isinstance(tree.children[1], Token)):
            self.scope.add(tree.children[0].value, tree.children[1].value)
        else:
            self.scope.add(tree.children[0].value, self.visit(tree.children[1]))

    # Définis le mot assign_expr_arith dans la grammaire.
    def assign_expr_arith(self, tree):
        if isinstance(tree.children[1], Tree.Tree):
            self.scope.add(tree.children[0], self.visit(tree.children[1]))
        else:
            self.scope.add(tree.children[0].value, tree.children[1].value)

    # Définis le mot string_expression dans la grammaire.
    def string_expression(self, tree):
        res = ""
        if(len(tree.children) > 1):
            # Cas des plusieurs fils.
            if (isinstance(tree.children[0], Token)):
                # Opération arithmétique avec * et /.
                if((tree.children[0].type == "VARIABLE") or (tree.children[0].type == "INT")):
                    # On initialise le premier int.
                    res = tree.children[0].value
                    if (self.scope.search(res) != None):
                        res = int(self.scope.search(res))
                    else:
                        res = int(res)
                    # On itère par deux avec en i l'opérateur et en i+1 le prochain int.
                    for i in range(1, len(tree.children), 2):
                        operator = tree.children[i].value
                        pot_int = tree.children[i+1].value
                        if (self.scope.search(pot_int) != None):
                            pot_int = self.scope.search(pot_int)
                        if (operator == "*"):
                            res *= int(pot_int)
                        else:
                            res //= int(pot_int)
            else:
                # Concaténation de 2 Tree.
                res += self.visit(tree.children[0])
                res += self.visit(tree.children[2])
        else:
            # Un seul fils.
            if (isinstance(tree.children[0], Tree.Tree)):
                # String.
                res += self.visit(tree.children[0])
            else:
                # Variable
                res += str(self.scope.search(tree.children[0].value))
        return res

    # Définis le mot string_list dans la grammaire.
    def string_list(self, tree):
        return self.visit_children(tree)[0]

    # Définis le mot string_list_interior dans la grammaire.
    def string_list_interior(self, tree):
        liste = []
        for elem in tree.children:
            liste.append(self.visit(elem))
        return liste

    # Définis le mot string dans la grammaire.
    def string(self, tree):
        try :
            return tree.children[0].value
        except(UnexpectedToken) : 
            print("error " + file + ":", file=sys.stderr)
                        
# Classe pour mettre en évidence l'erreur lors de l'interprétation.
class InterpreterError(Exception):
    
    # Construit notre message d'erreur.
    def __init__(self, file, tree, message):
        super(InterpreterError, self).__init__("In " + file + ": " + str(tree) + ": " + message)

if __name__ == '__main__':

    with open(".\src\lark_grammar.lark", "r") as grammar_file:

        # Notre grammaire.
        grammar = grammar_file.read()

        scope = Scope()

        # Les 2 fichiers (data - template). 
        for file in sys.argv[1:]:
            with open(file, "r") as fileReady:
                # Test du programme
                try:
                    # Repartition des éléments suivants la grammaire.
                    tree = Lark(grammar, start='programme', parser="lalr").parse(fileReady.read())
                    # Sémantique de l'arbre.
                    result = OurInterpreter(scope).display(tree)
                    if result is not None:
                        print(result, end = "")
                # Exception qu'il peut y avoir (mauvais caractère ou mauvaise interprétation)
                except UnexpectedToken as e:
                    print("Erreur dans la syntaxe.")
                except InterpreterError as e:
                    print(e, file=sys.stderr)