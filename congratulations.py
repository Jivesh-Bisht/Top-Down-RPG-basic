from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
import time

def show_congratulations(current_level):
    console = Console()
    ascii_art = """
     ____                            _         _       _   _                 
    / ___|___  _ __  _ __   ___  ___| |_   _  | | ___ | |_| |_ ___ _ __ ___  
   | |   / _ \| '_ \| '_ \ / _ \/ __| | | | | | |/ _ \| __| __/ _ \ '__/ __| 
   | |__| (_) | | | | | | |  __/ (__| | |_| | | | (_) | |_| ||  __/ |  \__ \ 
    \____\___/|_| |_|_| |_|\___|\___|_|\__, | |_|\___/ \__|\__\___|_|  |___/ 
                                       |___/                                
    """
    next_level = current_level + 1
    message = f"Progress: {current_level} -> {next_level}"
    panel = Panel(f"{ascii_art}\n\n{message}", title="Congratulations", subtitle="Select an option below")

    console.clear()
    console.print(panel, justify="center")

    choice = Prompt.ask("Do you want to continue or exit?", choices=["continue", "exit"], default="continue")
    return choice

def show_wait_screen():
    console = Console()
    ascii_art = """
     __        __    _ _      
     \ \      / /_ _| | | ___ 
      \ \ /\ / / _` | | |/ _ \\
       \ V  V / (_| | | |  __/
        \_/\_/ \__,_|_|_|\___|
    """
    message = "You need to clear all enemies before continuing"
    panel = Panel(f"{ascii_art}\n\n{message}", title="Wait", subtitle="Continuing in 5 seconds")

    console.clear()
    console.print(panel, justify="center")

    with Progress(
        SpinnerColumn(),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task("Continuing in 5 seconds...", total=100)
        for i in range(100):
            time.sleep(0.05)
            progress.update(task, advance=1, description=f"{5 - i // 20} seconds remaining")