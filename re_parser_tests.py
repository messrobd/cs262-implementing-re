import ply.lex as lex
import re_lexer

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ]
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [tok.type, tok.value]
  return result

lexer = lex.lex(module=re_lexer)

test = 'a(b*)c'
