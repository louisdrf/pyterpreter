from evalInst import evalInst

# Parsing rules
precedence = (
    ('left', 'OR', 'AND'),
    ('left', 'EQUALS', 'LOWER', 'HIGHER', 'HIGHEQUAL', 'LOWEQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)


def p_start(t):
    ''' start : linst'''
    t[0] = ('start',t[1])
    print(t[0])
    # printTreeGraph(t[0])
    evalInst(t[1])
    
   
               

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
    '''inst : IF LPAREN condition RPAREN b_bloc
            | IF LPAREN condition RPAREN b_bloc else'''
    if(len(t) > 6):
        t[0] = ('if', t[3], t[5], t[6])
    else:
        t[0] = ('if', t[3], t[5])
    

def p_expression_else(t):
    '''else : ELSE inst
            | ELSE b_bloc'''
    t[0] = t[2]
    
    
def p_expression_condition(t):
    '''condition : expression EQUALS expression
                 | expression LOWER expression
                 | expression HIGHER expression
                 | expression HIGHEQUAL expression
                 | expression LOWEQUAL expression
                 | expression OR expression
                 | expression AND expression'''
    t[0] = (t[2],t[1],t[3])


############################ OPERATIONS ###################################

def p_expression_operator(t):
    '''expression : expression operator expression'''
    t[0] = (t[2],t[1],t[3])


############################ FONCTIONS ###################################

def p_statement_return(t):
    '''inst : RETURN expression COLON
            | RETURN condition COLON'''
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
                   | '''
    
    if len(t) == 1:
        t[0] = []
    elif len(t) == 2:    
        t[0] = [t[1]]
    else:
        new_param, param_list = t[1], t[3]
        param_list.append(new_param)
        t[0] = param_list


def p_expression_params(t):
    '''params : NAME COMMA params 
              | NAME
              | '''
    if len(t) == 1:
        t[0] = []
    elif len(t) == 2:
        t[0] = [t[1]]
    else:
        new_param, param_list = t[1], t[3]
        param_list.append(new_param)
        t[0] = param_list
    
    
def p_statement_print(t):
    'inst : PRINT LPAREN expression RPAREN COLON' 
    t[0] = ('print', t[3])
    
def p_statement_print_string(t):
    'inst : SPRINT LPAREN STRING RPAREN COLON' 
    t[0] = ('sprint', t[3])
  
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
      
def p_expression_true(t):
    'expression : TRUE'
    t[0] = True
    
def p_expression_false(t):
    'expression : FALSE'
    t[0] = False
    
def p_expression_name(t):
    'expression : NAME'
    t[0] = t[1]

def p_expression_inverse(t):
    'expression : MINUS expression'
    t[0] = ('-', t[2])
    
    
def p_expression_array(t):
    'array : LSQBRACKET call_params RSQBRACKET'
    t[0] = ('array', t[2])
    
    
def p_error(t):
    print("Syntax error at '%s'" % t.value)