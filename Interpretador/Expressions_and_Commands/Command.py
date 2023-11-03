from abc import abstractmethod
class Command:
    def __init__(self, line):
        self.__line = line
    
    def line(self):
        return self.__line
    
    @abstractmethod
    def execute():
        return 0