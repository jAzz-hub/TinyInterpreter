from Expressions_and_Commands.IntExpression import *
class   ConstIntExpression(IntExpression):
    def __init__(self, line, value):
        super().__init__(line)
        self.__m_Value = value
       
    def expression(self):
        return self.__m_Value
