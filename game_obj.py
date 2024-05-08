import pygamejj

class GameObj:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.global_x = x
        self.global_y = y
        
    def get_hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, window):
        pygame.draw.rect(window, (0, 255, 0), self.get_hitbox())