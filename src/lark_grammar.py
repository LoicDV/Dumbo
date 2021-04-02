from lark import Lark

grammar = """
start: add_expr
     | sub_expr
     | WORD*
     | STRING
     | list_word

add_expr: (FLOAT "+" FLOAT) | (INT "+" INT)
sub_expr: (FLOAT "-" FLOAT) | (INT "-" INT)

////// VARIABLES
%import common.WORD
STRING: "'" WORD (" " WORD)* "'"

// LIST_WORD
list_word: "(" STRING (", " STRING)* ")"

////// NUMBERS
%import common.INT
%import common.FLOAT

%ignore " " 
"""

parser = Lark(grammar)

def main():
    print(parser.parse("1+1"))
    print(parser.parse("2-1"))
    print(parser.parse("3.1 - 2.1"))
    print(parser.parse("test de test"))
    print(parser.parse("'test de test'"))
    print(parser.parse(" "))
    print(parser.parse("( 'test', 'testb')"))

if __name__ == '__main__':
    main()