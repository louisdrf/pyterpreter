from evals import *

# Parsing rules
precedence = (
    ('left', 'OR', 'AND'),
    ('left', 'EQUALS', 'LOWER', 'HIGHER', 'HIGHEQUAL', 'LOWEQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO')
)

def p_start(t):
    '''start : function_list main 
             | main'''
    if len(t) == 2:
        evalInst(('main', t[1]))
    else:
        evalInst(('start', t[1], t[2]))
   

def p_linst(t):
    '''linst : linst inst 
            | inst '''
    if len(t) == 2:
        t[0] = [t[1]] 
    else:
        t[1].append(t[2])
        t[0] = t[1]  



############################ STACK ET MAIN ###################################

def p_statement_main(t):                
    'main : FUNCTION VOID MAIN LPAREN RPAREN b_bloc'
    t[0] = t[6] 



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
    

############################ TABLEAUX ###################################

def p_statement_assign_array(t):
    'inst : assign_array COLON'
    t[0] = t[1]
    
def p_expression_assign_array(t):
     'assign_array : NAME EQUAL new_array'
     t[0] = ('assign_array', t[1], t[3])

def p_expression_array(t):
     'new_array : LHOOK array_values RHOOK'
     t[0] = t[2]
     
    
def p_expression_array_values(t):
    '''array_values : expression COMMA array_values
                    | expression
                    | '''
    if len(t) == 1:
        t[0] = []
    elif len(t) == 2:
        t[0] = [t[1]]
    else:
        new_value, values_list = t[1], t[3]
        values_list.insert(0, new_value)  
        t[0] = values_list
         
         
         
############################ FONCTIONS SUR LES TABLEAUX ###################################


def p_expression_get_array_cell(t):
    'expression : NAME LHOOK expression RHOOK'
    t[0] = ('get_array_cell', t[1], t[3])
   

def p_expression_get_array_length(t):
    '''expression : LENGTH LPAREN NAME RPAREN
                  | LENGTH LPAREN new_array RPAREN'''
    t[0] = ('get_array_length', t[3])     
    

def p_statement_push_in_array(t):
    'inst : NAME DOT PUSH LPAREN expression RPAREN COLON' 
    t[0] = ('push', t[1], t[5])         

def p_statement_pop_in_array(t):
    'inst : NAME DOT POP LPAREN RPAREN COLON' 
    t[0] = ('pop', t[1])    
    
def p_statement_insert_in_array(t):
    'inst : NAME DOT INSERT LPAREN expression COMMA expression RPAREN COLON'
    t[0] = ('insert', t[1], t[5], t[7])
    

def p_statement_concat_arrays(t):
    '''inst : NAME DOT CONCAT LPAREN NAME RPAREN COLON
            | NAME DOT CONCAT LPAREN new_array RPAREN COLON'''
    t[0] = ('concat', t[1], t[5])
    
def p_statement_merge_and_sort_arrays(t):
    'inst : MERGE_AND_SORT LPAREN NAME COMMA NAME RPAREN COLON'
    t[0] = ('merge_and_sort', t[3], t[5])
    
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
            | RETURN condition COLON
            | RETURN new_array COLON
            | RETURN COLON'''
    if len(t) == 3:
        t[0] = ('return', None)
    else:
        t[0] = ('return', t[2])

def p_expression_ftype(t):
    '''ftype : VAL
             | VOID'''
    t[0] = t[1]
   
# déclarer plusieurs fonctions
def p_statements_prototypes(t):
    '''function_list : function_list function
                     | function'''
    if len(t) == 2:
        t[0] = [t[1]] 
    else:
        t[1].append(t[2])
        t[0] = t[1] 
    
    
# déclarer une fonction 
def p_statement_function(t):                
    'function : FUNCTION ftype NAME LPAREN params RPAREN b_bloc'
    t[0] = ('function', t[2], t[3], t[5], t[7]) 
    
# appeler une fonction qui retourne une valeur
def p_statement_call_function_value(t):
    'expression : NAME LPAREN call_params RPAREN'
    t[0] = ('call_function', t[1], t[3])

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
                | TIMES
                | MODULO'''
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
    
def p_statement_multiple_assign(t):
    'inst : params EQUAL multiple_values COLON'
    t[0] = ('multiple_assign', t[1], t[3])  
  
def p_expression_multiple_values(t):
    '''multiple_values : expression
                       | expression COMMA multiple_values'''
    if len(t) == 1:
        t[0] = []
    elif len(t) == 2:
        t[0] = [t[1]]
    else:
        new_param, param_list = t[1], t[3]
        param_list.append(new_param)
        t[0] = param_list  
 
    
def p_error(t):
    print("Syntax error at '%s'" % t.value)