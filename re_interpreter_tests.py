import ply.lex as lex
import ply.yacc as yacc
import re_lexer
import re_parser
from re_interpreter import interpret

lexer = lex.lex(module=re_lexer)
parser = yacc.yacc(module=re_parser)

abc = 'abc'
ast = parser.parse(abc, lexer=lexer)
print interpret(ast)

astar = 'a*'
ast = parser.parse(astar, lexer=lexer)
#print interpret(ast)
