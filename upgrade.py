import pygame

class Upgrade:
    def __init__(self, x):
        self.x = x
        self.y = 20
        self.width = 100
        self.height = 500
        self.bgcolor = (181, 181, 181)
        
    def get_hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, window:pygame.Surface):
        pygame.draw.rect(window, self.bgcolor, self.get_hitbox())