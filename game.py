import pygame
from player import Player
from game_obj import GameObj
class Game:
    
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1000, 800))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.player = Player(self.window)
        self.test = GameObj(100, 100, 20, 20)
        self.main_game_loop()

    def main_game_loop(self):
        while True:
            self.clock.tick(self.fps)
            self.event_handler()
            self.draw()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def draw(self):
        self.window.fill((0, 0, 0))
        self.player.draw(self.window)
        self.test.draw(self.window)
        pygame.display.update()