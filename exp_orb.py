import pygame
from game_obj import GameObj

class ExpOrb(GameObj):
    
    def __init__(self, mob, player, exp_amount):
        self.exp_amount = exp_amount
        super().__init__(mob.global_x, mob.global_y, 15, 15, player, "assets/exp_orb.png")

    def check_collision(self, player):
        collide = self.get_hitbox().colliderect(player.get_hitbox())
        return collide