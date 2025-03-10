from os import system, name
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.padding import Padding
from random import randint, choice

obstacles = ["$","@","|"]
border="#"
gate="="
enemy="%"
player = "*"
world = [["#","#","#","#","#","#","#","#","#","#"],
         ["#",".",".",".",".","*",".",".",".","#"],
         ["#",".",".",".",".",".",".",".",".","#"],
         ["#",".",".",".",".",".",".",".",".","#"],
         ["#",".",".",".",".",".",".",".",".","#"],
         ["#",".",".",".",".",".",".",".",".","#"],
         ["#","#","#","#","#","#","#","#","#","#"]]

class levelCleared(Exception):pass
class levelFailed(Exception):pass


console = Console()
def get_player(world) -> tuple[int, int]:
    for level, levels in enumerate(world):
        try:
            current_pos = levels.index(player)
            return level, current_pos
        except ValueError:
            level += 1
            
def print_world(world):
    world_str = ""
    for levels in world:
        for element in levels:
            if element == player:
                world_str += f"[green]{element}[/green] "
            elif element == enemy:
                world_str += f"[yellow]{element}[/yellow] "
            elif element in obstacles:
                world_str += f"[red]{element}[/red] "
            elif element == gate:
                world_str += f"[blue]{element}[/blue] "
            else:
                world_str += f"[magenta]{element}[/magenta] "
        world_str += "\n"
    world_str=world_str.rstrip("\n")
    padded_world_str = Padding(world_str, (1, 4))  # Add padding (top/bottom, left/right)
    panel = Panel(padded_world_str, title="level1", border_style="bold magenta")
    aligned_panel = Align.center(panel)
    console.print(aligned_panel)


def add_enemies(world, enemyy=1):
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


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')