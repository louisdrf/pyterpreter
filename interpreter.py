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
    a=2;
    clement=3;
    
    if(a==1) {
        print(1);
        print(16);
    }
    else if(a==0) {
        print(17);
    }
    else if(a==2) {
        print(2);
        print(clement);
    }
    else {
        print(15);
    }
}
'''
parser.parse(s)
