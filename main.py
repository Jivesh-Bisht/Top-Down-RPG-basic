from essentials import clear,print_world,obstacles,enemy,gate,player,world,levelCleared
from main_menu import main_menu
from keybinds import keybinds_menu
import keyboard
from collision import Collision
from random import randint,choice
from player import stats

def add_enemies(world,enemyy=2):
    for _ in range(enemyy):
        level = randint(0,(len(world)-1))
        pos = randint(0,9)
        if world[level][pos] in obstacles:
            pass
        elif (level,pos) == get_player(world):
            pass
        else:
            world[level][pos] = choice(enemy)



def add_gate(world):
    length = len(world)
    level=randint(0,length-1)
    print(level)
    world[level][0]=gate
    

def add_obstacles(world,obs=5):
    for _ in range(obs):
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

health=stats["health"]

def play_game():
    try:
        clear()
        print_world(world)
        run=True
        while run:
            if keyboard.is_pressed('q'):
                clear()
                print("Quitting")
                run = False

            if keyboard.is_pressed('a'):
                level,current_pos = get_player(world)
                collision= Collision(world,level,current_pos,health=health)
                collision.leftCollision()

            if keyboard.is_pressed('d'):
                level,current_pos = get_player(world)
                collision= Collision(world,level,current_pos,health)
                collision.rightCollision()

            if keyboard.is_pressed('w'):
                level,current_pos = get_player(world)
                collision= Collision(world,level,current_pos,health)
                collision.upCollision()

            if keyboard.is_pressed('s'):
                level,current_pos = get_player(world)
                collision= Collision(world,level,current_pos,health)
                collision.downCollision()
    except levelCleared:
        print("level cleared")


clear()
add_enemies(world)
add_obstacles(world)
add_gate(world)
print_world(world)

if __name__ == "__main__":
    main_menu()
    work = input("> ")
    if work=="1":
        play_game()
    elif work=="2":
        keybinds_menu()
        print("Continue to game??(y/n)")
        k = input("> ")
        if k=="y":
            play_game()
        else:
            print("Quitting")
    elif work=="3":
        print("Quitting")

