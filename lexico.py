from ply import lex

# Lista de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Regras de extensões regulares para tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore = ' \t'


# Regra para tratar números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regra para tratar erros
def t_error(t):
    print("Caracter irregular: ", t.value[0])
    t.lexer.skip(1)


# Construir o lexer
lexer = lex.lex()

# Testar o lexer
data = '3 + 4 * 10'
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

