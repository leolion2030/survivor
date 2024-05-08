import pygame
from player import Player
from game_obj import GameObj
class Game:
    
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000, 800))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.player = Player(5)
        self.rock = GameObj(100, 100, 20, 20)
        self.main_game_loop()

    def main_game_loop(self):
        while True:
            self.clock.tick(self.fps)
            self.event_handler()
            self.key_handler()
            self.update()
            self.draw()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def key_handler(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w] == True:
            self.player.move("up")
        elif pressed_keys[pygame.K_s] == True:
            self.player.move("down")
        if pressed_keys[pygame.K_a] == True:
            self.player.move("left")
        elif pressed_keys[pygame.K_d] == True:
            self.player.move("right")
    
    def update(self):
        self.player.update_display_pos(self.window)
        self.rock.update_display_pos(self.player)

    def draw(self):
        self.window.fill((0, 0, 0))
        self.player.draw(self.window)
        self.rock.draw(self.window)
        pygame.display.update()