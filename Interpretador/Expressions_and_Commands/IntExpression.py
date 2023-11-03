
from abc import abstractmethod

class IntExpression:
    
    def __init__(self, line):
        self._line = line
    
    def line(self):
        return self._line
    
    @abstractmethod
    def expression():
        return 0