from game_obj import GameObj

class Projectile(GameObj):

    def __init__(self, x, y, width, height, image, speed, dmg, direction):
        super().__init__(x, y, width, height, image)
        self.speed = speed
        self.dmg = dmg
        self.direction = direction
        self.active = False

    def shoot(self):
        self.active = True

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
            