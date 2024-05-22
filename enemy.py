import pygame
from game_obj import GameObj

class Enemy(GameObj):

    def __init__(self, global_x, global_y, width, height, image, speed, dmg, hp):
        super().__init__(global_x, global_y, width, height, image)
        self.speed = speed
        self.dmg = dmg
        self.max_hp = hp
        self.current_hp = hp
    