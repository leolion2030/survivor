import pygame
from game_obj import GameObj

class Skill:
    def __init__(self, name, projectile, cooldown, shoot_type, hit_type, aoe=None):
        self.name = name
        self.base_projectile = projectile
        self.cooldown = cooldown
        self.active_projectiles = []
        self.shoot_type = shoot_type
        self.hit_type = hit_type
        self.base_aoe = aoe
        self.active_aoe = []

    def use(self, player, nearest=None):
        center_x = player.global_x + (player.width/2) - (self.base_projectile.width/2)
        center_y = player.global_y + (player.height/2) - (self.base_projectile.height/2)
        for type in self.shoot_type:
            if type == "Forward":
                new_projectile = self.base_projectile.copy(center_x, center_y , player.direction, player)

            elif type == "Backward":
                if player.direction == "right":
                    opposite = "left"
                elif player.direction == "left":
                    opposite = "right"
                elif player.direction == "up":
                    opposite = "down"
                elif player.direction == "down":
                    opposite = "up"
                elif player.direction == "upleft":
                    opposite = "downright"
                elif player.direction == "downright":
                    opposite = "upleft"
                elif player.direction == "downleft":
                    opposite = "upright"
                elif player.direction == "upright":
                    opposite = "downleft"
                new_projectile = self.base_projectile.copy(center_x, center_y , opposite, player)

            elif type == "Nearest":
                print(self.calcdirection(player, nearest))
                new_projectile = self.base_projectile.copy(center_x, center_y, self.calcdirection(player, nearest), player)

            self.active_projectiles.append(new_projectile)
            new_projectile.shoot()

    def update(self, player):
        for bullet in self.active_projectiles:
            bullet.update(player)
            if bullet.active == False:
                self.active_projectiles.remove(bullet)
        for aoe in self.active_aoe:
            aoe.update(player)
            if aoe.active == False:
                self.active_aoe.remove(aoe)

    def calcdirection(self, player, enemy):
        if enemy != None:
            difx = enemy.global_x - player.global_x 
            dify = enemy.global_y - player.global_y
            vector = pygame.math.Vector2(difx, dify)
            diff = vector.normalize()
            return [diff.x, diff.y] 