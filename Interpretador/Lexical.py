from io import UnsupportedOperation
from os import getcwd
from Lexeme import *

class LexicalAnalyzer:
    def __init__(self, nameOfFile):
        self.nameOfFile = nameOfFile
        self.SymbolTable = Tokens
        self.line = 0
        self.state = 1
        
        
        if nameOfFile == 1:
            print(f"\n ERRO! \n Reveja os argumentos passados para open() ou para o construtor de objetos de LexicalAnalyzer \n\n\t erro")
            exit()
            
        else:
            a = open(nameOfFile, 'r+')
            
            try:    
                self.file = open(nameOfFile, 'r+')
                self.sizeOfFile = self.file.__sizeof__()/10
            
            except FileNotFoundError as erro:
                print(f"\n ERRO! \n Opa! {nameOfFile} não pode ser encontrado no diretório {getcwd()} \n\n\t erro: {erro}")
                exit()
            
            except OSError as erro:
                print(f"\n ERRO! \n Reveja os argumentos passados para open() ou para o construtor de objetos de LexicalAnalyzer \n\n\t erro {erro}")
                exit()

    # def Walkthroughself.states(self, actually_self.state, char):
    #     if actually_self.state == 1:
        
    #     elif actually_self.state == 2:
    #         if char == '==' :
            
    #     elif actually_self.state == 3:
        
    #     elif actually_self.state == 4:
            
    #     elif actually_self.state == 5:
        
    #     elif actually_self.state == 6:
        
    #     else:
    #         return
                
    def EOF(char, fileP):
        return(char!='')
    

    def TinyAutomata(self):
        self.state = 1
        sizeAux = 0
        content = ''
        expression = ''
        punchcard = []
        tokensCard = []
        
        # while sizeAux <= self.sizeOfFile:
        #     sizeAux+=1
            # punchcard.append(self.file.read(1))

        # punchcard = self.file.readlines()

        while True:
            
            auxChar = self.file.read(1)
            punchcard.append(auxChar)
            
            if not auxChar:
                break

        print(punchcard)
        print(tokensCard)
        
        the_lexeme = Lexeme()
        
        i=0 

        while i < len(punchcard):
            if self.state == 1:
                if punchcard[i] == ' ' or punchcard[i] == '\t' or punchcard[i] == '\r':
                    self.state = 1
                    
                elif punchcard[i] == '\n':
                    self.line += 1
                    self.state = 1
                
                elif punchcard[i] == '#':
                    self.state = 2

                elif punchcard[i] == '=' or punchcard[i] == '<' or punchcard[i] == '>':
                    the_lexeme.token +=punchcard[i]
                    self.state = 3
                    
                elif punchcard[i] == '!':
                    the_lexeme.token +=punchcard[i]
                    self.state = 4
                    
                elif punchcard[i] == ';' or punchcard[i] == '+' or punchcard[i] == '-' or punchcard[i] == '*' or punchcard[i] == '/' or punchcard[i] == '%':
                    the_lexeme.token += punchcard[i] 
                    self.state = 7
                    
                elif punchcard[i] == '_' or punchcard[i].isalpha():
                    the_lexeme.token +=punchcard[i]
                    self.state = 5
                    
                elif punchcard[i].isdigit():
                    the_lexeme.token +=punchcard[i]
                    self.state = 6
                
                elif punchcard[i] == '':
                    tokensCard.append(Lexeme(punchcard[i], word = 'TT_END_OF_FILE'))
                    self.state = 1
                    pass
                
                else:
                    the_lexeme.word +=punchcard[i]
                    tokensCard.append(Lexeme(punchcard[i], word = 'TT_INVALID_TOKEN'))
                    self.state = 1
                    break
                pass

            elif self.state == 2:
                if punchcard[i] == '\n' :
                    self.line += 1
                    self.state = 1                
                #Em python read() retorna uma string vazia quando chega ao final de uma string:
                elif punchcard[i] == '':
                    tokensCard.append(Lexeme(punchcard[i], word = 'ERRT_END_OF_FILE'))
                    self.state = 8            
                else:
                    self.state = 2
                pass

            elif self.state == 3:
                if punchcard[i] == "=":
                    the_lexeme.token +=punchcard[i]
                    self.state = 7
                else:
                    # self.file.seek(self.file.tell() - 1)
                    i-=1                
                    self.state = 7
                    
                pass       
                        
                        
            elif self.state == 4:
                if punchcard[i] == '=' :
                    the_lexeme.token += punchcard[i] 
                    self.state = 7
                    
                #Em python read() retorna uma string vazia quando chega ao final de uma string:
                elif punchcard[i] == '':             
                    tokensCard.append(Lexeme(punchcard[i], word = 'TT_UNEXPECTED_EOF'))
            
                else:                
                    tokensCard.append(Lexeme(punchcard[i], word = 'TT_INVALID_TOKEN'))
                    self.state = 1
                    break
                pass       
                    
            elif self.state == 5:
                if punchcard[i] == '_' or punchcard[i].isalpha() or punchcard[i].isnumeric():
                    the_lexeme.token +=punchcard[i]
                    self.state = 5
                else:
                    # self.file.seek(self.file.tell() - 1)
                    i-=1                
                    self.state = 7
                
                pass   
                            
                
            elif self.state == 6:
                if punchcard[i].isdigit():
                    the_lexeme.token+=punchcard[i]
                    self.state = 6
                else:
                    # auxExpression = ''
                    # # self.file.seek(self.file.tell() - 1)
                    # i-=1                
                    # auxExpression = 'NUMBER'
                    self.state = 8
                pass   
                    
            if self.state == 7:
                tokensCard.append(Lexeme(the_lexeme.token, EquivalentSymbol(the_lexeme.token)))
                the_lexeme = Lexeme()
                self.state = 1

            if self.state == 8:
                # i-=1 # DAHMN THERE'S fuckOFF shut that subtraction outside of here
                if(InsideTokenScope(the_lexeme.token)):
                    auxExpression = EquivalentSymbol(Lexeme(the_lexeme.token))
                else:
                    auxExpression = 'NUMBER'
                
                tokensCard.append(Lexeme(the_lexeme.token, auxExpression))

                the_lexeme = Lexeme()
                self.state = 1
                continue

            i+=1
        return tokensCard

    # def nextToken(self):
    #         self.state = 1
    #         the_lexeme = Lexeme()
    #         tape = []
            
    #         while self.state != 7 and self.state != 8:
            
    #             char = self.file.read(1)
    #             last_char = char
    #                 # print(char,self.state,  '  @  ')
    #             # self.state_then_token = Walkthroughself.states(self.state, char, )
                
    #             if self.state == 1:
    #                 # print(f"ENTREI!, {char == ''}")
    #                 if char == ' ' or char == '\t' or char == '\r':
    #                     self.state = 1
                        
    #                 elif char == '\n':
    #                     self.line += 1
    #                     self.state = 1

    #                 elif char == '=' or char == '<' or char == '>':
    #                     the_lexeme.token += char
    #                     self.state = 3
                        
    #                 elif char == '!':
    #                     the_lexeme.token += char
    #                     self.state = 4
                        
    #                 elif char == ';' or char == '+' or char == '-' or char == '*' or char == '/' or char == '%':
    #                     the_lexeme.token += char 
    #                     self.state = 7
                        
    #                 elif char == '_' or char.isalpha():
    #                     the_lexeme.token += char
    #                     self.state = 5
                        
    #                 elif char.isdigit():
    #                     the_lexeme.token += char
    #                     self.state = 6
                    
    #                 elif char == '':
    #                     the_lexeme.word = 'TT_END_OF_FILE'
    #                     self.state = 8
                    
    #                 else:
    #                     the_lexeme.word += char
    #                     the_lexeme.word = 'TT_INVALID_TOKEN'
    #                     self.state = 8

    #                 break                    
    #                 # print(self.state)
    #                 # exit()
        
                    
    #             elif self.state == 2:
    #                 ungetc = False
    #                 if char == '\n' :
    #                     self.line += 1
    #                     self.state = 1                
    #                 #Em python read() retorna uma string vazia quando chega ao final de uma string:
    #                 elif char == '':
    #                     the_lexeme.word = 'ERRT_END_OF_FILE'
    #                     self.state = 8            
    #                 else:
    #                     self.state = 2
    #                 break       
                        
    #             elif self.state == 3:
    #                 ungetc = False
    #                 if char == "=":
    #                     the_lexeme.token += char
    #                     self.state = 7
    #                 else:
    #                     self.file.seek(self.file.tell() - 1)
    #                     self.state = 7
                        
    #                 break       
                        
                        
    #             elif self.state == 4:
    #                 ungetc = False
    #                 if char == '=' :
    #                     the_lexeme.token += char 
    #                     self.state = 7
                    
    #                 #Em python read() retorna uma string vazia quando chega ao final de uma string:
    #                 elif char == '':
    #                     the_lexeme.word = 'TT_UNEXPECTED_EOF'
    #                     self.state = 8
                
    #                 else:
    #                     the_lexeme.word = 'TT_INVALID_TOKEN'
    #                     self.state = 8
    #                 break       
                    
    #             elif self.state == 5:
    #                 if char == '_' or char.isalpha() or char.isnumeric():
    #                     the_lexeme.token += char
    #                     self.state = 5
    #                 else:
    #                     self.file.seek(self.file.tell() - 1)
    #                     self.state = 7
                    
    #                 break   
                            
                
    #             elif self.state == 6:
    #                 if char.isdigit():
    #                     the_lexeme.token+=char
    #                     self.state = 6
    #                 else:
                            
    #                     self.file.seek(self.file.tell() - 1)
    #                     the_lexeme.word = 'NUMBER'
    #                     self.state = 8
    #                 break   
                    
    #             if self.state == 7:
    #                 the_lexeme.word = EquivalentSymbol(the_lexeme.token)
            
                
    #             # print(char, "  @  \n")
    #             # if self.state == 7:
    #             #     the_lexeme.word = EquivalentSymbol(the_lexeme.token)
            
    #             # the_lexeme.word = EquivalentSymbol(the_lexeme.token)
    #         return the_lexeme
