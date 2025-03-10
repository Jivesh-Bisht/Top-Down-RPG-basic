from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
import time

def show_congratulations(current_level):
    console = Console()
    ascii_art = """
  ____                            _         _       _   _                 _ 
 / ___|___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  ___| |
| |   / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __| |
| |__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \_|
 \____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___(_)
                  |___/                                                                                  
    """
    next_level = current_level + 1
    message = f"Progress: {current_level} -> {next_level}"
    panel = Panel(f"[bold green]{ascii_art}[/bold green]\n\n{message}", title="[bold cyan]Congratulations[/bold cyan]", subtitle="Select an option below",border_style="blue")

    console.clear()
    console.print(panel, justify="center")

    choice = Prompt.ask("Do you want to continue or exit?", choices=["continue", "exit"], default="continue")
    return choice

def show_wait_screen():
    console = Console()
    ascii_art = """
    __        __    _ _   _ 
    \ \      / /_ _(_) |_| |
     \ \ /\ / / _` | | __| |
      \ V  V / (_| | | |_|_|
       \_/\_/ \__,_|_|\__(_)
    """
    message = "You need to clear all enemies before continuing"
    panel = Panel(f"[bold green]{ascii_art}[/bold green]\n\n{message}", title="Wait", subtitle="Continuing in 4 seconds", border_style="blue")

    console.clear()
    console.print(panel, justify="center")

    with Progress(
        SpinnerColumn(),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task("Continuing in 4 seconds...", total=80)
        for i in range(90):
            time.sleep(0.025)
            progress.update(task, advance=1, description=f"{4 - i // 20} seconds remaining")


show_congratulations(1)