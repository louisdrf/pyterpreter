# from genereTreeGraphviz2 import printTreeGraph

#####################################################################
from lexer_rules import *
from parser_rules import *

import ply.lex as lex
lexer = lex.lex()

import ply.yacc as yacc
parser = yacc.yacc()


s = '''
def val lagourmande(b) {
    return 5*b;
}

def val lafameuse(a,b) {
    return a*b;
}

def void unefonction(a,b) {
    print(a*b);
    print(a-b);
    return;
    print(121);
}

def void main() {
    a = lagourmande(lafameuse(1, 2));
    print(a);
    unefonction(10,20);
}
'''
parser.parse(s)
