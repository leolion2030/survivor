import pygame
from game_obj import GameObj

class Skill(GameObj):

    def __init__(speed, x, y, width, height, name, dmg, projectiles, image):
        super().__init__(x, y, width, height, image)