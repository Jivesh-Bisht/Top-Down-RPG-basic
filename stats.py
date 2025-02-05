from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import json
import os

console = Console()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def load_stats():
    with open("stats.json") as f:
        stats = json.load(f)
    return stats

def display_stats():
    clear_screen()
    
    stats = load_stats()
    
    stats_str = f"""
 [bold yellow]Name[/bold yellow]: [blue]{stats['name']}[/blue]
 [bold yellow]HP[/bold yellow]: [blue]{stats['hp']}[/blue]
 [bold yellow]MP[/bold yellow]: [blue]{stats['mp']}[/blue]
 [bold yellow]Attack[/bold yellow]: [blue]{stats['atk']}[/blue]
 [bold yellow]Defense[/bold yellow]: [blue]{stats['df']}[/blue]
 [bold yellow]Runs[/bold yellow]: [blue]{stats['runs']}[/blue]
    """
    
    stats_title = """

░██████╗████████╗░█████╗░████████╗░██████╗
██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝
╚█████╗░░░░██║░░░███████║░░░██║░░░╚█████╗░
░╚═══██╗░░░██║░░░██╔══██║░░░██║░░░░╚═══██╗
██████╔╝░░░██║░░░██║░░██║░░░██║░░░██████╔╝
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░
    """
    
    combined_str = f"[bold cyan]{stats_title}[/bold cyan]\n{stats_str}"
    
    panel = Panel(combined_str, title="Player Stats", border_style="bold blue")
    aligned_panel = Align.center(panel)
    console.print(aligned_panel)

# Call the display_stats function to show the stats page
display_stats()