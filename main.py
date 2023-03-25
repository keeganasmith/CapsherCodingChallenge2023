import pygame
import playbutton
import enemy
# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

enemies = []



# Red Walls
wall_surface = pygame.Surface((100,720))
wall_surface.fill('Red')
wall_surface2 = pygame.Surface((980,310))
wall_surface2.fill('Red')

# Enemy
#
#NOTE: This should probably be in the enemy class but oh well
#
enemy_surface = pygame.Surface((50,50))
enemy_surface.fill('Blue')

# Help see waypoints
help_surface = pygame.Surface((50,50))
help_surface.fill('Yellow')

# Can add as many enimies as you want
enemies.append(enemy.Enemy())

#boolean for keeping track of wave
wave_in_progress = False

play_button = playbutton.play_button();


while running:
    # resets screen
    screen.fill(0)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            
            if((not wave_in_progress) and play_button.surface.get_rect(topleft = (play_button.loc[0], play_button.loc[1])).collidepoint(mouse[0],mouse[1])):
                wave_in_progress = True
                #start wave
                
    # Does for all enimies
    if(wave_in_progress):
        i = 0
        while(i < len(enemies)):
        # for xy in enemy.path:
            #    screen.blit(help_surface, xy);
            enemies[i].move()
            if(enemies[i].loc != enemies[i].path[len(enemies[i].path)-1]):
                screen.blit(enemy_surface, enemies[i].loc)
                i += 1
            else:
                del enemies[i]
    # Red Walss
    screen.blit(wall_surface, (0, 0));
    screen.blit(wall_surface2, (200, 0));
    screen.blit(wall_surface, (1180, 0));
    screen.blit(wall_surface2, (100, 410));
    if(not wave_in_progress):
        screen.blit(play_button.surface, (play_button.loc[0], play_button.loc[1]))

    # flip() the display to put your work on screen
    pygame.display.flip()
    
    clock.tick(60)  # limits FPS to 60

pygame.quit()