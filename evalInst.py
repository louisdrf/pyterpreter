from evalExpr import evalExpr
from env_const import *

def evalInst(t):
    global current_function
    global current_return_val
    
    if current_return_val and current_function:
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
        print(f"{Color.BLUE}{t[1]}{Color.RESET}")
            
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
   