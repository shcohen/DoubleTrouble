import pygame


# define projectile of the player
class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 1.5
        self.player = player
        self.image = pygame.image.load('assets/attack.png')
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 169
        self.rect.y = player.rect.y
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # make projectile rotate
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # check if projectile is colliding with monster
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # delete projectile
            self.remove()
            # inflict damages
            monster.damage(self.player.attack)

        # check if projectile is still on screen
        if self.rect.x > 600:
            # delete projectile
            self.remove()
            print("Projectile removed")
