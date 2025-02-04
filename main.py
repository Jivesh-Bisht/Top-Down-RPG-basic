import keyboard
from os import system, name
from termcolor import cprint
from random import randint,choice
from random import randint
from essentials import clear,obstacles,gate,player,world,print_world,levelCleared
from collision import Collision
from main_menu import main_menu

def add_gate(world):
    length = len(world)
    level=randint(0,length-1)
    print(level)
    world[level][0]=gate
    

def add_obstacles(world,obs=5):
    for i in range(obs):
        level = randint(0,(len(world)-1))
        pos = randint(0,9)
        if (level,pos) == get_player(world):
            pass
        else:
            world[level][pos] = choice(obstacles)
    



def get_player(world) -> tuple[int,int]:
    for level,levels in enumerate(world):
        try:
            current_pos = levels.index(player)
            return level,current_pos
        except ValueError:
            level+=1

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')

clear()
add_obstacles(world)
add_gate(world)
print_world(world)




def play_game():
    try:
        clear()
        print_world(world)
        while True:
            if keyboard.is_pressed('q'):
                clear()
                print("Quitting")
                run = False


            if keyboard.is_pressed('a'):
                level,current_pos = get_player(world)
                collision= Collision(world,level,current_pos)
                collision.leftCollision()

            if keyboard.is_pressed('d'):
                level,current_pos = get_player(world)
                collision= Collision(world,level,current_pos)
                collision.rightCollision()

            if keyboard.is_pressed('w'):
                level,current_pos = get_player(world)
                collision= Collision(world,level,current_pos)
                collision.upCollision()

            if keyboard.is_pressed('s'):
                level,current_pos = get_player(world)
                collision= Collision(world,level,current_pos)
                collision.downCollision()
    except levelCleared:
        print("level cleared")


if __name__ == "__main__":
    main_menu()
    work = input("> ")
    if work=="1":
        play_game()
    elif work=="2":
        print("Quitting")
        exit()
