import pygame
import playbutton
import enemy
import lives
import round
import money
import tower
import collisions
import shopbutton
import shop
import radius
import start_screen
# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

start_display = start_screen.start_screen()
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
wall_surfaces = [[wall_surface, [0, 0]], [wall_surface2, [200, 0]], [wall_surface, [1180, 0]], [wall_surface2, [100, 410]]]

path_surface = pygame.Surface((100,310))
path_surface.fill('Black')
path_surface2 = pygame.Surface((1080,100))
path_surface2.fill('Black')
path_surfaces = [[path_surface, (100, 0)], [path_surface, (1080, 410)], [path_surface2, (100, 310)]]
#towers
towers = []
# Help see waypoints
help_surface = pygame.Surface((50,50))
help_surface.fill('Yellow')

# Can add as many enimies as you want
#enemies.append(enemy.Enemy())
projectiles_on_screen = []
#boolean for keeping track of wave
wave_in_progress = False
shop_open = False

play_button = playbutton.play_button();

shop_button = shopbutton.shop_button()

shop_panel = shop.Shop()
tower_selected = False
selected_tower = tower.Tower()
counter = 0;

not_started = True;
while running:
    # resets screen
    screen.fill(0)
    
    # for surface in path_surfaces:
    #      screen.blit(surface[0], surface[1])
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            tower_selected = False
            mouse = pygame.mouse.get_pos()
            if(not_started):
                if(start_display.start_button.get_rect(topleft = start_display.start_button_loc).collidepoint(mouse)):
                    not_started = False
            for tow in towers: #checks if a tower has been selected and displays the towers radius
                #print("got here")
                if(tow.surface.get_rect(topleft = tow.loc).collidepoint(mouse)):
                    #print("got here")
                    tower_selected = True;
                    selected_tower = tow;
            if((not wave_in_progress) and play_button.surface.get_rect(topleft = (play_button.loc[0], play_button.loc[1])).collidepoint(mouse[0],mouse[1])): #Checks if the player has pressed the round start button, if so, starts playing
                wave_in_progress = True
                #start wave
                current_round.next_round()
                enemies_to_be_deployed = current_round.create_to_be_deployed();
                #print(enemies_to_be_deployed)
            
            #this checks to see if player clicked on any towers in shop
            if shop_open:
                result = shop_panel.checkaction(mouse, towers, screen, wall_surfaces, enemies, path_surfaces, money_display) 
                money_display.update();
                if(result == "exit"):
                    running = False
            #code to open shop on clicking the shop or close the shop depending on current state
            if (not shop_open) and shop_button.surface.get_rect(topleft = (shop_button.loc[0], shop_button.loc[1])).collidepoint(mouse[0],mouse[1]):
                #opens shop
                shop_open = True
                print(shop_open)
            elif (shop_open) and shop_button.surface.get_rect(topleft = (shop_button.loc[0], shop_button.loc[1])).collidepoint(mouse[0],mouse[1]):
                #closes shop
                shop_open = False
                print(shop_open)

    if(not_started):

        screen.blit(start_display.surface, (0, 0))
        pygame.display.flip()
        clock.tick(60)
        continue;
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
            j = 0;
            collisions.collision_detection(enemies[i], projectiles_on_screen)
            if(enemies[i].health <= 0):
                del enemies[i]
                money_display.money += 10
                money_display.update();
            elif(not enemies[i].escaped):
                screen.blit(enemies[i].surface, enemies[i].loc)
                i += 1
            else:
                del enemies[i]
                life_display.lives -= 1;
                life_display.update();
        if(len(enemies_to_be_deployed) == 0 and len(enemies) == 0):
            wave_in_progress = False
        i = 0
        while(i < len(towers)):
            towers[i].shoot(enemies, projectiles_on_screen)
            i += 1
        i = 0
        while(i < len(projectiles_on_screen)):
            projectiles_on_screen[i].update()
            projectiles_on_screen[i].draw(screen)
            i +=1
        
    # Red Walls
    for surface in wall_surfaces:
        screen.blit(surface[0], surface[1])

    screen.blit(life_display.text, life_display.loc)
    screen.blit(money_display.text, money_display.loc)
    screen.blit(shop_button.surface, (shop_button.loc[0], shop_button.loc[1]))
    i = 0
    while(i < len(towers)):
        screen.blit(towers[i].surface, towers[i].loc)
        i += 1
    if(not wave_in_progress):
        screen.blit(play_button.surface, (play_button.loc[0], play_button.loc[1]))
    
    if shop_open:
        shop_panel.render(screen)

    if tower_selected:
        radius.tower_is_selected(screen, selected_tower)

    # flip() the display to put your work on screen
    pygame.display.flip()
    counter += 1
    counter = counter % 2147483647
    clock.tick(60)  # limits FPS to 60

pygame.quit()