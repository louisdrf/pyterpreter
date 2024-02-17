# from genereTreeGraphviz2 import printTreeGraph

#####################################################################
from lexer_rules import *
from parser_rules import *

import ply.lex as lex
lexer = lex.lex()

import ply.yacc as yacc
parser = yacc.yacc()


s = '''

def void main() {
    a = [1,2,3];
    z = 2;
    b = a[z];
    print(b);
}
'''
parser.parse(s)
