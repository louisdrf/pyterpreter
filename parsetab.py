
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftEQUALSLOWERHIGHERleftPLUSMINUSleftTIMESDIVIDEAND COLON DIVIDE EQUAL EQUALS FOR HIGHER IF LBRACKET LOWER LPAREN MINUS NAME NUMBER OR PLUS PRINT RBRACKET RPAREN THEN TIMES WHILE start : linstlinst : linst inst \n            | inst inst : increment COLONinst : add_assign COLONincrement : NAME PLUS PLUSadd_assign : NAME PLUS EQUAL expressioninst : assign COLONassign : NAME EQUAL expressioninst : whileinst : forwhile : WHILE LPAREN condition RPAREN b_blocfor : FOR LPAREN assign COLON condition COLON increment RPAREN b_blocinst : ifif : IF LPAREN condition RPAREN b_bloccondition : expression EQUALS expression\n                 | expression LOWER expression\n                 | expression HIGHER expression\n                 | expression OR expression\n                 | expression AND expressionexpression : expression PLUS expressionexpression : expression TIMES expressionexpression : expression DIVIDE expressionexpression : expression MINUS expressioninst : PRINT LPAREN expression RPAREN COLONb_bloc : LBRACKET linst RBRACKETexpression : LPAREN expression RPARENexpression : NUMBERexpression : NAME'
    
_lr_action_items = {'PRINT':([0,2,3,7,8,9,15,16,17,18,53,58,59,66,67,69,74,],[10,10,-3,-10,-11,-14,-2,-4,-5,-8,-25,-12,10,-15,10,-26,-13,]),'NAME':([0,2,3,7,8,9,15,16,17,18,19,21,22,23,24,25,30,39,40,41,42,45,46,47,48,49,50,53,58,59,66,67,68,69,74,],[11,11,-3,-10,-11,-14,-2,-4,-5,-8,28,28,28,35,28,28,28,28,28,28,28,28,28,28,28,28,28,-25,-12,11,-15,11,71,-26,-13,]),'WHILE':([0,2,3,7,8,9,15,16,17,18,53,58,59,66,67,69,74,],[12,12,-3,-10,-11,-14,-2,-4,-5,-8,-25,-12,12,-15,12,-26,-13,]),'FOR':([0,2,3,7,8,9,15,16,17,18,53,58,59,66,67,69,74,],[13,13,-3,-10,-11,-14,-2,-4,-5,-8,-25,-12,13,-15,13,-26,-13,]),'IF':([0,2,3,7,8,9,15,16,17,18,53,58,59,66,67,69,74,],[14,14,-3,-10,-11,-14,-2,-4,-5,-8,-25,-12,14,-15,14,-26,-13,]),'$end':([1,2,3,7,8,9,15,16,17,18,53,58,66,69,74,],[0,-1,-3,-10,-11,-14,-2,-4,-5,-8,-25,-12,-15,-26,-13,]),'RBRACKET':([3,7,8,9,15,16,17,18,53,58,66,67,69,74,],[-3,-10,-11,-14,-2,-4,-5,-8,-25,-12,-15,69,-26,-13,]),'COLON':([4,5,6,27,28,29,31,34,38,43,52,54,55,56,57,60,61,62,63,64,65,],[16,17,18,-28,-29,-6,-9,50,53,-7,-27,-21,-22,-23,-24,-16,-17,-18,-19,-20,68,]),'LPAREN':([10,12,13,14,19,21,22,24,25,30,39,40,41,42,45,46,47,48,49,50,],[19,22,23,24,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'PLUS':([11,20,26,27,28,31,33,37,43,52,54,55,56,57,60,61,62,63,64,71,73,],[20,29,39,-28,-29,39,39,39,39,-27,-21,-22,-23,-24,39,39,39,39,39,73,29,]),'EQUAL':([11,20,35,],[21,30,21,]),'NUMBER':([19,21,22,24,25,30,39,40,41,42,45,46,47,48,49,50,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'RPAREN':([26,27,28,29,32,36,37,52,54,55,56,57,60,61,62,63,64,70,],[38,-28,-29,-6,44,51,52,-27,-21,-22,-23,-24,-16,-17,-18,-19,-20,72,]),'TIMES':([26,27,28,31,33,37,43,52,54,55,56,57,60,61,62,63,64,],[40,-28,-29,40,40,40,40,-27,40,-22,-23,40,40,40,40,40,40,]),'DIVIDE':([26,27,28,31,33,37,43,52,54,55,56,57,60,61,62,63,64,],[41,-28,-29,41,41,41,41,-27,41,-22,-23,41,41,41,41,41,41,]),'MINUS':([26,27,28,31,33,37,43,52,54,55,56,57,60,61,62,63,64,],[42,-28,-29,42,42,42,42,-27,-21,-22,-23,-24,42,42,42,42,42,]),'EQUALS':([27,28,33,52,54,55,56,57,],[-28,-29,45,-27,-21,-22,-23,-24,]),'LOWER':([27,28,33,52,54,55,56,57,],[-28,-29,46,-27,-21,-22,-23,-24,]),'HIGHER':([27,28,33,52,54,55,56,57,],[-28,-29,47,-27,-21,-22,-23,-24,]),'OR':([27,28,33,52,54,55,56,57,],[-28,-29,48,-27,-21,-22,-23,-24,]),'AND':([27,28,33,52,54,55,56,57,],[-28,-29,49,-27,-21,-22,-23,-24,]),'LBRACKET':([44,51,72,],[59,59,59,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'linst':([0,59,],[2,67,]),'inst':([0,2,59,67,],[3,15,3,15,]),'increment':([0,2,59,67,68,],[4,4,4,4,70,]),'add_assign':([0,2,59,67,],[5,5,5,5,]),'assign':([0,2,23,59,67,],[6,6,34,6,6,]),'while':([0,2,59,67,],[7,7,7,7,]),'for':([0,2,59,67,],[8,8,8,8,]),'if':([0,2,59,67,],[9,9,9,9,]),'expression':([19,21,22,24,25,30,39,40,41,42,45,46,47,48,49,50,],[26,31,33,33,37,43,54,55,56,57,60,61,62,63,64,33,]),'condition':([22,24,50,],[32,36,65,]),'b_bloc':([44,51,72,],[58,66,74,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> linst','start',1,'p_start','interpreter.py',77),
  ('linst -> linst inst','linst',2,'p_line','interpreter.py',161),
  ('linst -> inst','linst',1,'p_line','interpreter.py',162),
  ('inst -> increment COLON','inst',2,'p_statement_increment','interpreter.py',174),
  ('inst -> add_assign COLON','inst',2,'p_statement_add_assign','interpreter.py',178),
  ('increment -> NAME PLUS PLUS','increment',3,'p_expression_increment','interpreter.py',183),
  ('add_assign -> NAME PLUS EQUAL expression','add_assign',4,'p_expression_add_assign','interpreter.py',187),
  ('inst -> assign COLON','inst',2,'p_statement_assign','interpreter.py',195),
  ('assign -> NAME EQUAL expression','assign',3,'p_expression_assign','interpreter.py',200),
  ('inst -> while','inst',1,'p_statement_while','interpreter.py',207),
  ('inst -> for','inst',1,'p_statement_for','interpreter.py',211),
  ('while -> WHILE LPAREN condition RPAREN b_bloc','while',5,'p_expression_while','interpreter.py',216),
  ('for -> FOR LPAREN assign COLON condition COLON increment RPAREN b_bloc','for',9,'p_expression_for','interpreter.py',220),
  ('inst -> if','inst',1,'p_statement_condition','interpreter.py',226),
  ('if -> IF LPAREN condition RPAREN b_bloc','if',5,'p_expression_if','interpreter.py',231),
  ('condition -> expression EQUALS expression','condition',3,'p_expression_condition','interpreter.py',236),
  ('condition -> expression LOWER expression','condition',3,'p_expression_condition','interpreter.py',237),
  ('condition -> expression HIGHER expression','condition',3,'p_expression_condition','interpreter.py',238),
  ('condition -> expression OR expression','condition',3,'p_expression_condition','interpreter.py',239),
  ('condition -> expression AND expression','condition',3,'p_expression_condition','interpreter.py',240),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop_plus','interpreter.py',247),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop_times','interpreter.py',252),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop_divide','interpreter.py',257),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop_minus','interpreter.py',262),
  ('inst -> PRINT LPAREN expression RPAREN COLON','inst',5,'p_statement_print','interpreter.py',269),
  ('b_bloc -> LBRACKET linst RBRACKET','b_bloc',3,'p_expression_bracket_bloc','interpreter.py',275),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','interpreter.py',279),
  ('expression -> NUMBER','expression',1,'p_expression_number','interpreter.py',283),
  ('expression -> NAME','expression',1,'p_expression_name','interpreter.py',287),
]
