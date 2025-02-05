from essentials import clear,print_world,obstacles,enemy,gate,player,world,levelCleared,levelFailed
from main_menu import main_menu
from keybinds import keybinds_menu
import keyboard
from collision import Collision
from random import randint,choice
from player import stats

def add_enemies(world, enemyy=2):
    for _ in range(enemyy):
        level = randint(1, len(world) - 2)  # Avoid first and last row
        pos = randint(1, len(world[0]) - 2)  # Avoid first and last column
        if world[level][pos] in obstacles:
            pass
        elif (level, pos) == get_player(world):
            pass
        else:
            world[level][pos] = choice(enemy)

def add_gate(world):
    length = len(world)
    width = len(world[0])
    while True:
        if randint(0, 1) == 0:
            level = length - 1  # Last row but not the corners
            pos = randint(1, width - 1)
        else:
            level = randint(1, length - 1)
            pos = width - 1  # Last column but not the corners
        if (level, pos) != (length - 2, width - 2) and (level, pos) != (length - 2, 1) and (level, pos) != (1, width - 2):
            break
    world[level][pos] = gate

def add_obstacles(world, obs=5):
    for _ in range(obs):
        while True:
            level = randint(1, len(world) - 2)  # Avoid first and last row
            pos = randint(1, len(world[0]) - 2)  # Avoid first and last column
            if (level, pos) == get_player(world):
                continue
            if world[level][pos] in obstacles:
                continue
            if world[level][pos] == gate:
                continue
            if world[level][pos] in enemy:
                continue
            # Ensure obstacles do not surround the gate, enemy, or player
            if not ((world[level-1][pos] in [gate, player] and world[level+1][pos] in [gate, player] and world[level][pos-1] in [gate, player] and world[level][pos+1] in [gate, player]) or
                    (world[level-1][pos] in enemy and world[level+1][pos] in enemy and world[level][pos-1] in enemy and world[level][pos+1] in enemy)):
                world[level][pos] = choice(obstacles)
                break
    



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
    except (levelCleared,levelFailed) as e:
        if isinstance(e,levelCleared):
            print("level cleared")
        else:
            print("level failed booooooo!!")


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

