import pygame

class HpBar:

    def __init__(self, max_hp):
        self.max_hp = max_hp
        self.current_hp = max_hp

    def draw(self, window, x, y):
        #TODO adjust to make it centered to character
        red = pygame.Rect(x - 5, y - 10, 50, 5)
        #TODO adjust width based on health
        green = pygame.Rect(x - 5, y - 10, 50, 5)
        pygame.draw.rect(window, (255, 0, 0), red)
        pygame.draw.rect(window, (0, 255, 0), green)
        
    def update(self, current_hp):
        self.current_hp = current_hp