from Tokens import *

class Lexeme:
    '''
    Essa classe recebe apenas o valor do token em seu construtor
    '''
    
    def __init__(self, token = "", word = ""):
        self.string = ""
        try:
            print(f"\t {token} + \t ")
            if word != "":
                self.word = word
            else:
                self.word = [i.name for i in Tokens if i.value == token][0]
        except IndexError:
            print(f' --------\{token}/-----------')
        if(token == '\n'):
            token = '\\n'
        
        self.token = token


    def stringnizing(self):
        self.string+="(\""
        self.string+=self.token
        self.string+="\", "
        self.string+=str(self.word)
        self.string+=")"
        return str(self.string)


a = Lexeme('program')

a.string = a.stringnizing()

print(a.string)