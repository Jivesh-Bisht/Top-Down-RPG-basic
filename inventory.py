from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import json
import os

console = Console()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def load_inventory():
    with open("inventory.json") as f:
        inventory = json.load(f)
    return inventory

def load_items():
    with open("items.json") as f:
        items = json.load(f)
    return items

def display_inventory():
    clear_screen()
    
    inventory = load_inventory()
    items = load_items()
    
    inventory_str = ""
    for inv_item in inventory:
        item_name = inv_item['item']
        quantity = inv_item['quantity']
        for item in items["items"]:
            if item["name"] == "Potion" and item_name == "potion":
                item_description = item["description"]
                inventory_str += f"[bold yellow]{item["name"]}[/bold yellow]: [blue]{quantity}[/blue] - [italic]{item_description}[/italic]\n"
            if item["name"] == "Hi-Potion" and item_name == "hipotion":
                item_description = item["description"]
                inventory_str += f"[bold yellow]{item["name"]}[/bold yellow]: [blue]{quantity}[/blue] - [italic]{item_description}[/italic]\n"
            if item["name"] == "Super Potion" and item_name == "superpotion":
                item_description = item["description"]
                inventory_str += f"[bold yellow]{item["name"]}[/bold yellow]: [blue]{quantity}[/blue] - [italic]{item_description}[/italic]\n"
            if item["name"] == "Elixer" and item_name == "elixer":
                item_description = item["description"]
                inventory_str += f"[bold yellow]{item["name"]}[/bold yellow]: [blue]{quantity}[/blue] - [italic]{item_description}[/italic]\n"
            if item["name"] == "MegaElixer" and item_name == "hielixer":
                item_description = item["description"]
                inventory_str += f"[bold yellow]{item["name"]}[/bold yellow]: [blue]{quantity}[/blue] - [italic]{item_description}[/italic]\n"
            if item["name"] == "Grenade" and item_name == "grenade":
                item_description = item["description"]
                inventory_str += f"[bold yellow]{item["name"]}[/bold yellow]: [blue]{quantity}[/blue] - [italic]{item_description}[/italic]\n"
           
    inventory_title = """

██╗███╗░░██╗██╗░░░██╗███████╗███╗░░██╗████████╗░█████╗░██████╗░██╗░░░██╗
██║████╗░██║██║░░░██║██╔════╝████╗░██║╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝
██║██╔██╗██║╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░██║░░██║██████╔╝░╚████╔╝░
██║██║╚████║░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░██║░░██║██╔══██╗░░╚██╔╝░░
██║██║░╚███║░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░╚█████╔╝██║░░██║░░░██║░░░
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
    """
    
    combined_str = f"[bold cyan]{inventory_title}[/bold cyan]\n{inventory_str}"
    
    panel = Panel(Align.center(combined_str), title="[bold magenta]Inventory[/bold magenta]", border_style="bold green")
    aligned_panel = Align.center(panel)
    console.print(aligned_panel)

# Call the display_inventory function to show the inventory page
display_inventory()