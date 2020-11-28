import pygame
import math
from game import Game

pygame.init()

# generate window
pygame.display.set_caption("Double Trouble")
screen = pygame.display.set_mode((1080, 720))

# generate background
background = pygame.image.load('assets/test000.png')

# generate starting banner
banner = pygame.image.load('assets/banner0.png')
banner = pygame.transform.scale(banner, (1080, 720))

# import loading game's button
play_button = pygame.image.load('assets/play1.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 1.6)
play_button_rect.y = math.ceil(screen.get_height() / 1.28)

# generate game_over's banner
go_img = pygame.image.load('assets/game_over.png')
go_img = pygame.transform.scale(go_img, (1080, 720))

# generate game
game = Game()

# run game
running = True
while running:

    # apply background
    screen.blit(background, (-100, 0))

    # check if game has started
    if game.is_playing:
        # start instructions
        game.update(screen)
    else:
        if not game.restart:
            # add starting banner
            screen.blit(banner, (0, 0))
            screen.blit(play_button, play_button_rect)
        else:
            # add game_over banner
            screen.blit(go_img, (0, 0))
            screen.blit(play_button, play_button_rect)

    # update screen
    pygame.display.flip()

    # if player closes window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Closing game.")

        # detect player drops key
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detect if space touch is being used
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if mouse is on play button
            if play_button_rect.collidepoint(event.pos):
                # start game
                game.start()

