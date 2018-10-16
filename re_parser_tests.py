import ply.lex as lex
import re_lexer
import re

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ]
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type, tok.value]
  return result

lexer = lex.lex(module=re_lexer)

# character & operator regexps

a = 'a'
b = 'B'
num = '5'
string = 'aB5'
star = '*'
pipe = '|'
l = '('
r = ')'

ch = r'[a-zA-Z0-9]'
#print re.findall(ch, string) == ['a', 'B', '5']
print test_lexer(a)
print test_lexer(string)

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

simple_re = 'a(b*)c'
print test_lexer(simple_re)
