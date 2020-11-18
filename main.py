import pygame

pygame.init()


# generate player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_heath = 100
        self.attack = 10
        self.velocity = 4


# generate window
pygame.display.set_caption("Double Trouble")
screen = pygame.display.set_mode((1080, 720))

# generate background
background = pygame.image.load('assets/background1.jpg')

# run game
running = True
while running:

    # apply background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # if player closes window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Closing game.")
