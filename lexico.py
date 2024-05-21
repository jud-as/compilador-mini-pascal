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
    'ID',
    'ASSIGN',
    'EQUAL',
    'NOTEQUAL',
    'LESS',
    'GREATER',
    'LESSEQUAL',
    'GREATEREQUAL',
    'SEMICOLON',
    'STRING',
)

# Palavras reservadas

reserved = {
    'begin': 'BEGIN',
    'end': 'END',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'true': 'TRUE',
    'false': 'FALSE',
}

tokens = tokens + tuple(reserved.values())

# Regras de extensões regulares para tokens

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r':='
t_EQUAL = r'='
t_NOTEQUAL = r'<>'
t_LESS = r'<'
t_GREATER = r'>'
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='
t_SEMICOLON = r';'
t_ignore = ' \t'


# Regra para tratar identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Regra para tratar números

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'\'[^\'\n]*\''
    t.value = str(t.value)
    return t

# Regra para tratar comentários
def t_COMMENT(t):
    r'\{.*\}'
    pass


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

