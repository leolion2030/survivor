import pygame
from player import Player
from game_obj import GameObj
from enemy import Enemy
class Game:
    
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000, 1000))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.player = Player(5)
        self.rock = GameObj(100, 100, 35, 35, "assets/Rock.png")
        self.zombie = Enemy(100, 100, 30, 50, "assets/Zombie.png", 3, 5, 20)
        self.street = pygame.image.load("assets/Background.png")
        self.street = pygame.transform.scale(self.street, (1001, 1001))
        self.skill1event = pygame.event.custom_type()
        self.set_up_timer()
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
        self.zombie.update(self.player)
        
    def draw(self):
        self.window.fill((0, 0, 0))
        self.draw_background()
        self.player.draw(self.window)
        self.rock.draw(self.window)
        self.zombie.draw(self.window)
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
        

    def set_up_timer(self): 
        pygame.time.set_timer(self.skill1event, self.player.skill_set[0].cooldown)

    def check_enemies_hit(self):
        if self.zombie.check_collision(self.player.skill_set[0].active_projectiles) == True:
            print("hi")