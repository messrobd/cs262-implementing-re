from re_lexer import tokens

'''
required grammar:

regexp => CH regexp
regexp => CH
regexp => regexp *
regexp => regexp | regexp
regexp => ( regexp )                '''

start = 'regexp'

def p_regexp(p):
    'regexp : regexp regexp'
    p[0] = p[1] + p[2]

def p_regexp_ch(p):
    'regexp : CHARACTER'
    p[0] = [('character', p[1])]
