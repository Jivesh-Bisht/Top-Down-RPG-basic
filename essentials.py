from os import system, name
from termcolor import cprint
obstacles = ["$","@","|"]
gate="#"
enemy="%"
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
            elif element == enemy:
                cprint(element,"yellow",end=" ")      # i kinda forgor💀 what this end=" " does and what will happen if i remove it and i am too lazy to check 
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