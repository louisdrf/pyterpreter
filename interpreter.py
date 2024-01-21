# from genereTreeGraphviz2 import printTreeGraph
             
reserved = {
   'if'      : 'IF',
   'then'    : 'THEN',
   'print'   : 'PRINT',
   'while'   : 'WHILE',
   'for'     : 'FOR',
   'function': 'FUNCTION', 
   'return'  : 'RETURN'
}


tokens = [
    'NAME','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE', 
    'LPAREN','RPAREN', 'LBRACKET', 'RBRACKET', 'COLON', 'COMMA',
    'AND', 'OR', 'EQUAL', 'EQUALS', 'LOWER','HIGHER'
    ] + list(reserved.values())

# Tokens
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUAL   = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_COLON   = r';'
t_COMMA   = r','
t_AND     = r'\&'
t_OR      = r'\|'
t_EQUALS  = r'=='
t_LOWER   = r'\<'
t_HIGHER  = r'\>'

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
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex() 



# Parsing rules
precedence = (
    ('left', 'OR', 'AND'),
    ('left', 'EQUALS', 'LOWER', 'HIGHER'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)


def p_start(t):
    ''' start : linst'''
    t[0] = ('start',t[1])
    print(t[0])
    # printTreeGraph(t[0])
    evalInst(t[1])
    
    
    
names = {}
functions = {}
current_function = ""
current_return_val = None

def evalInst(t):
    global current_function
    global current_return_val
    
    if current_return_val is not None and current_function:
        return
    
    print('evalInst', t)
    if type(t)!=tuple : 
        print('warning')
        return
    
    if t[0]=='bloc' :
            evalInst(t[1])
            evalInst(t[2])
    
    
    if t[0]=='print' :
        print(evalExpr(t[1]))
        
    if t[0]=='assign' :
        if len(t) > 3:
            names[(t[1], t[3])]=evalExpr(t[2]) 
        else:
            scope = current_function if (t[1], current_function) in names else "global"
            names[(t[1], scope)]=evalExpr(t[2])

    if t[0]=='increment':
        scope = current_function if (t[1], current_function) in names else "global"
        names[(t[1], scope)] += 1
        
    if t[0]=='decrement':
        scope = current_function if (t[1], current_function) in names else "global"
        names[(t[1], scope)] -= 1
        
    if t[0]=='operator_assign':
        scope = current_function if (t[1], current_function) in names else "global"

        if t[2]=='+':
            names[(t[1], scope)] += evalExpr(t[3])
        elif t[2]=='-':
            names[(t[1], scope)] -= evalExpr(t[3])
        elif t[2]=='/':
            names[(t[1], scope)] /= evalExpr(t[3])
        elif t[2]=='*':
            names[(t[1], scope)] *= evalExpr(t[3])
            
    if t[0]=='if' : 
        if evalExpr(t[1]):
            evalInst(t[2])
        
    if t[0]=='while':
        while evalExpr(t[1]):  # condition
            evalInst(t[2])     # instructions
    
    if t[0]=='for':
        evalInst(t[1])          # assign
        while evalExpr(t[2]):   # condition
            evalInst(t[3])      # linst
            evalInst(t[4])      # increment
      
    
    if t[0] == 'return':
       current_return_val = evalExpr(t[1])
        
        
    if t[0]=='function':
        function_name, params, instructions = t[1], t[2], t[3]
        
        functions[function_name] = {'params': params, 'instructions': instructions}
        if len(params) > 0: # Si la fonction a des paramètres à déclarer
            for param in params:
                evalInst(('assign', param, 0, function_name))
                         
    if t[0]=='call':
        current_return_val = None
        fname  = t[1]
        params = t[2]
    
        if fname in functions:
            function = functions[fname]
            
            for i in range(len(function['params'])):
                names[ function['params'][i], fname ] = evalExpr(params[i]) 
                
            current_function = fname
            evalInst(function['instructions'])
            current_function = ""
            
        else:
            raise ValueError(f"Erreur: La fonction {fname} n'a pas été déclarée") 
       
        
               
def evalExpr(t):
    print('evalExpr', t)
    if type(t) == int:
        return t  
    elif type(t) == str:
        if (t, current_function) in names: # On vérifie si une variable locale existe
            return names[(t, current_function)]
        elif (t, "global") in names:
            return names[(t, "global")]
        else:
            print(f"Error: Variable '{t}' not found")
            return None
        
    elif type(t) == tuple:
        if   t[0] == '+':
            return evalExpr(t[1]) + evalExpr(t[2])
        elif t[0] == '*':
            return evalExpr(t[1]) * evalExpr(t[2])
        elif t[0] == '/':
            return evalExpr(t[1]) / evalExpr(t[2])
        elif t[0] == '-':
            return evalExpr(t[1]) - evalExpr(t[2])
        # Condition
        elif t[0] == '==':
            return evalExpr(t[1]) == evalExpr(t[2])
        elif t[0] == '<':
            return evalExpr(t[1]) < evalExpr(t[2])
        elif t[0] == '>':
            return evalExpr(t[1]) > evalExpr(t[2])
        elif t[0] == 'and':
            return evalExpr(t[1]) and evalExpr(t[2])
        elif t[0] == 'or':
            return evalExpr(t[1]) or evalExpr(t[2])
        
        elif t[0] == 'call_value':
            evalInst(('call', t[1], t[2]))
            return current_return_val
            
        else:
            print(f"Error: Unknown operator '{t[0]}'")
            return None
    else:
        print(f"Error: Unknown expression type {type(t)}")
        return None

def p_line(t):
    '''linst : linst inst 
            | inst '''
    if len(t) == 3 :
        t[0] = ('bloc',t[1], t[2])
    else:
        t[0] = ('bloc',t[1], 'empty')



############################ INCREMENTATIONS ###################################

# statements 
def p_statement_increment_decrement(t):
    '''inst : increment COLON
            | decrement COLON'''
    t[0] = t[1]

def p_statement_add_assign(t):
    'inst : operator_assign COLON'
    t[0] = t[1]   

# expressions   
def p_expression_increment(t):
    'increment : NAME PLUS PLUS'
    t[0] = ('increment', t[1])
    
def p_expression_decrement(t):
    'decrement : NAME MINUS MINUS'
    t[0] = ('decrement', t[1])
 
def p_expression_operator_assign(t):
    'operator_assign : NAME operator EQUAL expression'
    t[0] = ('operator_assign', t[1], t[2], t[4])
    
    
############################ ASSIGN ###################################

# statements
def p_statement_assign(t):
    'inst : assign COLON'
    t[0] = t[1]
    
# expressions
def p_expression_assign(t):
    'assign : NAME EQUAL expression'
    t[0] = ('assign', t[1], t[3])


############################ BOUCLES ###################################

# statements
def p_statement_while(t):
    'inst : WHILE LPAREN condition RPAREN b_bloc'
    t[0] = ('while', t[3], t[5])
    
def p_statement_for(t):
    '''inst : FOR LPAREN assign COLON condition COLON increment RPAREN b_bloc
    | FOR LPAREN assign COLON condition COLON operator_assign RPAREN b_bloc
    | FOR LPAREN assign COLON condition COLON decrement RPAREN b_bloc'''
    t[0] = ('for', t[3], t[5], t[7], t[9])
      
########################## CONDITIONS #####################################

def p_expression_if(t):
    'inst : IF LPAREN condition RPAREN b_bloc'
    t[0] = ('if', t[3], t[5])
    
    
def p_expression_condition(t):
    '''condition : expression EQUALS expression
                 | expression LOWER expression
                 | expression HIGHER expression
                 | expression OR expression
                 | expression AND expression'''
    t[0] = (t[2],t[1],t[3])


############################ OPERATIONS ###################################

def p_expression_operator(t):
    '''expression : expression operator expression'''
    t[0] = (t[2],t[1],t[3])


############################ FONCTIONS ###################################

def p_statement_return(t):
    'inst : RETURN expression COLON'
    t[0] = ('return', t[2])
   
# déclarer une fonction 
def p_statement_function(t):                
    'inst : FUNCTION NAME LPAREN params RPAREN b_bloc'
    t[0] = ('function', t[2], t[4], t[6]) 
    
# appeler une fonction qui retourne une valeur
def p_statement_call_function_value(t):
    'expression : NAME LPAREN call_params RPAREN'
    t[0] = ('call_value', t[1], t[3])


# appeler une fonction void
def p_statement_call_function_void(t):
    'inst : NAME LPAREN call_params RPAREN COLON'
    t[0] = ('call', t[1], t[3])
    
    
def p_expression_call_params(t):
    '''call_params : expression COMMA call_params 
                   | expression
                   | empty_params'''
    
    if len(t) == 2:
        if t[1] == []:
            t[0] = []
        else:
            t[0] = [t[1]]
    else:
        new_param, param_list = t[1], t[3]
        param_list.append(new_param)
        t[0] = param_list


def p_expression_params(t):
    '''params : NAME COMMA params 
              | NAME
              | empty_params'''
    if len(t) == 2:
        if t[1] == []:
            t[0] = []
        else:
            t[0] = [t[1]]
    else:
        new_param, param_list = t[1], t[3]
        param_list.append(new_param)
        t[0] = param_list
    
def p_statement_print(t):
    'inst : PRINT LPAREN expression RPAREN COLON' 
    t[0] = ('print',t[3])
  
############################ EXPRESSIONS ###################################

def p_expression_bracket_bloc(t):
    'b_bloc : LBRACKET linst RBRACKET'
    t[0] = t[2]
    
       
def p_operator(t):
    '''operator : PLUS
                | MINUS
                | DIVIDE
                | TIMES'''
    t[0] = t[1]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)
 
def p_expression_empty_params(t):
    'empty_params :'
    t[0] = []   

#####################################################################

import ply.yacc as yacc
parser = yacc.yacc()

s = '''
function test(a, b) {
    return a + b;
}

function test2(i) {
    print(16);
    for(a = 0; a < 10; a++) {
        i+=2;
    }
    return i;
    print(17);
}

x = test(10, 5);
y = test2(0);
print(x-1);
print(y);
'''

   
parser.parse(s)
