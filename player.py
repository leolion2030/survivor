import pygame
from game_obj import GameObj

class Player(GameObj):

    def __init__(self, window):
        w = 35
        h = 35
        x = (window.get_width() / 2) - (w / 2)
        y = (window.get_height() / 2) - (h / 2)
        super().__init__(x, y, w, h)