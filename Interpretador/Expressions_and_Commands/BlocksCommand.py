
from Expressions_and_Commands.Commando import *
class BlocksCommand(Command):
    
    def __init__(self, line, comandos = []):
        super().__init__(line)
        self.__comandos = comandos
        
    def addCommand(self, command):
        self.__comandos.append(command)
    
    def comandos(self):
        return self.__comandos
    
    @abstractmethod
    def execute(self):
        for i in self.__comandos:
            i.execute()