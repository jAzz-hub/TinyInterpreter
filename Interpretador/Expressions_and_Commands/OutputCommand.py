from Expressions_and_Commands.BlocksCommand import *
from Expressions_and_Commands.ConstIntExpression import *


class OutputCommand(Command):
    def __init__(self, line, intExp ):
        super().__init__(line)
        self.__intExp = intExp
    
    def intExp(self):
        return self.__intExp
    
    
    def execute(self):
        print(int( self.intExp() ))
        