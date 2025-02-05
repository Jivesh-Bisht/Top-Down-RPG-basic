from os import system, name
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.padding import Padding

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



def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')