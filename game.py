import pygame
from player import Player
from game_obj import GameObj
from enemy import Enemy
from exp_orb import ExpOrb
import random
class Game:
    
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000, 1000))
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.player = Player(5, self.window)
        self.rock = GameObj(100, 100, 35, 35, self.player, "assets/Rock.png")
        self.base_zombie = Enemy(100, 100, 30, 50, self.player, "assets/Zombie.png", 3, 15, 50, 30)
        self.mob_list = []
        self.orb_list = []

        self.street = pygame.image.load("assets/Background.png")
        self.street = pygame.transform.scale(self.street, (1001, 1001))

        self.skill1event = pygame.event.custom_type()
        self.spawn_event = pygame.event.custom_type()
        self.set_up_timers()

        self.main_game_loop()

    def main_game_loop(self):
        while True:
            self.clock.tick(self.fps)
            self.event_handler()
            self.key_handler()
            self.update()
            self.check_enemies_hit()
            self.draw()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == self.skill1event:
                self.player.skill_set[0].use(self.player)
            elif event.type == self.spawn_event:
                self.spawn_enemies()

    def key_handler(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w] == True and pressed_keys[pygame.K_d] == True:
            self.player.move("upright")
        elif pressed_keys[pygame.K_w] == True and pressed_keys[pygame.K_a] == True:
            self.player.move("upleft")
        elif pressed_keys[pygame.K_s] == True and pressed_keys[pygame.K_d] == True:
            self.player.move("downright")
        elif pressed_keys[pygame.K_s] == True and pressed_keys[pygame.K_a] == True:
            self.player.move("downleft")
        elif pressed_keys[pygame.K_w] == True:
            self.player.move("up")
        elif pressed_keys[pygame.K_s] == True:
            self.player.move("down")
        elif pressed_keys[pygame.K_a] == True:
            self.player.move("left")
        elif pressed_keys[pygame.K_d] == True:
            self.player.move("right")
    
    def update(self):
        self.player.update(self.window)
        self.rock.update(self.player)
        for orb in self.orb_list:
            orb.update(self.player)
            if orb.check_collision(self.player):
                self.player.gain_exp(orb.exp_amount)
                self.orb_list.remove(orb)
                print(self.player.exp)
        for mob in self.mob_list:
            mob.update(self.player)
            if mob.alive == False:
                exp_orb = ExpOrb(mob, self.player, 25)
                self.orb_list.append(exp_orb)
                self.mob_list.remove(mob)
        
    def draw(self):
        self.window.fill((0, 0, 0))
        self.draw_background()
        self.player.draw(self.window)
        self.player.hp_bar.draw(self.window, self.player.display_x, self.player.display_y)
        self.player.exp_bar.draw(self.window)
        self.rock.draw(self.window)
        for mob in self.mob_list:
            if mob.alive == True:
                mob.draw(self.window)
                mob.hp_bar.draw(self.window, mob.display_x, mob.display_y)
        for orb in self.orb_list:
            orb.draw(self.window)
        self.draw_projectiles()
        pygame.display.update()

    def draw_projectiles(self):
        for skill in self.player.skill_set:
            for projectile in skill.active_projectiles:
                projectile.draw(self.window)

    def draw_background(self):
        q1 = (0 - self.player.global_x % 1000, 0 - self.player.global_y % 1000)
        q2 = (1000 - self.player.global_x % 1000, 0 - self.player.global_y % 1000)
        q3 = (0 - self.player.global_x % 1000, 1000 - self.player.global_y % 1000)
        q4 = (1000 - self.player.global_x % 1000, 1000 - self.player.global_y % 1000)
        self.window.blit(self.street, q1)
        self.window.blit(self.street, q2)
        self.window.blit(self.street, q3)
        self.window.blit(self.street, q4)
        

    def set_up_timers(self): 
        pygame.time.set_timer(self.skill1event, self.player.skill_set[0].cooldown)
        pygame.time.set_timer(self.spawn_event, 3000)

    def check_enemies_hit(self):
        for mob in self.mob_list:
            if mob.alive == True:
                used_projectile = mob.check_collision(self.player.skill_set[0].active_projectiles)
                if  used_projectile != None:
                    mob.take_dmg(used_projectile.dmg)

    def spawn_enemies(self):
        amount_copy = 2
        for i in range(amount_copy):
            self.spawn_randomly(self.base_zombie)

    def spawn_randomly(self, base_mob):
        side = random.choice(["top", "left", "bottom", "right"])
        if side == "top":
            y = 0 - base_mob.height
            x = random.randrange(0 - base_mob.width, self.window.get_width())
        if side == "bottom":
            y = self.window.get_height()
            x = random.randrange(0 - base_mob.width, self.window.get_width())
        if side == "left":
            y = random.randrange(0 - base_mob.height, self.window.get_height())
            x = 0 - base_mob.width
        if side == "right":
            y = random.randrange(0 - base_mob.height, self.window.get_height())
            x = self.window.get_width()
        global_x_y = self.convert_display_to_global(x, y)
        new_mob = self.base_zombie.copy(global_x_y[0], global_x_y[1], self.player)
        self.mob_list.append(new_mob)

    def convert_global_to_display(self, global_x, global_y):
        #TODO: implement function
        return
    
    def convert_display_to_global(self, display_x, display_y):
        dif_x = self.player.display_x - display_x
        dif_y = self.player.display_y - display_y
        global_x = self.player.global_x + dif_x
        global_y = self.player.global_y + dif_y
        return [global_x, global_y]