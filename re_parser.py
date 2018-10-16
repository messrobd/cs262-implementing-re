from re_lexer import tokens

'''
required grammar:

expression => regexp expression
regexp => CH
regexp => regexp *
regexp => regexp | regexp
regexp => ( regexp )                '''

start = 'expression'

def p_exp(p):
    'expression : regexp expression'
    p[0] = [p[1]] + p[2]

def p_exp_last(p):
    'expression : regexp'
    p[0] = [p[1]]

def p_regexp_ch(p):
    'regexp : CHARACTER'
    p[0] = ('character', p[1])

def p_regexp_multiplier(p):
    'regexp : regexp MULTIPLIER'
    p[0] = ('multiplier', p[1])

def p_regexp_disjunction(p):
    'regexp : regexp DISJUNCTION regexp'
    p[0] = ('disjunction', p[1], p[3])

def p_regexp_group(p):
    'regexp : LPAREN regexp RPAREN'
    p[0] = ('group', p[2])
