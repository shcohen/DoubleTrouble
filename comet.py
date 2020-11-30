import pygame
import random


class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 5)
        self.rect.x = random.randint(0, 1920)
        self.rect.y = - random.randint(500, 1080)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

        # check if more comets
        if len(self.comet_event.all_comets) == 0:
            print("event done")
            # reset bar
            self.comet_event.reset_percent()
            # respawn monster
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()

    def fall(self):
        self.rect.y += self.velocity
        # won't fall on the ground
        if self.rect.y >= 500:
            print("ground")
            self.remove()

        # more comets
        if len(self.comet_event.all_comets) == 0:
            print("event done")
            self.comet_event.reset_percent()
            self.comet_event.fall_mode = False

        # check if comet is touching player
        if self.comet_event.game.check_collision(
                self, self.comet_event.game.all_players
        ):
            print("player")
            self.remove()
            self.comet_event.game.player.damage(30)