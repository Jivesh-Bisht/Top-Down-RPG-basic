from fighting_logic.main import fight,player_spells,enemy_spells,player_items
from fighting_logic.classes.game import Person
import json


with open("stats.json") as f:
    stats= json.load(f)
with open("inventory.json") as f:
    inventory=json.load(f)



player=Person(stats["name"],stats["hp"],stats["mp"],stats["atk"],stats["df"],player_spells,player_items)
enemy = Person("Imp  ", 3000, 130, 560, 325, enemy_spells, [])

def fightt() -> bool:
    won=fight(player,enemy)
    if won:
        return True
    else:
        return False