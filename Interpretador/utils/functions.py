from os import system as soSys
from platform import system as platSys

def clear():
    if platSys() == 'Linux':
        soSys('clear')
    else:
        soSys('cls')