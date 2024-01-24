from env_const import globals as g

def evalInst(t):

    if g.current_return_val and g.current_function:
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
        
    if t[0] == 'sprint':
        print(f"{t[1]}")
            
    if t[0]=='assign' :
        if len(t) > 3:
            g.names[(t[1], t[3])]=evalExpr(t[2]) 
        else:
            scope = g.current_function if (t[1], g.current_function) in g.names else "global"
            g.names[(t[1], scope)]=evalExpr(t[2])

    if t[0]=='increment':
        scope = g.current_function if (t[1], g.current_function) in g.names else "global"
        g.names[(t[1], scope)] += 1
        
    if t[0]=='decrement':
        scope = g.current_function if (t[1], g.current_function) in g.names else "global"
        g.names[(t[1], scope)] -= 1
        
    if t[0]=='operator_assign':
        scope = g.current_function if (t[1], g.current_function) in g.names else "global"

        if t[2]=='+':
            g.names[(t[1], scope)] += evalExpr(t[3])
        elif t[2]=='-':
            g.names[(t[1], scope)] -= evalExpr(t[3])
        elif t[2]=='/':
            g.names[(t[1], scope)] /= evalExpr(t[3])
        elif t[2]=='*':
            g.names[(t[1], scope)] *= evalExpr(t[3])
            
    if t[0]=='if' : 
        condition, inst_if, inst_else = t[1], t[2], t[3]
        
        if(len(t) == 3): # if there's not else
            if evalExpr(condition): 
                evalInst(inst_if)
        else:
            if evalExpr(condition):
                evalInst(inst_if)
            else:
                evalInst(inst_else)   
        
        
    if t[0]=='while':
        while evalExpr(t[1]):  # condition
            evalInst(t[2])     # instructions
    
    if t[0]=='for':
        evalInst(t[1])          # assign
        while evalExpr(t[2]):   # condition
            evalInst(t[3])      # linst
            evalInst(t[4])      # increment
      
    
    if t[0] == 'return':
       g.current_return_val = evalExpr(t[1])
        
        
    if t[0]=='function':
        function_name, params, instructions = t[1], t[2], t[3]
        
        g.functions[function_name] = {'params': params, 'instructions': instructions}
        if len(params) > 0: # Si la fonction a des paramètres à déclarer
            for param in params:
                evalInst(('assign', param, 0, function_name))
                         
    if t[0]=='call':
        g.current_return_val = None
        fname  = t[1]
        params = t[2]
        
        if fname in g.functions:
            function = g.functions[fname]
            
            for i in range(len(function['params'])):
                g.names[ function['params'][i], fname ] = evalExpr(params[i]) 
                
            g.current_function = fname
            evalInst(function['instructions'])
            g.current_function = ""
            
        else:
            raise ValueError(f"Erreur: La fonction {fname} n'a pas été déclarée") 
   

def evalExpr(t):
    print('evalExpr', t)
    if type(t) == bool:
        return t
    if type(t) == int:
        return t  
    elif type(t) == str:
        if (t, g.current_function) in g.names: # On vérifie si une variable locale existe
            return g.names[(t, g.current_function)]
        elif (t, "global") in g.names:
            return g.names[(t, "global")]
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
            return g.current_return_val
            
        else:
            print(f"Error: Unknown operator '{t[0]}'")
            return None
    else:
        print(f"Error: Unknown expression type {type(t)}")
        return None
