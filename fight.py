from random import randint,choices
from player import stats
import time



def iscrit():
    roll = choices([True,False],[int(stats["crit_chance"]),(100-int(stats["crit_chance"]))])
    return roll

def fight(world,print_world,current_pos,level,health):
    enemy_health = 50
    print("A fight has started!")
    time.sleep(0.5)

    while True:
        action = input("Choose your action (attack/heal): ").strip().lower()
        if action in ["attack", "heal"]:
            break
        else:
            print("Invalid action. Please choose again.")

    if action == "attack": 
        time.sleep(0.5)
        dmg=int(stats["crit_mult"]*stats["base_dmg"]) if iscrit() == True else stats["base_dmg"]
        print(f"You chose to attack! Attacked for {dmg}")
        enemy_health -= dmg
        time.sleep(0.5)


    elif action == "heal":
        time.sleep(0.5)
        heal=randint(1,20)
        print(f"You chose to heal! Healed for +{heal}")
        health+=heal
        time.sleep(0.5)

    world[level][current_pos] = "*"
    print_world(world)