import pygame
from game_obj import GameObj

class Player(GameObj):

    def __init__(self, speed):
        super().__init__(0, 0, 50, 50, "assets/Slime.png")
        self.speed = speed

    def update_display_pos(self, window):
        self.display_x = (window.get_width() / 2) - (self.width / 2)
        self.display_y = (window.get_height() / 2) - (self.height / 2)

    def move(self, direction):
        if direction == "left":
            self.global_x -= self.speed
        elif direction == "right":
            self.global_x += self.speed
        elif direction == "up":
            self.global_y -= self.speed
        elif direction == "down":
            self.global_y += self.speed