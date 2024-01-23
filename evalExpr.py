import evalInst
from env_const import *

def evalExpr(t):
    print('evalExpr', t)
    if type(t) == bool:
        return t
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
            if len(t) > 2:
                return evalExpr(t[1]) - evalExpr(t[2])
            else:
                return (-1) * evalExpr(t[1])
        # Condition
        elif t[0] == '==':
            return evalExpr(t[1]) == evalExpr(t[2])
        elif t[0] == '<':
            return evalExpr(t[1]) < evalExpr(t[2])
        elif t[0] == '>':
            return evalExpr(t[1]) > evalExpr(t[2])
        elif t[0] == '<=':
            return evalExpr(t[1]) <= evalExpr(t[2])
        elif t[0] == '>=':
            return evalExpr(t[1]) >= evalExpr(t[2])
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
