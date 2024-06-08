import pygame
from game_obj import GameObj

class Skill:
    def __init__(self, name, projectile, cooldown):
        self.name = name
        self.base_projectile = projectile
        self.cooldown = cooldown
        self.active_projectiles = []

    def use(self, player):
        new_projectile = self.base_projectile.copy(player.global_x, player.global_y, player.direction)
        self.active_projectiles.append(new_projectile)
        new_projectile.shoot()