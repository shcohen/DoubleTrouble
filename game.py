import pygame
from player import Player
from monster import Monster


# generate game
class Game:
    def __init__(self):
        # generate Player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # create monster group
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    # check collision
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # generate Monster
    def spawn_monster(self):
        self.all_monsters.add(Monster(self))