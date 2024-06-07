import pygame
from skill import Skill
from game_obj import GameObj
from projectile import Projectile

class Player(GameObj):

    def __init__(self, speed):
        super().__init__(0, 0, 50, 50, "assets/Slime.png")
        self.direction = "up"
        self.speed = speed
        water_gun = Skill("Water Gun", Projectile(self.global_x, self.global_y, 10, 10, "assets/Bullet.png", 10, 25, self.direction), 2000)
        self.skill_set = [water_gun]  

    def update_display_pos(self, window):
        self.display_x = (window.get_width() / 2) - (self.width / 2)
        self.display_y = (window.get_height() / 2) - (self.height / 2)

    def move(self, direction):
        self.direction = direction
        if direction == "left":
            self.global_x -= self.speed
        elif direction == "right":
            self.global_x += self.speed
        elif direction == "up":
            self.global_y -= self.speed
        elif direction == "down":
            self.global_y += self.speed

    def update(self, window):
        self.update_display_pos(window)
        for skill in self.skill_set:
            skill.projectile.update(self)