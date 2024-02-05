# from genereTreeGraphviz2 import printTreeGraph

#####################################################################
from lexer_rules import *
from parser_rules import *

import ply.lex as lex
lexer = lex.lex()

import ply.yacc as yacc
parser = yacc.yacc()


s = '''
def main() {
    clement = 3;
   for(i=0; i < clement; i++) {
       print(i);
   }
   i=0;
   while(i<clement) {
       print(clement);
       i++;
   }
}
'''
parser.parse(s)
