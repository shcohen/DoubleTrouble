import pygame
import random

#créer une classe qui va gere le monstre sur le jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 15
        self.image = pygame.image.load("assets/Ganondorf.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1050 + random.randint(0,200)
        self.rect.y = 205
        self.velocity = random.randint(1, 2)

    def damage(self,amount):
        #infliger les degats
        self.health -= amount

        #verifier si son nouveau nombre de points de vie est inferieur ou egal a 0
        if self.health <= 0:
            #réaparaitre comme un nouveau monstre
            self.rect.x = 950 + random.randint(0,200)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health


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


    def forward(self):
        #le deplacement ne se fait que s'il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

