from env_const import globals as g
from env_const import colors

    
def push_and_execute(stack, inst):
            stack.append(inst)
            # print(stack)
            print('evalInst: ', inst)
            evalInst(inst)
            stack.pop()

def evalInst(t):
    
    if g.current_return_val and g.current_function:
        return
    
    if type(t) != tuple : 
        return
    
    if t[0] == 'start':
        for function_def in t[1]:
             evalInst(function_def)
        evalInst(t[2]) # évaluer le main
        
         
    if t[0]=='main':
        main_linst = t[1]
        g.stack.append('main')
        i = 0
        
        while len(g.stack) > 0:
            if i < len(main_linst):
                push_and_execute(g.stack, main_linst[i])
                i+=1
            else:
                g.stack.pop()
            
            
    if t[0] == 'linst':
        for inst in t[1]:
           push_and_execute(g.stack, inst)
            
        
                        
    if t[0]=='print' :
        print(evalExpr(t[1]))
        
    if t[0] == 'sprint':
        print(f"{colors.blue}{t[1]}{colors.reset}")
            
    if t[0]=='assign' :
        if len(t) > 3:
            g.names[(t[1], t[3])]=evalExpr(t[2]) 
        else:
            scope = g.current_function if (t[1], g.current_function) in g.names or g.current_function else "global"
            g.names[(t[1], scope)]=evalExpr(t[2])
            
    if t[0] == 'multiple_assign':
        variables, values = t[1], t[2]
        if len(variables) != len(values) or len(values) == 0:
            raise ValueError(f"Erreur: le nombre de valeurs ne correspond pas au nombre de variables")
        else:    
            for i in range(0, len(variables)):
               scope = g.current_function if (variables[i], g.current_function) in g.names or g.current_function else "global"
               g.names[(variables[i], scope)]=evalExpr(values[i]) 
            
        

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
        condition, inst_if = t[1], t[2]

        if evalExpr(condition): 
            push_and_execute(g.stack, ('linst', inst_if))
        else:
            if(len(t) == 4):
                inst_else = t[3]
                if inst_else[0] == 'if':
                    push_and_execute(g.stack, (inst_else))
                else:
                    push_and_execute(g.stack, ('linst', inst_else))
        
        
    if t[0]=='while':
        while evalExpr(t[1]):  # condition
            evalInst(('linst', t[2]))     # instructions
    
    if t[0]=='for':
        evalInst(t[1])          # assign
        while evalExpr(t[2]):   # condition
            evalInst(('linst', t[3]))      # linst
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
    # print('evalExpr', t)
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
        elif t[0] == '%':
            return evalExpr(t[1]) % evalExpr(t[2])
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
