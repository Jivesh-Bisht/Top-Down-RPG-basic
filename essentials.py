from os import system, name
from termcolor import cprint


obstacles = ["$","@","|"]
gate="#"
player = "*"
world = [[".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".","*",".",".",".","."],
         [".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".","."]]

class levelCleared(Exception):pass

def print_world(world):
    for levels in world:
        for element in levels:
            if element == player:
                cprint(element,"green",end=" ")
            elif element in obstacles:
                cprint(element,"red",end=" ")
            elif element == gate:
                cprint(element,"blue",end=" ")
            else:
                cprint(element,"magenta",end=" ")
        print("\n")

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')