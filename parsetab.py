
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'expressionCHARACTER DISJUNCTION LPAREN MULTIPLIER RPARENexpression : regexp expressionexpression : regexpregexp : CHARACTERregexp : regexp MULTIPLIER'
    
_lr_action_items = {'$end':([1,2,3,4,5,],[-2,-3,0,-1,-4,]),'CHARACTER':([0,1,2,5,],[2,2,-3,-4,]),'MULTIPLIER':([1,2,5,],[5,-3,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'regexp':([0,1,],[1,1,]),'expression':([0,1,],[3,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> regexp expression','expression',2,'p_exp','re_parser.py',15),
  ('expression -> regexp','expression',1,'p_exp_last','re_parser.py',19),
  ('regexp -> CHARACTER','regexp',1,'p_regexp_ch','re_parser.py',23),
  ('regexp -> regexp MULTIPLIER','regexp',2,'p_regexp_multiplier','re_parser.py',27),
]
