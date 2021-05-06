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
        print("debug : programme")
        print("-----------------")
        
        self.visit_children(tree)
    
    # Définis le mot txt dans la grammaire.
    def txt(self, tree):
        print("debug : txt")
        print("-----------------")
        
        # De part le code dans tree.py, children est une liste d'éléments.
        # Ici, on est dans txt qui ne va pas se dériver autrement donc il y a qu'un seul fils.
        for elem in tree.children:
            self.myPrint.add(elem.value)
        
    # Définis le mot dumbo_bloc dans la grammaire.
    def dumbo_bloc(self, tree):
        print("debug : dumbo_bloc")
        print("-----------------")
        
        # Gérer le dumbo_bloc par rapport à un autre dumbo_bloc
        # --> créer un objet spécifique pour eux.
        self.visit_children(tree)

    # Définis le mot expresssion_list dans la grammaire.
    def expresssion_list(self, tree):
        print("debug : expresssion_list")
        print("-----------------")
        
        self.visit_children(tree)

    # Définis le mot expression dans la grammaire.
    def expression(self, tree):
        print("debug : expression")
        print("-----------------")
        
        
        expression = tree.children[0].data
        # tab_expr = ["for", ...] ou tab_expr = ["if", ...] ou
        # tab_expr = ["<variable>", ...] ou tab_expr = ["print", ...]
        if expression == "for_expr" or expression == "if_expr":
            self.scope.other.begin_insert(self.scope.dictio)
            self.visit_children(tree)
            self.scope.dictio = self.scope.other.begin_remove().data
        # cas assignement de variable ou print.
        else:
            self.visit_children(tree)

    # Définis le mot add_expr dans la grammaire.
    def add_expr(self, tree):
        print("debug : add_expr")
        print("-----------------")
        
        sum = tree.children[0].value + tree.children[2].value
        return sum

    # Définis le mot sub_expr dans la grammaire.
    def sub_expr(self, tree):
        print("debug : sub_expr")
        print("-----------------")
        
        sub = tree.children[0].value - tree.children[2].value
        return sub

    # Définis le mot mul_expr dans la grammaire.
    def mul_expr(self, tree):
        print("debug : mul_expr")
        print("-----------------")
        
        mul = tree.children[0].value * tree.children[2].value
        return mul

    # Définis le mot div_expr dans la grammaire.
    def div_expr(self, tree):
        print("debug : div_expr")
        print("-----------------")
        
        div = tree.children[0].value // tree.children[2].value
        return div

    # Définis le mot inf_expr dans la grammaire.
    def inf_expr(self, tree):
        print("debug : inf_expr")
        print("-----------------")
        
        flag = False
        if tree.children[0].data < tree.children[2].data:
            flag = True
        return flag

    # Définis le mot sup_expr dans la grammaire.
    def sup_expr(self, tree):
        print("debug : sup_expr")
        print("-----------------")
        flag = False
        left_member = 0
        right_member = 0
        while(type(tree.children[0]) is not Token and type(tree.children[1]) is not Token):
            tree.children[0] = self.visit_children(tree.children[0])
            tree.children[1] = self.visit_children(tree.children[1])
        if tree.children[0].data > tree.children[2].data:
            flag = True
        return flag

    # Définis le mot eq_expr dans la grammaire.
    def eq_expr(self, tree):
        print("debug : eq_expr")
        print("-----------------")
        
        flag = False
        if tree.children[0].data == tree.children[2].data:
            flag = True
        return flag

    # Définis le mot dif_expr dans la grammaire.
    def dif_expr(self, tree):
        print("debug : dif_expr")
        print("-----------------")
        
        flag = False
        if tree.children[0].data != tree.children[2].data:
            flag = True
        return flag

    def mul_int(self, tree):
        print("debug : mul_int")
        print("-----------------")
        
        mul = tree.children[0].value
        i = 0
        while tree.children[i] != None :
            if tree.children[i] == "*":
                mul = mul * tree.children[i+1].value
            else : 
                mul = mul / tree.children[i+1].value
            i += 2
        return mul
        
    def print_expr(self, tree):
        print("debug : print_expr")
        print("-----------------")
        res = self.visit_children(tree)[0]
        print(self.visit_children(tree))
        print("res = " + str(res))
        if res[0] == "'":
            self.myPrint.add(" " + res[1:-1] + " ")
        else:
            self.myPrint.add(" " + self.scope.search(res) + " ")

    def add_int(self, tree):
        print("debug : add_int")
        print("-----------------")
        
        sum = tree.children[0].value
        i = 1
        while tree.children[i] != None :
            if tree.children[i] == "+":
                sum = sum + tree.children[i+1].value
            else : 
                sum = sum - tree.children[i+1].value
            i += 2
        return sum

    # Définis le mot bool_expr dans la grammaire.
    def bool_expr(self, tree):
        print("debug : bool_expr")
        print("-----------------")
        
        tab_expr = tree.children
        flag = False
        if tab_expr.length == 1:
            if tab_expr[0]:
                flag = self.visit_children(tree)
            else:
                flag = self.visit_children(tree)
        else :
            flag = self.visit_children(tree)
        return flag

    # Définis le mot if_expr dans la grammaire.
    def if_expr(self, tree):
        print("debug : if_expr")
        print("-----------------")
        
        if self.visit_children(tree.children[0]):
            self.visit_children(tree.children[1])

    # Définis le mot for_expr dans la grammaire.
    def for_expr(self, tree):
        print("debug : for_expr")
        print("-----------------")
        var, liste_elem, liste_expr = tree.children
        for i in range(len(self.scope.search(liste_elem))):
            self.scope.add(var.value, self.scope.search(liste_elem)[i])
            self.visit_children(liste_expr)
            self.scope.dictio = self.scope.other.head.data

    # Définis le mot assign_expr dans la grammaire.
    def assign_expr(self, tree):
        print("debug : assign_expr")
        print("-----------------")
        self.visit_children(tree)

    # Définis le mot assign_expr_var dans la grammaire.
    def assign_expr_var(self, tree):
        print("debug : assign_expr_var")
        print("-----------------")
        
        liste = []
        next_tree = tree.children[1:]
        for elem in next_tree[0].children:
            if isinstance(elem, Tree.Tree):
                for string in elem.children:
                    liste.append(string.value[1:-1])
                self.scope.add(tree.children[0].value, liste)
            else:
                self.scope.add(tree.children[0].value, elem.value[1:-1])
    
    # Définis le mot assign_expr_arith dans la grammaire.
    def assign_expr_arith(self, tree):
        print("debug : assign_expr_arith")
        print("-----------------")
        print(tree.children[1])
        if (type(tree.children[1]) is Tree.Tree):
            self.scope.add(tree.children[0].value, self.visit(tree.children[1]))
        elif (len(tree.children[1]) == 1):
            self.scope.add(tree.children[0].value, tree.children[1].value)
        else:
            print("debug here (assign_expr_arith) : " + str(tree))
            pass
        

    # Définis le mot string_expression dans la grammaire.
    def string_expression(self, tree):
        print("debug : string_expression")
        print("-----------------")
        if (tree.data == "string_expression"):
            if (type(self.visit_children(tree)[0]) is list):
                return self.visit_children(tree)[0].value
            else:
                return self.visit_children(tree)[0]
        else:
            return tree.children[0].value

    # Définis le mot string_list dans la grammaire.
    def string_list(self, tree):
        print("debug : string_list")
        print("-----------------")
        return self.visit_children(tree)

    # Définis le mot string_list_interior dans la grammaire.
    def string_list_interior(self, tree):
        print("debug : string_list_interior")
        print("-----------------")
        
        liste = []
        for elem in tree.children:
            liste.append(elem.value)
        return liste

    # Définis le mot variable dans la grammaire.
    def variable(self, tree):
        print("debug : variable")
        print("-----------------")
        
        try :
            return tree.children[0].value
        except(UnexpectedToken) : 
            print("error " + file + ":", file=sys.stderr)

    # Définis le mot string dans la grammaire.
    def string(self, tree):
        print("debug : string")
        print("-----------------")
        try :
            return tree.children[0].value
        except(UnexpectedToken) : 
            print("error " + file + ":", file=sys.stderr)
        
    # Définis le mot boolean dans la grammaire.  
    def boolean(self, tree):
        print("debug : boolean")
        print("-----------------")
        
        try :
            return tree.children[0].value
        except(UnexpectedToken) : 
            print("error " + file + ":", file=sys.stderr)
            
            
# Classe pour mettre en évidence l'erreur lors de l'interprétation.
class InterpreterError(Exception):
    
    # Construit notre message d'erreur.
    def __init__(self, file, tree, message):
        super(InterpreterError, self).__init__(file + " " + self.get_line_number(tree) + ": " + message)

    # Recupère la ligne ainsi que la colonne de l'erreur.
    def get_line_number(self, tree):
        return "ligne " + str(tree.line) + ", colonne " + str(tree.column) + "."

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
                    result = OurInterpreter(scope).display(tree,)
                    if result is not None:
                        print(result, end = "")
                # Exception qu'il peut y avoir (mauvais caractère ou mauvaise interprétation)
                except UnexpectedToken as e:
                    print("error " + file + ":", file=sys.stderr)
                    raise
                except InterpreterError as e:
                    print(e, file=sys.stderr)