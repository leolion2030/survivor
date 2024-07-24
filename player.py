import pygame
from skill import Skill
from game_obj import GameObj
from projectile import Projectile
from hp_bar import HpBar

class Player(GameObj):

    def __init__(self, speed, window):
        super().__init__(0, 0, 50, 50, image="assets/Slime.png")
        self.update_display_pos(window)
        self.direction = "up"
        self.speed = speed
        water_gun = Skill("Water Gun", Projectile(self.global_x, self.global_y, 10, 10, self, "assets/Bullet.png", 10, 25, self.direction, 500), 100)
        self.skill_set = [water_gun]
        self.max_hp = 1000
        self.current_hp = self.max_hp  
        self.hp_bar = HpBar(self.max_hp)

    def update_display_pos(self, window):
        self.display_x = (window.get_width() / 2) - (self.width / 2)
        self.display_y = (window.get_height() / 2) - (self.height / 2)

    def move(self, direction):
        self.direction = direction
        # x = sqrt(speed^2/2)
        if direction == "upright":
            self.global_x += self.speed
            self.global_y -= self.speed
        elif direction == "upleft":
            self.global_x -= self.speed
            self.global_y -= self.speed
        elif direction == "downright":
            self.global_x += self.speed
            self.global_y += self.speed
        elif direction == "downleft":
            self.global_x -= self.speed
            self.global_y += self.speed
        elif direction == "left":
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
            skill.update(self)
        self.hp_bar.update(self.current_hp)

    def take_dmg(self, dmg):
        self.current_hp -= dmg
        print(f"{self.current_hp}/{self.max_hp} hp")
        if self.current_hp <= 0:
            self.alive = False