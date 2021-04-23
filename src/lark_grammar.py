from lark import Lark

grammar = """
start: programme

add_expr: (FLOAT "+" FLOAT) | (INT "+" INT)
sub_expr: (FLOAT "-" FLOAT) | (INT "-" INT)
mul_expr: (FLOAT "*" FLOAT) | (INT "*" INT)
div_expr: (FLOAT "/" "1".."9") | (INT "/" "1".."9")
inf_expr: (INT "<" INT)
sup_expr: (INT ">" INT)
eq_expr: (INT "=" INT)
dif_expr: (INT "!=" INT)

programme: txt | txt programme
programme: dumbo_bloc | dumbo_bloc programme

txt: [a-zA-Z0-9;&<>"_-.\>\n\p:,]+

dumbo_bloc: "{{" expression_list "}}"
expression_list: expression ";" expression_list | expression ";"
expression: (add_expr | sub_expr | mul_expr | div_expr)
expression: "print" string_expression 
expression: "for" variable "in" (string_list | variable) "do" expression_list "endfor"
expression: variable ":=" (string_expression | string_list)
expression: "if" (boolean | inf_expr | sup_expr | eq_expr | dif_expr) (operator bool_expr)* "do" expression_list "endif"
bool_expr: boolean | inf_expr | sup_expr | eq_expr | dif_expr | bool_expr
string_expression: string | variable | string_expression "." string_expression
string_list: "(" string_list_interior ")"
string_list_interior: string | string "," string_list_interior
variable: CNAME
boolean: "true" | "false"
operator: "or" | "and"
string: "'" (WORD | INT) ((" ")* (WORD | INT))* "'"

%import common.INT
%import common.FLOAT
%import common.NUMBER
%import common.WORD
%import common.CNAME
%ignore " " 
"""

parser = Lark(grammar)

def main():
    print(parser.parse("1+1"))
    print(parser.parse("2-1"))
    print(parser.parse("3.1 - 2.1"))
    print(parser.parse("test de test"))
    print(parser.parse("'test de test'"))
    print(parser.parse("'test de 4'"))
    print(parser.parse(" "))
    print(parser.parse("('test', 'testb')"))
    print(parser.parse("test := '4'"))

if __name__ == '__main__':
    main()