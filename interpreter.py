# from genereTreeGraphviz2 import printTreeGraph

#####################################################################
from lexer_rules import *
from parser_rules import *

import ply.lex as lex
lexer = lex.lex()

import ply.yacc as yacc
parser = yacc.yacc()


s = '''

def val mafonction() {
    return [1,2,3];
}

def val get_tab() {
    return mafonction();
}

def void main() {
    a = get_tab();
    print(a);
}
'''
parser.parse(s)
