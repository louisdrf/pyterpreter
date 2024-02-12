# from genereTreeGraphviz2 import printTreeGraph

#####################################################################
from lexer_rules import *
from parser_rules import *

import ply.lex as lex
lexer = lex.lex()

import ply.yacc as yacc
parser = yacc.yacc()


s = '''

def fonction(a) {
    if(a == 2) {
        return a;
    }
    return 1;
}

def main() {
    a = fonction(1);
    print(a);
}
'''
parser.parse(s)
