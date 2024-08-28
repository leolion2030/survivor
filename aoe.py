import pygame
from game_obj import GameObj

class AOE(GameObj):

    def __init__(self, x, y, width, height, player, image, duration, dmg, dmgtick):
        super().__init__(x, y, width, height, player, image)
        self.duration = duration
        self.dmg = dmg
        self.dmgtick = dmgtick

