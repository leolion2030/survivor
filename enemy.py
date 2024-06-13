import pygame
from game_obj import GameObj

class Enemy(GameObj):

    def __init__(self, global_x, global_y, width, height, image, speed, dmg, hp):
        super().__init__(global_x, global_y, width, height, image)
        self.speed = speed
        self.dmg = dmg
        self.max_hp = hp
        self.current_hp = hp
    
    def take_dmg(self, dmg):
        self.current_hp -= dmg
        print(self.current_hp + "/" + self.max_hp)
        if self.current_hp <= 0:
            pass