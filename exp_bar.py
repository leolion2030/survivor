import pygame
import math

class ExpBar:
    def __init__(self, exp_amount, exp_needed, level):
        self.exp_amount = exp_amount
        self.exp_needed = exp_needed
        self.level = level
        self.width = 800

    def draw(self, window):
        exp_need = pygame.Rect(100, 800, self.width, 20)
        if self.level > 0:
            past_exp = 250*math.pow(1.25, self.level - 1)
        else:
            past_exp = 0

        percnt = ((self.exp_amount - past_exp)/(self.exp_needed - past_exp)) * self.width
        exp_have = pygame.Rect(100, 800, percnt, 20)
        pygame.draw.rect(window, (0, 0, 0), exp_need)
        pygame.draw.rect(window, (0, 255, 0), exp_have)

    def update(self, exp, exp_needed, level):
        self.exp_amount = exp
        self.exp_needed = exp_needed
        self.level = level