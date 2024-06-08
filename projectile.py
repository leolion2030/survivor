from game_obj import GameObj

class Projectile(GameObj):

    def __init__(self, x, y, width, height, image, speed, dmg, direction, max_range):
        super().__init__(x, y, width, height, image)
        self.speed = speed
        self.dmg = dmg
        self.direction = direction
        self.active = False
        self.max_range = max_range

    def shoot(self):
        self.active = True
        
    def copy(self, x, y, direction):
        copy = Projectile(x, y, self.width, self.height, None, self.speed, self.dmg, direction, self.max_range)
        copy.sprite = self.sprite
        return copy

    def reset(self):
        pass

    def update(self, player):
        self.update_display_pos(player)
        if self.active == True:
            if self.direction == "up":
                self.global_y -= self.speed
            elif self.direction == "down":
                self.global_y += self.speed
            elif self.direction == "left":
                self.global_x -= self.speed
            elif self.direction == "right":
                self.global_x += self.speed
            