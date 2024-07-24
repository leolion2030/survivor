import pygame
from game_obj import GameObj

class Skill:
    def __init__(self, name, projectile, cooldown):
        self.name = name
        self.base_projectile = projectile
        self.cooldown = cooldown
        self.active_projectiles = []

    def use(self, player):
        center_x = player.global_x + (player.width/2) - (self.base_projectile.width/2)
        center_y = player.global_y + (player.height/2) - (self.base_projectile.height/2)
        new_projectile = self.base_projectile.copy(center_x, center_y , player.direction, player)
        self.active_projectiles.append(new_projectile)
        new_projectile.shoot()

    def update(self, player):
        for bullet in self.active_projectiles:
            bullet.update(player)
            if bullet.active == False:
                self.active_projectiles.remove(bullet)