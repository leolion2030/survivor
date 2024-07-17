import pygame
from game_obj import GameObj
from hp_bar import HpBar

class Enemy(GameObj):

    def __init__(self, global_x, global_y, width, height, image, speed, dmg, hp, atk_cd):
        super().__init__(global_x, global_y, width, height, image)
        self.speed = speed
        self.dmg = dmg
        self.max_hp = hp
        self.current_hp = hp
        self.hp_bar = HpBar(self.max_hp)
        self.alive = True
        self.direction = pygame.math.Vector2(0, 0)
        self.atk_cd = atk_cd
        self.atk_ready = False
    
    def take_dmg(self, dmg):
        self.current_hp -= dmg
        #print(f"{self.current_hp}/{self.max_hp} hp")
        if self.current_hp <= 0:
            self.alive = False

    def update(self, player):
        self.calculate_direction(player)
        self.move()
        super().update(player)
        self.check_touching_player(player)
        self.hp_bar.update(self.current_hp)

    def check_touching_player(self, player):
        if self.atk_ready == True:
            if self.get_hitbox().colliderect(player.get_hitbox()):
                player.take_dmg(self.dmg)
                self.atk_ready = False

    def copy(self, x, y):
        copy = Enemy(x, y, self.width, self.height, None, self.speed, self.dmg, self.max_hp, self.atk_cd)
        copy.sprite = self.sprite
        return copy
    
    def calculate_direction(self, player):
        player_center = player.get_center()
        enemie_center = self.get_center()
        diff_x = player_center[0] - enemie_center[0]
        diff_y = player_center[1] - enemie_center[1]
        diff_vector = pygame.math.Vector2(diff_x, diff_y)
        self.direction = diff_vector.normalize()

    def move(self):
        self.global_x += self.direction.x*self.speed
        self.global_y += self.direction.y*self.speed
    
    def start_atk_timer(self, event_timer):
        attribute = {"enemy": self}
        event = pygame.event.Event(event_timer, attribute)
        pygame.time.set_timer(event, self.atk_cd, 1)