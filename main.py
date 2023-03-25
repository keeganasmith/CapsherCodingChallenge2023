import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

test_surface = pygame.image.load("map.png");
enemy_surface = pygame.image.load("enemy.png");
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #screen.fill("blue")

    screen.blit(test_surface, (0, 0));
    screen.blit(enemy_surface, (0, 400));
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()