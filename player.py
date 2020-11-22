import pygame
from projectile import Projectile


# generate player
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/test1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 300

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount

    def update_health_bar(self, surface):
        # define health bar position, width and height
        bar_position = [(self.rect.x), (self.rect.y - 10), self.health, 7]
        # define background of health bar
        back_bar_position = [(self.rect.x), (self.rect.y - 10), self.max_health, 7]

        # draw health bar
        pygame.draw.rect(surface, (60, 63, 60), back_bar_position)
        pygame.draw.rect(surface, (111, 210, 46), bar_position)

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # check if
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
