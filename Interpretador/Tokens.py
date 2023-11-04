from enum import Enum

Tokens = Enum(
        'TokenType', 
        {
          'ERRT_UNEXPECTED_EOF': "", 'ERRT_END_OF_FILE': "\n", 'ST_SEMICOLON': ";"
        , 'ST_ASSIGN': "=", 'ST_EQUAL': "==", 'ST_NOT_EQUAL': "!="
        , 'ST_SEMICOLON': ";", 'ST_LOWER': "<", 'ST_LOWER_EQUAL': "<="
        , 'ST_GREATER': ">", 'ST_GREATER_EQUAL': ">=", 'AT_ADD': "+"
        , 'AT_SUB': "-", 'AT_MUL': "*", 'AT_DIV': "/"
        , 'AT_MOD': "%", 'KT_PROGRAM': "program", 'KT_WHILE': "while"
        , 'KT_DO': "do", 'KT_DONE': "done", 'KT_IF': "if"
        , 'KT_THEN': "then", 'KT_ELSE': "else", 'KT_OUTPUT': "output"
        , 'KT_TRUE': "true", 'KT_FALSE': "false", 'KT_READ': "read"
        , 'KT_NOT': "not", 'OT_VAR': "variable",
        'NUMBER' : "0",
        'NUMBER' : "1",
        'NUMBER' : "2",
        'NUMBER' : "3",
        'NUMBER' : "4",
        'NUMBER' : "5",
        'NUMBER' : "6",
        'NUMBER' : "7",
        'NUMBER' : "8",
        'NUMBER' : "9"
        }
    )

def InsideTokenScope(token):
  return token in [i.value for i in Tokens]

def EquivalentSymbol(token):
  for i in Tokens:
    if i.value == token:
      return i.name  
  return 'OT_VAR'

