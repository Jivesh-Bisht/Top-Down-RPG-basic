from player import stats
from stats import display_stats
from inventory import display_inventory
from congratulations import show_congratulations
from essentials import clear, print_world, world, levelCleared, levelFailed, add_obstacles, add_enemies, add_gate, get_player
from main_menu import main_menu
from keybinds import keybinds_menu
import keyboard, json
from collision import Collision

with open("stats.json") as f:
    __ = json.load(f)
    runs = __["runs"]

health = stats["health"]

def generate_new_world():
    new_world = [["#","#","#","#","#","#","#","#","#","#"],
                ["#",".",".",".",".","*",".",".",".","#"],
                ["#",".",".",".",".",".",".",".",".","#"],
                ["#",".",".",".",".",".",".",".",".","#"],
                ["#",".",".",".",".",".",".",".",".","#"],
                ["#",".",".",".",".",".",".",".",".","#"],
                ["#","#","#","#","#","#","#","#","#","#"]]
    add_enemies(new_world)
    add_obstacles(new_world)
    add_gate(new_world)
    return new_world

def play_game():
    global world
    try:
        clear()
        print_world(world)
        run = True
        while run:
            if keyboard.is_pressed('q'):
                clear()
                print("Quitting")
                run = False

            if keyboard.is_pressed('i'):
                clear()
                display_inventory()
                while True:
                    ask = input("Continue??(y) > ")
                    if ask == "y":
                        clear()
                        print_world(world)
                        break

            if keyboard.is_pressed('a'):
                level, current_pos = get_player(world)
                collision = Collision(world, level, current_pos, health=health)
                collision.leftCollision()

            if keyboard.is_pressed('d'):
                level, current_pos = get_player(world)
                collision = Collision(world, level, current_pos, health)
                collision.rightCollision()

            if keyboard.is_pressed('w'):
                level, current_pos = get_player(world)
                collision = Collision(world, level, current_pos, health)
                collision.upCollision()

            if keyboard.is_pressed('s'):
                level, current_pos = get_player(world)
                collision = Collision(world, level, current_pos, health)
                collision.downCollision()
    except (levelCleared, levelFailed) as e:
        if isinstance(e, levelCleared):
            print("level cleared")
            choice = show_congratulations(level)
            if choice == "continue":
                level += 1
                # Generate a new world for the new level
                world = generate_new_world()
                play_game()
            else:
                print("Exiting game.")
        else:
            print("level failed booooooo!!")

clear()
world = generate_new_world()
print_world(world)

if __name__ == "__main__":
    main_menu()
    work = input("> ")
    if work == "1":
        runs += 1
        play_game()
    elif work == "2":
        keybinds_menu()
        print("Continue to game??(y/n)")
        k = input("> ")
        if k == "y":
            play_game()
            runs += 1
        else:
            print("Quitting")
    elif work == "3":
        display_inventory()
        print("Continue to game??(y/n)")
        k = input("> ")
        if k == "y":
            play_game()
            runs += 1
        else:
            print("Quitting")
    elif work == "4":
        display_stats()
        print("Continue to game??(y/n)")
        k = input("> ")
        if k == "y":
            play_game()
            runs += 1
        else:
            print("Quitting")
    elif work == "5":
        print("Quitting")

    __["runs"] = runs
    with open("stats.json", "w") as f:
        json.dump(__, f)
