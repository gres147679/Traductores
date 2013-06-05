
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '@Zi$,\xca\x17\xb5D\x05c&NK\x84\xff'
    
_lr_action_items = {'TYPEDEF_INT':([14,],[18,]),'INST_DECLARE':([2,7,15,],[5,5,5,]),'SEMICOLON':([3,10,11,18,19,20,21,],[-6,-7,15,-11,-8,-13,-12,]),'TYPEDEF_RANGE':([14,],[20,]),'TYPEDEF_BOOL':([14,],[21,]),'VAR_IDENTIFIER':([5,13,],[8,8,]),'INST_END':([3,10,11,12,18,19,20,21,22,],[-6,-7,-4,16,-11,-8,-13,-12,-5,]),'INST_AS':([8,9,17,],[-9,14,-10,]),'COMMA':([8,],[13,]),'INST_BEGIN':([2,],[7,]),'INST_PROGRAM':([0,],[2,]),'$end':([1,3,4,6,10,16,18,19,20,21,],[0,-6,-1,-3,-7,-2,-11,-8,-13,-12,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Inst_Declare':([2,7,15,],[3,3,3,]),'Tipo':([14,],[19,]),'Bloque_Inst':([2,],[4,]),'program':([0,],[1,]),'Inst':([2,7,15,],[6,11,11,]),'Lista_Variables':([5,13,],[9,17,]),'Lista_Declare':([5,],[10,]),'Lista_Inst':([7,15,],[12,22,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> INST_PROGRAM Bloque_Inst','program',2,'p_program','parser.py',14),
  ('Bloque_Inst -> INST_BEGIN Lista_Inst INST_END','Bloque_Inst',3,'p_Bloque_Inst','parser.py',19),
  ('Bloque_Inst -> Inst','Bloque_Inst',1,'p_Bloque_Inst','parser.py',20),
  ('Lista_Inst -> Inst','Lista_Inst',1,'p_Lista_Inst','parser.py',27),
  ('Lista_Inst -> Inst SEMICOLON Lista_Inst','Lista_Inst',3,'p_Lista_Inst','parser.py',28),
  ('Inst -> Inst_Declare','Inst',1,'p_Inst','parser.py',35),
  ('Inst_Declare -> INST_DECLARE Lista_Declare','Inst_Declare',2,'p_Inst_Declare','parser.py',47),
  ('Lista_Declare -> Lista_Variables INST_AS Tipo','Lista_Declare',3,'p_Lista_Declare','parser.py',51),
  ('Lista_Variables -> VAR_IDENTIFIER','Lista_Variables',1,'p_Lista_Variables','parser.py',55),
  ('Lista_Variables -> VAR_IDENTIFIER COMMA Lista_Variables','Lista_Variables',3,'p_Lista_Variables','parser.py',56),
  ('Tipo -> TYPEDEF_INT','Tipo',1,'p_Tipo','parser.py',64),
  ('Tipo -> TYPEDEF_BOOL','Tipo',1,'p_Tipo','parser.py',65),
  ('Tipo -> TYPEDEF_RANGE','Tipo',1,'p_Tipo','parser.py',66),
]
