reserved = {
   'if'      : 'IF',
   'else'    : 'ELSE',
   'print'   : 'PRINT',
   'while'   : 'WHILE',
   'for'     : 'FOR',
   'def'     : 'FUNCTION', 
   'return'  : 'RETURN',
   'sprint'  : 'SPRINT',
   'true'    : 'TRUE',
   'false'   : 'FALSE',
   'main'    : 'MAIN',
   'val'     : 'VAL',
   'void'    : 'VOID',
   'len'     : 'LENGTH',
   'push'    : 'PUSH',
   'pop'     : 'POP',
   'insert'  : 'INSERT',
   'concat'  : 'CONCAT',
   'merge_sort': 'MERGE_AND_SORT'
}


tokens = [
    'NAME','NUMBER','STRING',
    'PLUS','MINUS','TIMES','DIVIDE', 'MODULO',
    'LPAREN','RPAREN', 'LBRACKET', 'RBRACKET', 'LHOOK', 'RHOOK', 'COLON', 'COMMA', 'DOT',
    'AND', 'OR', 'EQUAL', 'EQUALS', 'LOWER','HIGHER', 'HIGHEQUAL', 'LOWEQUAL',
    ] + list(reserved.values())


# Tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_MODULO    = r'%'
t_EQUAL     = r'='
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACKET  = r'\{'
t_RBRACKET  = r'\}'
t_LHOOK     = r'\['
t_RHOOK     = r'\]'
t_COLON     = r';'
t_COMMA     = r','
t_DOT       = r'.'
t_AND       = r'\&'
t_OR        = r'\|'
t_EQUALS    = r'=='
t_LOWER     = r'\<'
t_HIGHER    = r'\>'
t_HIGHEQUAL = r'\>='
t_LOWEQUAL  = r'\<='


def t_STRING(t):
    r'\"[^\"]*\"' 
    t.value = t.value[1:-1]
    return t

def t_TRUE(t):
    r'true'
    t.value = True
    return t

def t_FALSE(t):
    r'false'
    t.value = False
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
