import pygame

#definir classe qui gere le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    #defirnir le constructeur de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 4
        self.player = player
        self.image = pygame.image.load("assets/word-image-1362.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 160
        self.rect.y = player.rect.y
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
    #faire tourner le projectile
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    #bouger le projectile
    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #venir verifier si projectile rentre en collision avec un monstre
        for monster in self.player.game.check_collision(self,self.player.game.all_monsters):
            #supprimer le projectile
            self.remove()
            #infliger des degats
            monster.damage(self.player.attack)

        #condition pour verifier si projectile n'est plus présent sur l'ecran
        if self.rect.x > 1080:
            #supprimer le projectile en dehors de l'écran
            self.remove()
            print("projectile supprimé")


