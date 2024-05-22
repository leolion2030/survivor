import pygame

class GameObj:

    def __init__(self, global_x, global_y, width, height, image):
        self.width = width
        self.height = height
        self.global_x = global_x
        self.global_y = global_y
        self.display_x = None
        self.display_y = None
        self.sprite = pygame.image.load(image)
        self.sprite = pygame.transform.scale(self.sprite, (width, height))
        
    def get_hitbox(self):
        return pygame.Rect(self.display_x, self.display_y, self.width, self.height)
    
    def draw(self, window:pygame.Surface):
        pygame.draw.rect(window, (0, 255, 0), self.get_hitbox())
        window.blit(self.sprite, (self.display_x, self.display_y))

    def update_display_pos(self, player):
        self.display_x = player.display_x + (self.global_x - player.global_x)
        self.display_y = player.display_y+ (self.global_y - player.global_y)