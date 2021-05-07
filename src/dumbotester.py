import unittest
from dumbo import *

class DumboTester(unittest.TestCase):
    def testPrintSimple(self):
        # Print string
        tree = langage.parse("{{ print 'a'; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "a")
        # Print variable
        tree = langage.parse("{{ a := 'test'; print a; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "test")

if __name__ == '__main__':
    with open(".\src\lark_grammar.lark", "r") as grammar_file:
        grammar = grammar_file.read()
        scope = Scope()
        langage = Lark(grammar, start='programme', parser="lalr")
        unittest.main()