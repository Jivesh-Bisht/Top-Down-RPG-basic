from essentials import player,gate,obstacles,levelCleared,enemy,print_world,border,levelFailed
import time
from fight import fightt as fight
from os import name,system


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class Collision:
    def __init__(self,world,level,current_pos,health):
        self.level = level
        self.health = health
        self.world = world
        self.current_pos=current_pos

    def leftCollision(self):
        level = self.level
        current_pos=self.current_pos
        world=self.world

        if current_pos == 0:
            clear()
            print_world(world)
        else:
            clear()
            if world[level][current_pos-1] in obstacles or world[level][current_pos-1]==border:
                print_world(world)
            elif world[level][current_pos-1] == gate:
                raise levelCleared
            elif world[level][current_pos-1] == enemy:
                k = fight()
                if k:
                    world[level][current_pos] = "."
                    world[level][current_pos-1] = player # remove the enemy
                    clear()
                    print_world(world)
                else:
                    raise levelFailed
                
            else:
                world[level][current_pos] = "."
                world[level][current_pos-1] = player
                print_world(world)
            time.sleep(0.1)

    def rightCollision(self):
        level = self.level
        current_pos=self.current_pos
        world=self.world

        if current_pos == len(world[0])-1:
            clear()
            print_world(world)
        else:
            clear()
            if world[level][current_pos+1] in obstacles or world[level][current_pos+1]==border:
                print_world(world)
            elif world[level][current_pos+1] == gate:
                raise levelCleared
            elif world[level][current_pos+1] == enemy:
                k = fight()
                if k:
                    world[level][current_pos] = "."
                    world[level][current_pos+1] = player # remove the enemy
                    clear()
                    print_world(world)
                else:
                    raise levelFailed
            else:
                world[level][current_pos] = "."
                world[level][current_pos+1] = player
                print_world(world)
            time.sleep(0.1)
    
    def upCollision(self):
        level = self.level
        current_pos=self.current_pos
        world=self.world
        if level == 0:
            clear()
            print_world(world)
        else:
            clear()
            if world[level-1][current_pos] in obstacles or world[level-1][current_pos]==border:
                print_world(world)
            elif world[level-1][current_pos] == gate:
                raise levelCleared
            elif world[level-1][current_pos] == enemy:
                k = fight()
                if k:
                    world[level][current_pos] = "."
                    world[level-1][current_pos] = player # remove the enemy
                    clear()
                    print_world(world)
                else:
                    raise levelFailed
            else:
                world[level][current_pos] = "."
                world[level-1][current_pos] = player
                print_world(world)
            time.sleep(0.1)

    def downCollision(self):
        level = self.level
        current_pos=self.current_pos
        world=self.world

        if level == (len(world)-1):
            clear()
            print_world(world)
        else:
            clear()
            if world[level+1][current_pos] in obstacles or world[level+1][current_pos] == border:
                print_world(world)
            elif world[level+1][current_pos] == gate:
                raise levelCleared
            elif world[level+1][current_pos] == enemy:
                k = fight()
                if k:
                    world[level][current_pos] = "."
                    world[level+1][current_pos] = player # remove the enemy
                    clear()
                    print_world(world)
                else:
                    raise levelFailed

            else:
                world[level][current_pos] = "."
                world[level+1][current_pos] = player
                print_world(world)
            time.sleep(0.1)