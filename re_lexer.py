import ply.lex as lex

'''
required tokens:

single character [a-zA-Z0-9]
* operator
| operator
() grouping '''

tokens = (
    'CHARACTER',
    'MULTIPLIER',
    'DISJUNCTION',
    'LPAREN',
    'RPAREN'
)

def t_CHARACTER(token):
    r'[a-zA-Z0-9]'
    return token

def t_MULTIPLIER(token):
    r'\*'
    return token

def t_DISJUNCTION(token):
    r'\|'
    return token

def t_LPAREN(token):
    r'\('
    return token

def t_RPAREN(token):
    r'\)'
    return token
