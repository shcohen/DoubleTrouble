import pygame
from game import Game

pygame.init()

# generate window
pygame.display.set_caption("Double Trouble")
screen = pygame.display.set_mode((1080, 720))

# generate background
background = pygame.image.load('assets/test000.png')

# generate game
game = Game()

# run game
running = True
while running:

    # apply background
    screen.blit(background, (-100, 0))

    # apply player
    screen.blit(game.player.image, game.player.rect)

    # update player health bar
    game.player.update_health_bar(screen)

    # get player's projectile
    for projectile in game.player.all_projectiles:
        projectile.move()

    # apply all projectiles
    game.player.all_projectiles.draw(screen)

    # generate monster's movements
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # apply all monsters
    game.all_monsters.draw(screen)

    # check directions
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 819:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 178:
        game.player.move_left()

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
