class Colors:
        def __init__(self):
         self.blue = '\033[94m'
         self.red = '\033[91m'
         self.reset = '\033[0m' 

class Globals: 
    
   def __init__(self):
        self.names = {}
        self.functions = {}
        self.current_function = ""
        self.current_return_val = None
        self.stack = []
        
        
globals = Globals()
colors = Colors()
