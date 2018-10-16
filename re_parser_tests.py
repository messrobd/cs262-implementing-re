import ply.lex as lex
import ply.yacc as yacc
import re_lexer
import re_parser
import re

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ]
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type, tok.value]
  return result

def test_parser(input_string):
    lexer.input(input_string)
    parse_tree = parser.parse(input_string,lexer=lexer)
    return parse_tree

lexer = lex.lex(module=re_lexer)
parser = yacc.yacc(module=re_parser)

# character & operator regexps

a = 'a'
b = 'B'
num = '5'
string = 'aB5'
star = '*'
pipe = '|'
l = '('
r = ')'

print test_lexer(a)
print test_parser(a)

ch = r'[a-zA-Z0-9]'
#print re.findall(ch, string) == ['a', 'B', '5']
print test_lexer(string)
print test_parser(string)

multiplier = r'\*'
#print re.findall(multiplier, star) == ['*']
print test_lexer(star)

disjunction = r'\|'
#print re.findall(disjunction, pipe) == ['|']
print test_lexer(pipe)

lparen = r'\('
#print re.findall(lparen, l) == ['(']
print test_lexer(l)

rparen = r'\)'
#print re.findall(rparen, r) == [')']
print test_lexer(r)

a_star = 'a*'
print test_parser(a_star)

a_or_b = 'a|b'
print test_parser(a_or_b)

a_or_b_star = '(a|b)*'
print test_parser(a_or_b_star)

a_b_star_c = 'a(b*)c'
print test_lexer(a_b_star_c)
