from env_const import globals as g
from env_const import colors

    
def push_and_execute(stack, inst):
        stack.append(inst)
        print('stack: ', stack)
        print('evalInst: ', inst)
        evalInst(inst)
        
        if inst[0] == 'return':
            return 
        else:
            if stack[-1] != 'main':
                stack.pop()
            
        
def empty_function_call(stack, fname):
    nbInstToPop = 0
    inst = stack.pop() # pop du return
    for inst in stack:
        if inst[0] != 'call' and inst[1] != fname:
            nbInstToPop+=1
        else:
            break
        
    if nbInstToPop != len(stack):
        for _ in range(nbInstToPop):
            stack.pop()
           


def evalInst(t):
    
    
    if t[0] == 'start':
        for function_def in t[1]:
             evalInst(function_def)
        print(g.functions)
        evalInst(('main', t[2])) # évaluer le main
        
         
    if t[0]=='main':
        main_linst = t[1]
        g.stack.append('main')
        i = 0
        
        while i < len(main_linst):
            push_and_execute(g.stack, main_linst[i])
            i+=1
        
        g.stack.pop()
            
            
    if t[0] == 'linst':
        for inst in t[1]:
            push_and_execute(g.stack, inst)
            if g.current_return_val:
                break
                   
    if t[0]=='print' :
        print(evalExpr(t[1]))
        
    if t[0] == 'sprint':
        print(f"{colors.blue}{t[1]}{colors.reset}")
            
    if t[0]=='assign' :
        variable, expression = t[1], t[2]
         
        if len(t) > 3:
           g.names[(variable, t[3])]=evalExpr(expression) # déclaration de paramètre dans une fonction 
        else:
            scope = g.current_function if (variable, g.current_function) in g.names or g.current_function else "global"
            g.names[(variable, scope)]=evalExpr(expression)   
             
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
        while evalExpr(t[1]):                          # condition
            push_and_execute(g.stack, ('linst', t[2])) # linst
                
    if t[0]=='for':
        push_and_execute(g.stack, t[1])      # assign
        while evalExpr(t[2]):                # condition
            push_and_execute(g.stack, ('linst', t[4]))  # linst
            push_and_execute(g.stack, t[3])  # increment
      

        
    if t[0]=='function':
        g.current_return_val = None
        ftype, function_name, params, instructions = t[1], t[2], t[3], t[4]
        
        g.functions[function_name] = {'params': params, 'instructions': instructions}
        
        if ftype =='val':
            g.functions[function_name]['return_val'] = True
        else:
            g.functions[function_name]['return_val'] = False
            
        if len(params) > 0: # Si la fonction a des paramètres à déclarer
           for param in params:
                push_and_execute(g.stack, ('assign', param, 0, function_name))
                
    
    if t[0] == 'return':
        if t[1] != None:
            g.current_return_val = evalExpr(t[1])
        else:
            g.current_return_val = "none"
        
        
                 
    if t[0]=='call':
        g.current_return_val = None
        fname  = t[1]
        params = t[2]
        return_value = False
        
        if len(t) == 4:
            return_value = t[3]
        
        if fname in g.functions:
            function = g.functions[fname]
            
            for i in range(len(function['params'])):
                g.names[ function['params'][i], fname ] = evalExpr(params[i]) 
                
            g.current_function = fname
            
            for inst in function['instructions']:
                push_and_execute(g.stack, inst)
                if g.current_return_val:
                    if g.current_return_val != "none": # return avec valeur
                        if return_value == False:
                            raise ValueError(f"Erreur: La fonction {fname} n'a pas été appelée de la bonne manière.") 
                        if function['return_val'] == False:
                            raise ValueError(f"Erreur: La fonction {fname} est une fonction void et ne devrait pas retourner de valeur.") 
                        else:
                            empty_function_call(g.stack, fname)
                            break
                    elif g.current_return_val == "none": # return sans valeur
                        if return_value == True:
                            raise ValueError(f"Erreur: La fonction {fname} n'a pas été appelée de la bonne manière.") 
                        if function['return_val'] == True:
                            raise ValueError(f"Erreur: La fonction {fname} est une fonction val et devrait retourner de valeur.") 
                        else:
                            empty_function_call(g.stack, fname)
                            break
               
            g.current_function = ""
            
        else:
            raise ValueError(f"Erreur: La fonction {fname} n'a pas été déclarée") 
   
   
    if t[0] == 'assign_array':
         variable, array_values = t[1], t[2]
         array_values_evaluated = []
        
         for expression in array_values:
             array_values_evaluated.append(evalExpr(expression))
         
         if len(t) > 3:
            g.names[(variable, t[3])] = array_values_evaluated # déclaration de paramètre dans une fonction 
         else:
             scope = g.current_function if (variable, g.current_function) in g.names or g.current_function else "global"
             g.names[(variable, scope)] = array_values_evaluated
            
         
    if t[0] == 'push':
        array_name, expression = t[1], t[2]
        value_to_push = evalExpr(expression)
        array = evalExpr(array_name)
        if isinstance(array, list):
                array.append(value_to_push)
        else:
            raise ValueError(f"Erreur: la variable {array_name} n'est pas un tableau")
        
    if t[0] == 'pop':
        array_name = t[1]
        array = evalExpr(array_name)
        if isinstance(array, list):
            if len(array) > 0:
                array.pop()
            else:
                raise ValueError(f"Erreur: impossible de pop sur un tableau vide")
        else:
            raise ValueError(f"Erreur: la variable {array_name} n'est pas un tableau")
    
    if t[0] == 'insert':
        array, index, value = evalExpr(t[1]), evalExpr(t[2]), evalExpr(t[3])
        if isinstance(array, list):
            if index >= 0 and index < len(array):
                array.insert(index, value)
            else:
                raise ValueError(f"Erreur: impossible d'accéder à cet index pour le tableau")
        else:
            raise ValueError(f"Erreur: la variable {array} n'est pas un tableau")
        
    if t[0] == 'concat':
        array1, array2 = evalExpr(t[1]), evalExpr(t[2])      
        if isinstance(array1, list) and isinstance(array2, list):
            array1 += array2
        else:
            raise ValueError(f"Erreur: Impossible de concaténer deux éléments qui ne sont pas des tableaux")
        
    if t[0] == 'merge_and_sort':
        array1, array2 = evalExpr(t[1]), evalExpr(t[2])      
        if isinstance(array1, list) and isinstance(array2, list):
            array1 += array2
            array1 = array1.sort()
        else:
            raise ValueError(f"Erreur: Impossible de fusionner deux éléments qui ne sont pas des tableaux")
        
                    

def evalExpr(t):
    print('evalExpr', t)
    if type(t) == bool:
        return t
    if type(t) == int or type(t) == list:
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
        
        elif t[0] == 'call_function':
            fname = t[1]
            if g.functions[fname]['return_val'] and g.functions[fname]['return_val'] == True:
                push_and_execute(g.stack, ('call', fname, t[2], True))
                
                if g.current_return_val == None:
                    raise ValueError(f"Erreur: La fonction {fname} ne retourne pas de valeur")
                return g.current_return_val
            else:
                raise ValueError(f"Erreur: La fonction {fname} est void et ne doit donc pas retourner de valeur")
        
        elif t[0] == 'get_array_cell':
            array_name, index = t[1], evalExpr(t[2])
            array = evalExpr(array_name)
            if isinstance(array, list):
                if index >= 0 and index < len(array):
                    return array[index]
                else:
                    raise ValueError(f"Erreur: impossible d'accéder à cet index pour le tableau")
            else:
                raise ValueError(f"Erreur: la variable {array_name} n'est pas un tableau")

        elif t[0] == 'get_array_length':
            array_name = t[1]
            array = evalExpr(array_name)
            if isinstance(array, list):
                    return len(array)
            else:
                raise ValueError(f"Erreur: la variable {array_name} n'est pas un tableau")
            
        else:
            print(f"Error: Unknown operator '{t[0]}'")
            return None
    else:
        print(f"Error: Unknown expression type {type(t)}")
        return None
