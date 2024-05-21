from ply import lex

# Lista de tokens
tokens = (
    'NUMBER',
    'REAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
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
    'COLON',
    'PERIOD',
    'LKEY',
    'RKEY',
    'DOUBLEBAR',
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
    'for': 'FOR',
    'repeat': 'REPEAT',
    'until': 'UNTIL',
    'function': 'FUNCTION',
    'procedure': 'PROCEDURE',
}

tokens = tokens + tuple(reserved.values())

# Regras de extensões regulares para tokens

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_ASSIGN = r':='
t_EQUAL = r'='
t_NOTEQUAL = r'<>'
t_LESS = r'<'
t_GREATER = r'>'
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='
t_SEMICOLON = r';'
t_COLON = r':'
t_PERIOD = r'\.'
t_DOUBLEBAR = r'//'
t_ignore = ' \t'


# Regra para tratar identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    if t.type == 'BOOLEAN':
        t.value = True if t.value == 'true' else False
    return t

# Regra para tratar números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regra para tratar números reais
def t_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Regra para tratar strings
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


