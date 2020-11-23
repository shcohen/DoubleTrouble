import pygame
from player import Player
from monster import Monster
import math

#classe qui represente le jeu
class Game:
    def __init__(self):
        #definir si notre jeu a commence ou non
        self.is_playing = False
        #generer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed ={}
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_monster()

    def update(self,screen):
        # charger notre bouton pour lancer la partie
        playbutton = pygame.image.load("assets/logo.png")
        playbutton = pygame.transform.scale(playbutton, (480, 250))
        playbutton_rect = playbutton.get_rect()
        playbutton_rect.x = math.ceil(screen.get_width() / 2.8)
        playbutton_rect.y = math.ceil(screen.get_height() / 1.5)

        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        #actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # récuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstres
        self.all_monsters.draw(screen)

        # verifier si le joueur veut aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 950:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 150:
            self.player.move_left()

        print(self.player.rect.x)

        # mettre a jour l'ecran
        pygame.display.flip()

        # si le joueur ferme la fenetre
        for event in pygame.event.get():
            # si l'evenement est la fermeture de la fenetre par le joueur alors
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu")
            # detecter si un joueur appuie sur une touche du clavier
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True

                # detecter si la touche espace est enclenché pour lancer le projectile
                if event.key == pygame.K_SPACE:
                    self.player.launch_projectile()

            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("pygame.MOUSEBUTTONDOWN")
                #verification si la souris est en collision avec le bouton BRAWL
                if playbutton_rect.collidepoint(event.pos):
                    #mette le jeu en mode lancé
                    self.is_playing = True
                    print("ok")


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)