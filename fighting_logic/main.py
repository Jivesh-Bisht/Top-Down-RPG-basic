from fighting_logic.classes.game import bcolors
from fighting_logic.classes.magic import Spell
from fighting_logic.classes.inventory import Item
import random,time,json

# Create Black Magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")
curaga = Spell("Curaga", 50, 6000, "white")


# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 1000 HP", 1000)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

with open("inventory.json") as f:
    inventory=json.load(f)    


def save_inventory(player_items) -> None:
    new_inventory=[
    {
        "item": "potion",
        "quantity": player_items[0]["quantity"]
    },
    {
        "item": "hipotion",
        "quantity": player_items[1]["quantity"]
    },
    {
        "item": "superpotion",
        "quantity": player_items[2]["quantity"]
    },
    {
        "item": "elixer",
        "quantity": player_items[3]["quantity"]
    },
    {
        "item": "hielixer",
        "quantity": player_items[4]["quantity"]
    },
    {
        "item": "grenade",
        "quantity": player_items[5]["quantity"]
    }
]

    with open("inventory.json","w") as f:
        json.dump(new_inventory,f)   

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
enemy_spells = [fire, meteor, curaga]
player_items = [{"item": potion, "quantity": inventory[0]["quantity"]}, {"item": hipotion, "quantity": inventory[1]["quantity"]},
                {"item": superpotion, "quantity": inventory[2]["quantity"]}, {"item": elixer, "quantity": inventory[3]["quantity"]},
                {"item": hielixer, "quantity": inventory[4]["quantity"]}, {"item": grenade, "quantity": inventory[5]["quantity"]}]


# Instantiate People
# player = Person("Valos:", 3260, 132, 300, 34, player_spells, player_items)
# players=[player]
# enemy = Person("Imp  ", 1250, 130, 560, 325, enemy_spells, [])
# enemies=[enemy]



print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

def fight(player,enemy) -> bool:
    running = True
    i = 0
    enemies=[enemy]
    players=[player]
    while running:
        print("======================")

        print("\n\n")
        print("NAME                 HP                                     MP")
        player.get_stats()

        print("\n")
        enemy.get_enemy_stats()
        time.sleep(0.5)
        for player in players:
            player.choose_action()
            choice = input("    Choose action: ")
            index = int(choice) - 1

            if index == 0:
                dmg = player.generate_damage()

                enemy.take_damage(dmg)
                print("You attacked " + enemy.name.replace(" ", "") + " for", dmg, "points of damage.")
                time.sleep(0.5)

                if enemy.get_hp() == 0:
                    print(enemy.name.replace(" ", "") + " has died.")
                    print("You won!")
                    save_inventory(player_items)
                    enemy.heal(30000)
                    time.sleep(0.5)
                    return True

            elif index == 1:
                player.choose_magic()
                magic_choice = int(input("    Choose magic: ")) - 1

                if magic_choice == -1:
                    continue

                spell = player.magic[magic_choice]
                magic_dmg = spell.generate_damage()

                current_mp = player.get_mp()

                if spell.cost > current_mp:
                    print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                    time.sleep(0.5)
                    continue
                

                player.reduce_mp(spell.cost)

                if spell.type == "white":
                    player.heal(magic_dmg)
                    print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
                    time.sleep(0.5)
                elif spell.type == "black":


                    enemy.take_damage(magic_dmg)

                    print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " + enemy.name.replace(" ", "") + bcolors.ENDC)
                    time.sleep(0.5)
                    
                    if enemy.get_hp() == 0:
                        print(bcolors.FAIL + "You won!" + bcolors.ENDC)
                        save_inventory(player_items)
                        time.sleep(0.5)
                        enemy.heal(30000)
                        running = False
                        return True

            elif index == 2:
                player.choose_item()
                item_choice = int(input("    Choose item: ")) - 1

                if item_choice == -1:
                    time.sleep(0.5)
                    continue

                item = player.items[item_choice]["item"]

                if player.items[item_choice]["quantity"] == 0:
                    print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                    enemy.heal(30000)
                    time.sleep(0.5)
                    continue

                player.items[item_choice]["quantity"] -= 1

                if item.type == "potion":
                    player.heal(item.prop)
                    print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
                    time.sleep(0.5)
                elif item.type == "elixer":

                    if item.name == "MegaElixer":
                        for i in players:
                            i.hp = i.maxhp
                            i.mp = i.maxmp
                    else:
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                    print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
                    time.sleep(0.5)
                elif item.type == "attack":
                    enemy.take_damage(item.prop)

                    print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to " + enemy.name + bcolors.ENDC)
                    time.sleep(0.5)
                    if enemy.get_hp() == 0:
                        print(enemy.name.replace(" ", "") + " has died.")



        # Check if Player won
        if enemy.get_hp() == 0:
            print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
            save_inventory(player_items)
            time.sleep(0.5)
            enemy.heal(30000)
            running = False
            return True


        # Check if Enemy won
        elif player.get_hp() == 0:
            print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
            save_inventory(player_items)
            time.sleep(0.5)
            running = False
            return False

        print("\n")
        # Enemy attack phase
        for enemy in enemies:
            enemy_choice = random.randrange(0, 2)

            if enemy_choice == 0:
                # Attack
                enemy_dmg = enemy.generate_damage()

                player.take_damage(enemy_dmg)
                print(enemy.name.replace(" ", "") + " attacks " + player.name.replace(" ", "") + " for", enemy_dmg)
                time.sleep(0.5)

            elif enemy_choice == 1:
                spell, magic_dmg = enemy.choose_enemy_spell()
                enemy.reduce_mp(spell.cost)

                if spell.type == "white":
                    enemy.heal(magic_dmg)
                    print(bcolors.OKBLUE + spell.name + " heals " + enemy.name + " for", str(magic_dmg), "HP." + bcolors.ENDC)
                    time.sleep(0.5)
                elif spell.type == "black":

                    player.take_damage(magic_dmg)

                    print(bcolors.OKBLUE + "\n" + enemy.name.replace(" ", "") + "'s " + spell.name + " deals", str(magic_dmg), "points of damage to " + player.name.replace(" ", "") + bcolors.ENDC)
                    time.sleep(0.5)

                    if player.get_hp() == 0:
                        print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
                        save_inventory(player_items)
                        time.sleep(0.5)
                        running = False
                        return False