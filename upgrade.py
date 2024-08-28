import pygame

class Upgrade:
    def __init__(self, x, upg):
        self.x = x
        self.y = 200
        self.width = 250
        self.height = 300
        self.bgcolor = (181, 181, 181)
        self.bg = pygame.image.load("assets/upgrad_bgd.png")
        self.upg = upg
        self.find_upg_img()
        
    def get_hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, window:pygame.Surface):
        pygame.draw.rect(window, self.bgcolor, self.get_hitbox())
        window.blit(self.bg, (self.x, self.y))
        window.blit(self.upg_img, (self.x, self.y))

    def find_upg_img(self):
        match self.upg:
            case "water_gunupg1":
                self.upg_img = pygame.image.load("assets/water_gun1upg.png")
            case "water_gunupg2":
                self.upg_img = pygame.image.load("assets/water_gun2upg.png")
            case _:
                self.upg_img = pygame.image.load("assets/Rock.png")