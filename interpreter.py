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
    print(5);
    print(6+1);
    a = 2;
    b = (a+a);
    sprint("test");
    if(a==1) {
        print(1);
        print(2);
        print(3);
    }
    else {
        print(5);
    }
}
'''
parser.parse(s)
