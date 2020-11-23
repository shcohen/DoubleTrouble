import pygame
from projectile import Projectile


#classe pour le joueur
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 150
        self.max_health = 150
        self.attack = 10
        self.velocity = 2.5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets/Zelda_Rod_-_HW.png")
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 220

    def damage(self, amount):
        if self.health - amount > amount:
            self.health-= amount

    def update_health_bar(self,surface):
        #definir une couleur pour la jauge de vie(vert)
        bar_color = (52,255,1)

        #definir couleur pour arrière plan de la jauge
        back_bar_color =(255,174,1)

        #definir la position de la jauge de vie ainsi que sa largeur et son epaisseur
        bar_position = [self.rect.x +70, self.rect.y -10, self.health, 5]

        #definir position de l'arrère plan de la jauge de vie
        back_bar_position = [self.rect.x + 70, self.rect.y - 10, self.max_health, 5]

        #dessiner la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def launch_projectile(self):
        #creer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        #si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity