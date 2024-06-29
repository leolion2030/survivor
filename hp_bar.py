import pygame

class HpBar:

    def __init__(self, max_hp):
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.hp_width = 50

    def draw(self, window, x, y):
        #TODO adjust to make it centered to character
        red = pygame.Rect(x - 5, y - 10, self.hp_width, 5)
        #TODO adjust width based on health
        green_width = (self.current_hp / self.max_hp) * self.hp_width
        green = pygame.Rect(x - 5, y - 10, green_width, 5)
        pygame.draw.rect(window, (255, 0, 0), red)
        pygame.draw.rect(window, (0, 255, 0), green)
        
    def update(self, current_hp):
        self.current_hp = current_hp