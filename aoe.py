import pygame
from game_obj import GameObj

class AOE(GameObj):

    def __init__(self, x, y, width, height, player, image, duration, dmg, dmgtick):
        super().__init__(x, y, width, height, player, image)
        self.duration = duration
        self.dmg = dmg
        self.dmgtick = dmgtick
        self.active = False
        self.curframe = 0
        self.dealdmg = False

    def start(self):
        self.active = True


    def stop(self):
        self.active = False

    def copy(self, x, y, player):
        copy_aoe = AOE(x, y, self.width, self.height, player, None, self.duration, self.dmg, self.dmgtick)
        copy_aoe.sprite = self.sprite
        return copy_aoe

    def update(self, player):
        self.update_display_pos(player)
        if self.active == True:
            if self.curframe % self.dmgtick == 0:
                self.dealdmg = True
            else:
                self.dealdmg = False 
            self.curframe += 1
            if self.curframe >= self.duration:
                self.stop()
            