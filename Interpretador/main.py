

#Para rodar execute : python3 main.py[nome do arquivo que vai rodar] example/sum.tiny[nome do path que vai para o argv]



from sys import argv

import os

import sys



from Syntatical import *


print("Hi I'm the print in the main")


print(argv[1])


lexeme = Lexeme()


analyzeLex = LexicalAnalyzer(argv[1])



# lexeme = analyze.nextToken()

fileTokens = analyzeLex.TinyAutomata()
for i in fileTokens:
    print(i.word)

last = fileTokens[-1]
if(last == 'TT_INVALID_TOKEN' or last == 'TT_UNEXPECTED_EOF'):
    print(f'ERRO NO ARQUIVO sum.tiny!! \n\n {last}')
else:
    print('CONTINUAMOS DAQUI!!')

s = SyntaticAnalyzer(analyzeLex)

print(analyzeLex.nameOfFile)

TinyCommands = s.Start()


os.system('clear')

TinyCommands.execute()

# for i in TinyCommands.comandos():
#     print(i)

# for i in TinyCommands.comandos():
#     print(i.execute())

#Executa todos os comandos do script interpretado

    


#Implementar analizador sintático
#Implementar a interpretação


# print()
# print(analyze.nextToken().word)
# print(analyze.nextToken().word)
# print(analyze.nextToken().word)
# print(analyze.nextToken().word)
# print(analyze.nextToken().word)
# print(analyze.nextToken().word)
# print(analyze.nextToken().word)
# print(analyze.nextToken().word)
# print(analyze.nextToken().word)
# print(analyze.nextToken().word)
# print(analyze.nextToken().word)
# print(analyze.nextToken().word)
# print(analyze.nextToken().word)
# print(analyze.nextToken().word)
# print(analyze.nextToken().word)
# exit()


# print(lista)

# lex = Lexeme()

# LexicalAnalyzer l(a[1])

# except:
#     print("Deu ruim")