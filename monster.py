import pygame
import random


# generate second player aka IA
class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.1
        self.velocity = 0.1
        self.image = pygame.image.load('assets/ganon.png')
        self.image = pygame.transform.scale(self.image, (180, 180))
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = 200

    def damage(self, amount):
        # inflict damages
        self.health -= amount

        # check if monster should still be alive
        if self.health <= 0:
            # respawn as new monster
            self.rect.x = 700 + random.randint(0, 200)
            self.rect.y = 300
            self.health = self.max_health

            # si barre d'evenements chargée
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)

                # appel de la methode pour lancer la pluie de comete
                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):
        # define health bar position, width and height
        bar_position = [(self.rect.x + 35), (self.rect.y - 10), self.health, 5]
        # define background of health bar
        back_bar_position = [(self.rect.x + 35), (self.rect.y - 10), self.max_health, 5]

        # draw health bar
        pygame.draw.rect(surface, (60, 63, 60), back_bar_position)
        pygame.draw.rect(surface, (111, 210, 46), bar_position)

    def forward(self):
        # moving forward only if there's no collision
        if not self.game.check_collision(self, self.game.all_players):
            if self.rect.x > 50:
                self.rect.x -= self.velocity
            # making the monster fall
            elif self.rect.x == 50:
                self.rect.y += 1

        # if there's a collision
        else:
            self.game.player.damage(self.attack)

    # check if monster is still on screen
        if self.rect.y >= 600:
            # remove monster from screen
            self.remove()
