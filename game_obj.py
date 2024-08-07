import pygame

class GameObj:

    def __init__(self, global_x, global_y, width, height, player = None, image = None):
        self.width = width
        self.height = height
        self.global_x = global_x
        self.global_y = global_y
        self.display_x = None
        self.display_y = None
        if player != None:
            self.update_display_pos(player)
        self.hitbox_color = (0, 255, 0)
        if image != None:
            self.sprite = pygame.image.load(image)
            self.sprite = pygame.transform.scale(self.sprite, (width, height))
        
    def get_hitbox(self):
        return pygame.Rect(self.display_x, self.display_y, self.width, self.height)
    
    def draw(self, window:pygame.Surface):
        pygame.draw.rect(window, self.hitbox_color, self.get_hitbox())
        window.blit(self.sprite, (self.display_x, self.display_y))

    def update(self, player):
        self.update_display_pos(player)

    def update_display_pos(self, player):
        self.display_x = player.display_x + (self.global_x - player.global_x)
        self.display_y = player.display_y+ (self.global_y - player.global_y)
    
    def check_collision(self, projectile_list):
        #TODO: collide with multiple bullets
        hitbox_list = []
        for projectile in projectile_list:
            if projectile.active == True:
                hitbox_list.append(projectile.get_hitbox())

        collide = self.get_hitbox().collidelist(hitbox_list)

        if collide == -1:
            return None
        else:
            projectile_list[collide].hit()
            return projectile_list[collide]
        
    def get_center(self):
        x = self.global_x + self.width/2
        y = self.global_y + self.height/2
        xy = (x, y)
        return xy