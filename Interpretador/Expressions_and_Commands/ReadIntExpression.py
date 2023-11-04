
from Expressions_and_Commands.IntExpression import *

class ReadIntExpression(IntExpression):
    def __init__(self, line):
        super().__init__(line)
    
    @abstractmethod
    def ReadIntExpression(self):
        value = int(input(''))
        return value
    