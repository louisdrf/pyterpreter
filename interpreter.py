# from genereTreeGraphviz2 import printTreeGraph

#####################################################################
from lexer_rules import *
from parser_rules import *

import ply.lex as lex
lexer = lex.lex()

import ply.yacc as yacc
parser = yacc.yacc()

s = '''
function test(a, b, c) {
    print(12);
}

x = test(1, 2, 3);
'''

   
parser.parse(s)
