from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import os

console = Console()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def keybinds_menu():
    clear_screen()

    # ASCII Art for "Keybinds"
    keybinds_title = """ 
██╗  ██╗███████╗██╗   ██╗██████╗ ██╗███╗   ██╗██████╗ ███████╗
██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔══██╗██║████╗  ██║██╔══██╗██╔════╝
█████╔╝ █████╗   ╚████╔╝ ██████╔╝██║██╔██╗ ██║██║  ██║███████╗
██╔═██╗ ██╔══╝    ╚██╔╝  ██╔══██╗██║██║╚██╗██║██║  ██║╚════██║
██║  ██╗███████╗   ██║   ██║  ██║██║██║ ╚████║██████╔╝███████║
╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝
    """

    # Keybind options (centered)
    keybinds_text = """ 
    [bold yellow]W[/bold yellow] - Move Up
    [bold yellow]A[/bold yellow] - Move Left
    [bold yellow]S[/bold yellow] - Move Down
    [bold yellow]D[/bold yellow] - Move Right
    [bold yellow]E[/bold yellow] - Interact
    [bold yellow]I[/bold yellow] - Inventory
    [bold yellow]Q[/bold yellow] - Quit in between the game
    """

    # Combine title and keybinds
    menu_content = Align.center(f"[bold cyan]{keybinds_title}[/bold cyan]\n{keybinds_text}")

    # Create a panel with centered content
    menu_panel = Panel(
        menu_content,
        title="[bold green]Keybinds[/bold green]",
        border_style="blue",
        padding=(1, 5),  # Adds spacing inside the panel
    )

    console.print(Align.center(menu_panel))  # Center everything in the terminal

if __name__ == "__main__":
    keybinds_menu()
