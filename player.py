import pygame
import math
from skill import Skill
from game_obj import GameObj
from projectile import Projectile
from hp_bar import HpBar
from exp_bar import ExpBar
from aoe import AOE

class Player(GameObj):

    def __init__(self, speed, window, level_up_event):
        super().__init__(0, 0, 50, 50, image="assets/Slime.png")
        self.update_display_pos(window)
        self.direction = "up"
        self.speed = speed
        self.water_gun = Skill(
            "Water Gun", 
            Projectile(self.global_x, self.global_y, 10, 10, self, "assets/Bullet.png", 10, 25, self.direction, 500),
            1000,
            ["Forward"],
            ["Single"]
        )
        self.fire_potion = Skill(
            "Fire Potion", 
            Projectile(self.global_x, self.global_y, 50, 50, self, "assets/potion/frame_00_delay-0.4s.png", 10, 25, self.direction, 750),
            2000, 
            ["Nearest"],
            ["Aoe"],
            aoe = AOE(self.global_x, self.global_y, 40, 40, self, "assets/Rock.png", 150, 15, 30)
        )
        self.skill_set = [self.water_gun]
        self.max_hp = 1000
        self.current_hp = self.max_hp  
        self.hp_bar = HpBar(self.max_hp)
        self.exp = 0
        self.level = 0
        self.exp_require = 25
        self.exp_bar = ExpBar(self.exp, self.exp_require, self.level)
        self.level_up_event = level_up_event

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
        self.exp_bar.update(self.exp, self.exp_require, self.level)

    def take_dmg(self, dmg):
        self.current_hp -= dmg
        print(f"{self.current_hp}/{self.max_hp} hp")
        if self.current_hp <= 0:
            self.alive = False

    def gain_exp(self, exp_amount):
        self.exp += exp_amount
        if self.exp >= self.exp_require:
            pygame.event.post(pygame.event.Event(self.level_up_event))
            self.level += 1
            self.exp_require = math.ceil(self.exp_require + (self.exp_require * 1.25))

    def gain_upg(self, upg):
        match upg:
            case "water_gunupg1":
                self.skill_set[0].cooldown -= 150
                if self.skill_set[0].cooldown < 1:
                    self.skill_set[0].cooldown = 1
            case "water_gunupg2":
                self.skill_set[0].shoot_type.append("Backward")

    def gain_skill(self, skill):
        match skill:
            case "fire_potion":
                self.skill_set.append(self.fire_potion)
                