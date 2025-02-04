from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import os

console = Console()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    clear_screen()
    
    # ASCII Art for RPG title
    rpg_title = """ 
██████╗ ██████╗  ██████╗ 
██╔══██╗██╔══██╗██╔════╝ 
██████╔╝██████╔╝██║  ███╗
██╔══██╗██╔═══╝ ██║   ██║
██║  ██║██║     ╚██████╔╝
╚═╝  ╚═╝╚═╝      ╚═════╝ 
    """

    # Menu options (centered)
    menu_options = "\n[bold yellow][1][/bold yellow] Start Game\n\n[bold yellow][2][/bold yellow] Keybinds\n\n[bold yellow][3][/bold yellow] Quit\n"

    # Combine title and centered options
    menu_content = Align.center(f"[bold cyan]{rpg_title}[/bold cyan]\n{menu_options}")

    # Create a panel with centered content
    menu_panel = Panel(
        menu_content,
        title="[bold green]Welcome To[/bold green]",
        border_style="blue",
        padding=(1, 5),  # Adds spacing inside the panel
    )

    console.print(Align.center(menu_panel))  


