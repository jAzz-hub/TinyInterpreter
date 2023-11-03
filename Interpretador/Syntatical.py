from Lexical import *


# from Expressions_and_Commands.BlocksCommand import *

# from Expressions_and_Commands.ConstIntExpression import *

from Expressions_and_Commands.OutputCommand import *

class SyntaticAnalyzer:
    def __init__(self, lexeme = Lexeme(), LexAnalysis = LexicalAnalyzer('examples/sum.tiny')):
        self.LexAnalysis = LexAnalysis
        self.lexemes = LexAnalysis.TinyAutomata()
        self.readingPoint = 0

    def NextLexeme(self):
        self.readingPoint+=1

    def ShowError(self):
        print(f'Erro na linha : {self.LexAnalysis.line}')

        if self.lexemes[self.readingPoint].word == 'TT_INVALID_TOKEN':
            print(f'Lexema inválido {self.lexemes[self.readingPoint].word}\n')
        
        elif self.lexemes[self.readingPoint].word == 'ERRT_UNEXPECTED_EOF' or self.lexemes[self.readingPoint].word == 'ERRT_END_OF_FILE':
            print('Fim de arquivo inesperado')
        
        else:
            print(f'Lexema não esperado! \n\n\t{self.lexemes[self.readingPoint].word}')
        
        print('F')
        exit()

    def eat(self, token):
        print('\n\n')
        print(f'i: {self.readingPoint} (Expected: {token} , Found: {self.lexemes[self.readingPoint].word})\n')

        if token == self.lexemes[self.readingPoint].word:
            self.NextLexeme()
        else:
            self.ShowError()


    def Start(self):
        self.procProgram()
        self.eat('TT_END_OF_FILE')

    def procProgram(self):
        self.eat('KT_PROGRAM')
        self.procCmdList()



    #<cmdlist>   ::= <cmd> { <cmd> }
    def procCmdList(self): # v 
        
        self.procCmd()

        while self.lexemes[self.readingPoint].word == 'OT_VAR' or self.lexemes[self.readingPoint].word == 'KT_OUTPUT' or self.lexemes[self.readingPoint].word == 'KT_IF' or self.lexemes[self.readingPoint].word == 'KT_WHILE':
            self.procCmd()



    #<cmd>       ::= (<assign> | <output> | <if> | <while>) ;
    def procCmd(self):
        if self.lexemes[self.readingPoint].word == 'OT_VAR':
            self.procAssign()

        elif self.lexemes[self.readingPoint].word == 'KT_OUTPUT':
            self.procOutput()

        elif self.lexemes[self.readingPoint].word == 'KT_IF':
            self.procIf()

        elif self.lexemes[self.readingPoint].word == 'KT_WHILE':
            self.procWhile()

        else:
            self.ShowError()
        
        self.eat('ST_SEMICOLON')


    #<assign>    ::= <var> = <intexpr>
    def procAssign(self): #v 
        self.procVar()
        self.eat('ST_ASSIGN')
        self.procIntExpr()


    #<output>    ::= output <intexpr>
    def procOutput(self): #v
        self.eat('KT_OUTPUT')
        
        outputLine = self.LexAnalysis.line
        expression = self.procIntExpr()
        
        outputCmd = OutputCommand(outputLine, expression)
         

#<if>        ::= if <boolexpr> then <cmdlist> [ else <cmdlist> ] done
    def procIf(self): #v
        self.eat('KT_IF')
        self.procBoolExpr()
        self.eat('KT_THEN')
        self.procCmdList()
        
        if self.lexemes[self.readingPoint].word == 'KT_ELSE':
            self.NextLexeme()
            self.procCmdList()

        self.eat('KT_DONE')


#<while>     ::= while <boolexpr> do <cmdlist> done
    def procWhile(self): #v
        self.eat('KT_WHILE')
        self.procBoolExpr()
        self.eat('KT_DO')
        self.procCmdList()
        self.eat('KT_DONE')
        


    #<boolexpr>  ::= false | true |
    #                not <boolexpr> |
    #                <intterm> (== | != | < | > | <= | >=) <intterm>
    def procBoolExpr(self): #v

        if self.lexemes[self.readingPoint].word == 'KT_FALSE':
            self.NextLexeme()
        
        elif self.lexemes[self.readingPoint].word == 'KT_TRUE':
            self.NextLexeme()
        
        elif self.lexemes[self.readingPoint].word ==  'KT_NOT':
            self.NextLexeme()
            self.procBoolExpr()
        
        else:
            self.procIntTerm()
            while(1):
                if self.lexemes[self.readingPoint].word ==  'ST_EQUAL' or self.lexemes[self.readingPoint].word == 'ST_NOT_EQUAL' or self.lexemes[self.readingPoint].word == 'ST_LOWER' or self.lexemes[self.readingPoint].word == 'ST_GREATER' or self.lexemes[self.readingPoint].word == 'ST_LOWER_EQUAL' or self.lexemes[self.readingPoint].word == 'ST_GREATER_EQUAL': 
                    self.NextLexeme()
                    break
                else:
                    self.ShowError()  
                    break

            self.procIntTerm()


    #<intexpr>   ::= [ + | - ] <intterm> [ (+ | - | * | / | %) <intterm> ]
    def procIntExpr(self): #v
        if self.lexemes[self.readingPoint].word == 'AT_ADD':
              self.NextLexeme()
        elif self.lexemes[self.readingPoint].word == 'AT_SUB':
             self.NextLexeme()
        
        expression = self.procIntTerm()

        if self.lexemes[self.readingPoint].word == 'AT_ADD' or self.lexemes[self.readingPoint].word == 'AT_SUB' or self.lexemes[self.readingPoint].word == 'AT_MUL' or self.lexemes[self.readingPoint].word == 'AT_MOD' or self.lexemes[self.readingPoint].word == 'AT_DIV':
            if self.lexemes[self.readingPoint].word == 'AT_ADD' or self.lexemes[self.readingPoint].word == 'AT_MUL' or self.lexemes[self.readingPoint].word == 'AT_SUB' or self.lexemes[self.readingPoint].word == 'AT_DIV' or self.lexemes[self.readingPoint].word == 'AT_MOD':
                self.NextLexeme()
            else:
                self.NextLexeme()

            self.procIntTerm()

        return expression
    #<intterm>   ::= <var> | <const> | read
    def procIntTerm(self): # v

        if self.lexemes[self.readingPoint].word == 'OT_VAR':
            self.procVar()
            return 0

        elif self.lexemes[self.readingPoint].word == 'NUMBER':
            self.procConst()

        else:
            self.eat('KT_READ')
            return 0


    #<var>       ::= id
    def procVar(self): #v
        self.eat('OT_VAR')


    #<const>     ::= number
    def procConst(self): #v
        
        auxVariable =  self.lexemes[self.readingPoint].token
        
        self.eat('NUMBER')
        
        lineOfNumber = self.LexAnalysis.line
            
        eatenNumber = int(auxVariable)

        expression = ConstIntExpression(lineOfNumber, eatenNumber)

        return expression
