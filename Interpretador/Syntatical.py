from Lexical import *


# from Expressions_and_Commands.BlocksCommand import *

# from Expressions_and_Commands.ConstIntExpression import *

from Expressions_and_Commands.OutputCommand import *

from Expressions_and_Commands.ReadIntExpression import *

class SyntaticAnalyzer:
    def __init__(self, lexeme = Lexeme(), LexAnalysis = LexicalAnalyzer('examples/read.tiny')):
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

        if token == self.lexemes[self.readingPoint].word:
            self.NextLexeme()
        else:
            self.ShowError()


    def Start(self):
        
        startCmd = self.procProgram()
        
        self.eat('TT_END_OF_FILE')

        return startCmd
        
    def procProgram(self):
        
        self.eat('KT_PROGRAM')
        
        programCmd = self.procCmdList()
        

        return programCmd


    #<cmdlist>   ::= <cmd> { <cmd> }
    def procCmdList(self): # v 
        
        commandLIne = self.LexAnalysis.line
        commands = BlocksCommand(commandLIne)
         
        cmdCmd = self.procCmd()
        commands.addCommand(cmdCmd)

        while self.lexemes[self.readingPoint].word == 'OT_VAR' or self.lexemes[self.readingPoint].word == 'KT_OUTPUT' or self.lexemes[self.readingPoint].word == 'KT_IF' or self.lexemes[self.readingPoint].word == 'KT_WHILE':
            cmdCmd = self.procCmd()
            commands.addCommand(cmdCmd)

        
        return commands 

    #<cmd>       ::= (<assign> | <output> | <if> | <while>) ;
    def procCmd(self):
        auxCommand = Command(self.LexAnalysis.line)
        
        if self.lexemes[self.readingPoint].word == 'OT_VAR':
            self.procAssign()

        elif self.lexemes[self.readingPoint].word == 'KT_OUTPUT':
            auxCommand = self.procOutput()
            
        elif self.lexemes[self.readingPoint].word == 'KT_IF':
            self.procIf()

        elif self.lexemes[self.readingPoint].word == 'KT_WHILE':
            self.procWhile()

        else:
            self.ShowError()
        
        self.eat('ST_SEMICOLON')
        
        return auxCommand

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
        
        outputCmd = OutputCommand(outputLine, expression if type(expression) == type(1)  else expression.expression() )
        
        
        return outputCmd
         

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
        
        leftExpression = self.procIntTerm()
        

        if self.lexemes[self.readingPoint].word == 'AT_ADD' or self.lexemes[self.readingPoint].word == 'AT_SUB' or self.lexemes[self.readingPoint].word == 'AT_MUL' or self.lexemes[self.readingPoint].word == 'AT_MOD' or self.lexemes[self.readingPoint].word == 'AT_DIV':
            if self.lexemes[self.readingPoint].word == 'AT_ADD' or self.lexemes[self.readingPoint].word == 'AT_MUL' or self.lexemes[self.readingPoint].word == 'AT_SUB' or self.lexemes[self.readingPoint].word == 'AT_DIV' or self.lexemes[self.readingPoint].word == 'AT_MOD':
                self.NextLexeme()
            else:
                self.NextLexeme()

            self.procIntTerm()

        return leftExpression
    
    #<intterm>   ::= <var> | <const> | read
    def procIntTerm(self): # v

        if self.lexemes[self.readingPoint].word == 'OT_VAR':
            self.procVar()
            return 0

        elif self.lexemes[self.readingPoint].word == 'NUMBER':
            a = self.procConst()
            return a

        else:
            
            self.eat('KT_READ')
            readLine = self.LexAnalysis.line
            
            readExpression = ReadIntExpression(readLine)
            
            return readExpression.ReadIntExpression()


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
