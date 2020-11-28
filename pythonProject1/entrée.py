import math
import pygame
from game import Game

screen = pygame.display.set_mode((1280, 720))

#importer notre bannière
banner = pygame.image.load("assets/logo2.png")
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/10)
banner_rect.y = math.ceil(screen.get_height()/2)

#charger notre bouton pour lancer la partie
playbutton = pygame.image.load("assets/logo.png")
playbutton = pygame.transform.scale(playbutton, (480, 250))
playbutton_rect = playbutton.get_rect()
playbutton_rect.x = math.ceil(screen.get_width()/3.1)
playbutton_rect.y = math.ceil(screen.get_height()/1.4)

# si le joueur ferme la fenetre
for event in pygame.event.get():
    # si l'evenement est la fermeture de la fenetre par le joueur alors
    if event.type == pygame.QUIT:
        running = False
        pygame.quit()
        print("Fermeture du jeu")
    # detecter si un joueur appuie sur une touche du clavier
    elif event.type == pygame.KEYDOWN:
        game.pressed[event.key] = True

        # detecter si la touche espace est enclenché pour lancer le projectile
        if event.key == pygame.K_SPACE:
            game.player.launch_projectile()

    elif event.type == pygame.KEYUP:
        game.pressed[event.key] = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
# verification si la souris est en collision avec le bouton BRAWL
    if playbutton_rect.collidepoint(event.pos):
    # mette le jeu en mode lancé
        self.is_playing = True

    # charger notre bouton pour lancer la partie
    playbutton = pygame.image.load("assets/logo.png")
    playbutton = pygame.transform.scale(playbutton, (480, 250))
    playbutton_rect = playbutton.get_rect()
    playbutton_rect.x = math.ceil(screen.get_width() / 3.1)
    playbutton_rect.y = math.ceil(screen.get_height() / 1.4)
