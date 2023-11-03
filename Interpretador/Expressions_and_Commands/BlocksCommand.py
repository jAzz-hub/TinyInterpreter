
from abc import abstractmethod

from Command import * 

class BlocksCommand(Command):
    
    def __init__(self, line, comandos = []):
        super().__init__(line)
        self.__comandos = comandos
        
    def addCommand(self, command):
        self.__comandos.append(command)
    
    @abstractmethod
    def execute():
        for i in self.__comandos:
            i.execute()