import unittest
from dumbo import *

class DumboTester(unittest.TestCase):
    
    def testPrintSimple(self):
        # Print string.
        tree = langage.parse("{{ print 'test'; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "test")
        # Print variable string.
        tree = langage.parse("{{ a := 'test'; print a; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "test")
        # Print int.
        tree = langage.parse("{{ print 4; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "4")
        # Print variable int.
        tree = langage.parse("{{ a := 4; print a; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "4")
        # Print concaténation.
        tree = langage.parse("{{ print 'cou'.'cou'; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "coucou")
        # Print variable concaténation.
        tree = langage.parse("{{ a := 'cou'.'cou'; print a; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "coucou")

    def testIfRéussi(self):
        # If réussi avec boolean.
        tree = langage.parse("{{ if true do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec variables.
        tree = langage.parse("{{ a := true; if a do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec And et boolean.
        tree = langage.parse("{{ if true and true do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec Or et 2 boolean true.
        tree = langage.parse("{{ if true or true do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec Or et boolean true et false.
        tree = langage.parse("{{ if true or false do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec 2 And et boolean.
        tree = langage.parse("{{ if true and true and true do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec 2 Or et boolean true.
        tree = langage.parse("{{ if true or true or true do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec 2 Or et boolean true et false.
        tree = langage.parse("{{ if false or false or true do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec 1 And, 1 Or et boolean true.
        tree = langage.parse("{{ if true and true or true do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec 1 And, 1 Or et boolean true et false.
        tree = langage.parse("{{ if true and true or false do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ if true and false or true do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ if true or false and true do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ if true or false and true do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ if false or true and true do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec <.
        tree = langage.parse("{{ if 1 < 2 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec < avec variable.
        tree = langage.parse("{{ a := 1; if a < 2 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec < et calcul.
        tree = langage.parse("{{ if 0 + 1 < 2 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ if 0 + 1 < 4 / 2 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ if 0 + 1 * 0 < 4 / 2 + 1 * 6 - 4 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec < et calcul et variable.
        tree = langage.parse("{{ a := 0 + 1; if a < 2 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 0 + 1; if a < 4 / 2 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 0 + 1 * 0; if a < 4 / 2 + 1 * 6 - 4 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 0 + 1; if a + 1 < 2 + 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 0 + 1; if a + 1 < 4 / 2 + 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 0 + 1 * 0; if a * 1 + 1 < 4 / 2 + 1 * 6 - 4 + 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec >.
        tree = langage.parse("{{ if 2 > 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec > avec variable.
        tree = langage.parse("{{ a := 2; if a > 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec > et calcul.
        tree = langage.parse("{{ if 2 > 0 + 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ if 4 / 2 > 0 + 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ if 4 / 2 + 1 * 6 - 4 > 0 + 1 * 0 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec > et calcul et variable.
        tree = langage.parse("{{ a := 2; if a > 0 + 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 4 / 2; if a > 0 + 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 4 / 2 + 1 * 6 - 4; if a > 0 + 1 * 0 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 2; if a + 1 > 0 + 1 + 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 4 / 2; if 1 + a > 0 + 1 + 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 4 / 2 + 1 * 6 - 4; if 1 * a > 0 + 1 * 0 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec ==.
        tree = langage.parse("{{ if 1 == 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec == avec variable.
        tree = langage.parse("{{ a := 1; if a == 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec == avec calcul.
        tree = langage.parse("{{ if 0 + 1 == 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ if 0 + 1 == 0 + 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ if 0 + 1 * 0 + 0 == 1 * 0 + 1 - 1 * 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec == avec calcul avec variable.
        tree = langage.parse("{{ a := 0 + 1; if a == 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 0 + 1; if a == 0 + 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 0 + 1 * 0 + 0; if a == 1 * 0 + 1 - 1 * 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 0 + 1; if a + 1 == 1 + 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 0 + 1; if a + 1 == 0 + 1 + 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 0 + 1 * 0 + 0; if a * 1 == 1 * 0 + 1 - 1 * 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec !=.
        tree = langage.parse("{{ if 0 != 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec != avec variable.
        tree = langage.parse("{{ a := 0; if a != 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec != avec calcul.
        tree = langage.parse("{{ if 0 + 0 != 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ if 0 + 1 != 0 + 3 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ if 0 + 1 * 0 + 0 + 1 != 1 * 0 + 1 - 1 * 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        # If réussi avec != avec calcul avec variable.
        tree = langage.parse("{{ a := 0 + 0; if a != 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 0 + 1; if a != 0 + 3 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 0 + 1 * 0 + 0 + 1; if a != 1 * 0 + 1 - 1 * 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 0; if a + 0 != 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 0; if a + 1 != 0 + 3 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
        tree = langage.parse("{{ a := 0; if a + 1 * 0 + 0 + 1 != 1 * 0 + 1 - 1 * 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "yes")
    
    def testIfRaté(self):
        # If raté avec boolean.
        tree = langage.parse("{{ if false do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        # If raté avec And et boolean true et false.
        tree = langage.parse("{{ if true and false do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        # If raté avec Or et 2 boolean true et false.
        tree = langage.parse("{{ if false and false do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        # If raté avec Or et 2 boolean.
        tree = langage.parse("{{ if false or false do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        # If raté avec 2 And et boolean true et false.
        tree = langage.parse("{{ if false and true and true do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        tree = langage.parse("{{ if true and false and true do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        tree = langage.parse("{{ if true and true and false do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        tree = langage.parse("{{ if false and false and false do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        # If raté avec 2 Or et boolean.
        tree = langage.parse("{{ if false or false or false do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        # If raté avec 1 And, 1 Or et boolean true.
        tree = langage.parse("{{ if true and false or false do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        tree = langage.parse("{{ if false and false or false do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        tree = langage.parse("{{ if false and true or false do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        # If raté avec <.
        tree = langage.parse("{{ if 2 < 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        # If raté avec < et calcul.
        tree = langage.parse("{{ if 2 + 1 < 2 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        tree = langage.parse("{{ if 0 + 1 < 2 / 2 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        tree = langage.parse("{{ if 4 / 2 + 1 * 6 - 4 < 0 + 1 * 0 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        # If raté avec >.
        tree = langage.parse("{{ if 2 > 3 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        # If raté avec > et calcul.
        tree = langage.parse("{{ if 2 > 0 + 1 * 2  do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        tree = langage.parse("{{ if 4 / 2 - 2 > 0 + 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        tree = langage.parse("{{ if 0 + 1 * 0 > 4 / 2 + 1 * 6 - 4 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        # If raté avec ==.
        tree = langage.parse("{{ if 2 == 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        # If raté avec == avec calcul.
        tree = langage.parse("{{ if 0 + 1 == 3 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        tree = langage.parse("{{ if 0 + 1 == 0 + 1 * 2 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        tree = langage.parse("{{ if 0 + 1 * 0 + 0 + 4 == 1 * 0 + 1 - 1 * 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        # If raté avec !=.
        tree = langage.parse("{{ if 0 != 0 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        # If raté avec != avec calcul.
        tree = langage.parse("{{ if 0 + 0 != 0 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        tree = langage.parse("{{ if 0 + 1 * 2 != 0 + 3 - 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")
        tree = langage.parse("{{ if 0 + 1 * 0 + 0 != 1 * 0 + 1 - 1 * 1 do print 'yes'; endif; }}")
        self.assertEqual(OurInterpreter(scope).display(tree), "")

if __name__ == '__main__':
    with open(".\src\lark_grammar.lark", "r") as grammar_file:
        grammar = grammar_file.read()
        scope = Scope()
        langage = Lark(grammar, start='programme', parser="lalr")
        unittest.main()