from Expressions_and_Commands.Commando import *
from Expressions_and_Commands.ConstIntExpression import *

class OutputCommand(Command):
    def __init__(self, line, intExp ):
        super().__init__(line)
        self.__intExp = IntExpression(line)
    
    def execute(self):
        print(self.__intExp.expression())
        