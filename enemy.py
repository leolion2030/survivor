import pygame
from game_obj import GameObj
from hp_bar import HpBar

class Enemy(GameObj):

    def __init__(self, global_x, global_y, width, height, image, speed, dmg, hp):
        super().__init__(global_x, global_y, width, height, image)
        self.speed = speed
        self.dmg = dmg
        self.max_hp = hp
        self.current_hp = hp
        self.hp_bar = HpBar(self.max_hp)
        self.alive = True
    
    def take_dmg(self, dmg):
        self.current_hp -= dmg
        print(f"{self.current_hp}/{self.max_hp} hp")
        if self.current_hp <= 0:
            self.alive = False

    def update(self, player, window):
        super().update(player)
        self.hp_bar.update(self.current_hp)
        