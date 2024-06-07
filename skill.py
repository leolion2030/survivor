import pygame
from game_obj import GameObj

class Skill:
    def __init__(self, name, projectile, cooldown):
        self.name = name
        self.projectile = projectile
        self.cooldown = cooldown

    def use(self):
        self.projectile.shoot()