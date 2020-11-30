import pygame
from player import Player
from monster import Monster
from comet import Comet
from comet_event import CometFallEvent

# generate game
class Game:
    def __init__(self):
        # check if game has started
        self.is_playing = False
        # check if game_over banner must be loaded
        self.restart = False
        # generate Player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer comete
        self.comet_event = CometFallEvent(self)
        # create monster group
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.all_monsters = pygame.sprite.Group()
        self.spawn_monster()
        self.player.rect.x = 350
        self.player.rect.y = 300

    # restart game
    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.restart = True

    # generate game
    def update(self, screen):
        # apply player
        screen.blit(self.player.image, self.player.rect)

        # update player health bar
        self.player.update_health_bar(screen)

        # get player's projectile
        for projectile in self.player.all_projectiles:
            projectile.move()

        # apply all projectiles
        self.player.all_projectiles.draw(screen)

        # generate comets
        for comet in self.comet_event.all_comets:
            comet.fall()

        # refresh comets
        self.comet_event.update_bar(screen)

        # apply comets
        self.comet_event.all_comets.draw(screen)

        # generate monster's movements
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # apply all monsters
        self.all_monsters.draw(screen)

        # check directions
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 810 and self.player.rect.y == 300:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 120:
            self.player.move_left()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x == 120 or self.player.rect.x <= 120:
            self.player.fall()

    # check collision
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # generate Monster
    def spawn_monster(self):
        self.all_monsters.add(Monster(self))