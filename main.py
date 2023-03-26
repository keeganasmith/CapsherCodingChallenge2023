import pygame
import playbutton
import enemy
import lives
import round
import money
# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True


enemies = []
enemies_to_be_deployed = []
#round setup
current_round = round.Round()
#life display:
life_display = lives.Lives(1050, 75)
life_display.lives = 50
life_display.update()

#money display:
money_display = money.Money(1050, 25)
money_display.money = 100

# Red Walls
wall_surface = pygame.Surface((100,720))
wall_surface.fill('Red')
wall_surface2 = pygame.Surface((980,310))
wall_surface2.fill('Red')

# Enemy
#
#NOTE: This should probably be in the enemy class but oh well
#


# Help see waypoints
help_surface = pygame.Surface((50,50))
help_surface.fill('Yellow')

# Can add as many enimies as you want
#enemies.append(enemy.Enemy())

#boolean for keeping track of wave
wave_in_progress = False

play_button = playbutton.play_button();

counter = 0;
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
                current_round.next_round()
                enemies_to_be_deployed = current_round.create_to_be_deployed();
                #print(enemies_to_be_deployed)
    if(len(enemies_to_be_deployed) != 0 and counter % current_round.delay == 0):
        #print("got here\n")
        enemies.append(enemies_to_be_deployed.pop())
    # Does for all enimies
    if(wave_in_progress):
        i = 0
        while(i < len(enemies)):
            #print(str(i) + ":" + enemies[i].to_string())
        # for xy in enemy.path:
            #    screen.blit(help_surface, xy);
            enemies[i].move()
            if(not enemies[i].escaped):
                screen.blit(enemies[i].surface, enemies[i].loc)
                i += 1
            else:
                del enemies[i]
                life_display.lives -= 1;
                life_display.update();
        if(len(enemies_to_be_deployed) == 0 and len(enemies) == 0):
            wave_in_progress = False
    # Red Walss
    screen.blit(wall_surface, (0, 0));
    screen.blit(wall_surface2, (200, 0));
    screen.blit(wall_surface, (1180, 0));
    screen.blit(wall_surface2, (100, 410));
    screen.blit(life_display.text, life_display.loc)
    screen.blit(money_display.text, money_display.loc)
    if(not wave_in_progress):
        screen.blit(play_button.surface, (play_button.loc[0], play_button.loc[1]))

    # flip() the display to put your work on screen
    pygame.display.flip()
    counter += 1
    counter = counter % 2147483647
    clock.tick(60)  # limits FPS to 60

pygame.quit()