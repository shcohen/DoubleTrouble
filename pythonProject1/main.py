import pygame
from game import Game
pygame.init()
import math

#fenetre
pygame.display.set_caption("SSB ZELDA")
screen = pygame.display.set_mode((1280, 720))

#importer fond d'écran
background = pygame.image.load("assets/SSBU-Yggdrasil'sAltar.jpg")

#importer notre bannière
banner = pygame.image.load("assets/logo2.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width()/3.2
banner_rect.y = screen.get_height()/6

#charger notre bouton pour lancer la partie
playbutton = pygame.image.load("assets/logo.png")
playbutton = pygame.transform.scale(playbutton, (480, 250))
playbutton_rect = playbutton.get_rect()
playbutton_rect.x = math.ceil(screen.get_width()/2.8)
playbutton_rect.y = math.ceil(screen.get_height()/1.5)

#charger notre joueur et jeu
game = Game()


running = True

#boucle tant que fenetre ouverte
while running:
    #appliquer arriere plan du jeu
    screen.blit(background, (0, 0))

    #verifier si notre jeu a commence
    if game.is_playing:
        #déclancher les instructions de la partie
        game.update(screen)
    #verifier si le jeu n'a pas commencé
    else:
        #ajouter écran de bienvenue
        screen.blit(banner, banner_rect)
        screen.blit(playbutton, playbutton_rect)


    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # si l'evenement est la fermeture de la fenetre par le joueur alors
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
