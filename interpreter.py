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
    b = [2,4,1];
    merge_and_sort(a,b);
    print(a);
}
'''
parser.parse(s)
