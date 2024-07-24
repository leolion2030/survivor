import pygame
from game_obj import GameObj
from hp_bar import HpBar

class Enemy(GameObj):

    def __init__(self, global_x, global_y, width, height, player, image, speed, dmg, hp, atk_cd):
        super().__init__(global_x, global_y, width, height, player, image)
        self.speed = speed
        self.dmg = dmg
        self.max_hp = hp
        self.current_hp = hp
        self.hp_bar = HpBar(self.max_hp)
        self.alive = True
        self.direction = pygame.math.Vector2(0, 0)
        self.atk_cd = atk_cd
        self.atk_ready = False
        self.current_frame = 0
    
    def take_dmg(self, dmg):
        self.current_hp -= dmg
        #print(f"{self.current_hp}/{self.max_hp} hp")
        if self.current_hp <= 0:
            self.alive = False

    def update(self, player):
        self.calculate_direction(player)
        self.move()
        super().update(player)
        if self.atk_ready == False:
            self.current_frame += 1
            if self.current_frame == self.atk_cd:
                self.atk_ready = True
                self.hitbox_color = (0, 0, 255)
                self.current_frame = 0
                
        self.check_touching_player(player)
        self.hp_bar.update(self.current_hp)

    def check_touching_player(self, player):
        if self.atk_ready == True:
            if self.get_hitbox().colliderect(player.get_hitbox()):
                player.take_dmg(self.dmg)
                self.atk_ready = False
                self.hitbox_color = (0, 255, 0)

    def copy(self, x, y, player):
        copy = Enemy(x, y, self.width, self.height, player, None, self.speed, self.dmg, self.max_hp, self.atk_cd)
        copy.sprite = self.sprite
        return copy
    
    def calculate_direction(self, player):
        player_center = player.get_center()
        enemie_center = self.get_center()
        diff_x = player_center[0] - enemie_center[0]
        diff_y = player_center[1] - enemie_center[1]
        diff_vector = pygame.math.Vector2(diff_x, diff_y)
        if not (diff_vector.x == 0 and diff_vector.y == 0):
            self.direction = diff_vector.normalize()

    def move(self):
        self.global_x += self.direction.x*self.speed
        self.global_y += self.direction.y*self.speed