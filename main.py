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
import sell_tower
import round_display
import asyncio
# pygame setup
async def main():
    pygame.init()
    WIDTH = 1280
    HEIGHT = 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    start_display = start_screen.start_screen()
    enemies = []
    enemies_to_be_deployed = []

    victory_display = pygame.image.load("assets/victory.png")
    lost_display = pygame.image.load("assets/lose.png")
    #round setup
    current_round = round.Round()
    #life display:
    life_display = lives.Lives(1050, 75)
    life_display.lives = 20
    life_display.update()

    #money display:
    money_display = money.Money(1050, 25)
    money_display.money = 100

    #round display:
    round_dis = round_display.round_display(1050, 125)
    round_dis.rounds = 1
    round_dis.update()

    #sell button
    sell_panel = sell_tower.sell_panel()
    sell_panel.loc = [1050, 150]
    #boolean for when round finishes to update money
    round_finish = False

    # Path of enemies
    path_surface = pygame.Surface((82,558))
    path_surface2 = pygame.Surface((240,80))
    path_surface3 = pygame.Surface((80,352))
    path_surface4 = pygame.Surface((450,80))
    path_surface5 = pygame.Surface((80,272))
    path_surface6 = pygame.Surface((428,80))
    path_surfaces = [[path_surface, (80, 0)], [path_surface2, (162, 478)], [path_surface3, (322, 126)], [path_surface4, (402, 126)], [path_surface5, (772, 206)], [path_surface6, (852, 398)]]

    #this is updated background
    background_surface = pygame.image.load("assets/roadmap-new.png")
    background_surface = pygame.transform.scale(background_surface, (1280,720))

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

    victory = False
    lost = False
    num_snipers = [0]
    slow_tower_id = [1]
    while running:
        await asyncio.sleep(0)
        # resets screen
        screen.fill(0)

        #print(pygame.mouse.get_pos())
        
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if(not_started):
                    if(start_display.start_button.get_rect(topleft = start_display.start_button_loc).collidepoint(mouse)):
                        not_started = False
                    continue
                if(victory):
                    if(mouse[0] <= 200 and mouse[0] >= 20 and mouse[1] >= 610 and mouse[1] <= 670):
                        victory = False
                        not_started = True
                    continue
                if(lost):
                    if(mouse[0] <= 200 and mouse[0] >= 20 and mouse[1] >= 610 and mouse[1] <= 670):
                        lost = False
                        not_started = True
                    continue
                if(tower_selected):
                    if(sell_panel.surface.get_rect(topleft = sell_panel.loc).collidepoint(mouse)):
                        towers.remove(selected_tower)
                        money_display.money += selected_tower.getCost()//2
                        money_display.update()
                        tower_selected = False
                tower_selected = False
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
                    #sets this so that when round ends it will update money
                    round_finish = True
                    enemies_to_be_deployed = current_round.create_to_be_deployed();
                    #print(enemies_to_be_deployed)
                
                #this checks to see if player clicked on any towers in shop
                if shop_open:
                    result = await shop_panel.checkaction(mouse, towers, screen, enemies, path_surfaces, money_display, num_snipers, slow_tower_id) 
                    money_display.update();
                    if(result == "exit"):
                        running = False
                #code to open shop on clicking the shop or close the shop depending on current state
                if (not shop_open) and shop_button.surface.get_rect(topleft = (shop_button.loc[0], shop_button.loc[1])).collidepoint(mouse[0],mouse[1]):
                    #opens shop
                    shop_open = True
                    
                    #print(shop_open)
                elif (shop_open) and shop_button.surface.get_rect(topleft = (shop_button.loc[0], shop_button.loc[1])).collidepoint(mouse[0],mouse[1]):
                    #closes shop
                    shop_open = False
                    #print(shop_open)

            #end mouse down if statement
        #end event if statement
        #display victory screen/reset stuff
        if(lost):
            screen.blit(lost_display, (0, 0))
            
            pygame.display.flip()
            clock.tick(60)
            continue
        if(life_display.lives == 0):
            screen.blit(lost_display, (0, 0))
            towers = []
            money_display.money = 100
            money_display.update()
            current_round = round.Round()
            lost = True
            shop_open = False
            life_display.lives = 20
            life_display.update()
            round_dis.rounds = 1
            round_dis.update()
            enemies_to_be_deployed = []
            enemies = []
            projectiles_on_screen = []
            round_finish = False
            wave_in_progress = False
            continue
        if(victory):
            screen.blit(victory_display, (0,0))
            pygame.display.flip()
            clock.tick(60)
            continue;
        if((not wave_in_progress) and current_round.current_round == len(current_round.rounds)):
            #print("got here\n")
            screen.blit(victory_display, (0, 0))
            towers = []
            money_display.money = 100
            money_display.update()
            current_round = round.Round()
            victory = True
            shop_open = False
            life_display.lives = 20
            life_display.update()
            round_dis.rounds = 1
            round_dis.update()
            round_finish = False
            pygame.display.flip()
            clock.tick(60)
            continue
        if(not_started):

            screen.blit(start_display.surface, (0, 0))
            pygame.display.flip()
            clock.tick(60)
            continue;
        # Red Walls
        
        #should display road map
        screen.blit(background_surface, (0,0))
        
        # for surface in path_surfaces:
        #     screen.blit(surface[0], surface[1])     

        if(len(enemies_to_be_deployed) != 0 and counter % current_round.delay == 0):
            #print("got here\n")
            #print(len(enemies_to_be_deployed))
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
                    money_display.money += 4
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
                round_dis.rounds += 1
                round_dis.update()
                projectiles_on_screen = []
            i = 0
            while(i < len(towers)):
                if(towers[i].type == "aoe"):
                    proj = towers[i].shoot(enemies)
                    if proj is None:
                        i += 1
                        continue
                    screen.blit(proj.sprite, proj.loc)
                    i += 1
                    continue
                if(towers[i].type == "sniper"):
                    towers[i].shoot(enemies, projectiles_on_screen, game_counter = counter);
                    i += 1
                    continue
                towers[i].shoot(enemies, projectiles_on_screen)
                i += 1
            i = 0
            while(i < len(projectiles_on_screen)):
                projectiles_on_screen[i].update()
                projectiles_on_screen[i].draw(screen)
                i +=1
            
        

        screen.blit(life_display.text, life_display.loc)
        screen.blit(money_display.text, money_display.loc)
        screen.blit(round_dis.text, round_dis.loc)
        screen.blit(shop_button.surface, (shop_button.loc[0], shop_button.loc[1]))
        i = 0
        while(i < len(towers)):
            screen.blit(towers[i].surface, towers[i].loc)
            i += 1
        if(not wave_in_progress):
            screen.blit(play_button.surface, (play_button.loc[0], play_button.loc[1]))
            if round_finish == True:
                #this line gives 50 dollars after a round finishes so we can change value to balance game
                money_display.money += 20
                money_display.update()
                round_finish = False
        
        if shop_open:
            shop_panel.render(screen)
            mouse_ps = pygame.mouse.get_pos()
            shop_panel.checkhover(mouse_ps, screen)

        if tower_selected:
            radius.tower_is_selected(screen, selected_tower)
            sell_panel.draw_sell_panel(screen, selected_tower)
        # flip() the display to put your work on screen
        pygame.display.flip()
        counter += 1
        counter = counter % 2147483647
        clock.tick(60)  # limits FPS to 60

    pygame.quit()
    
if __name__ == "__main__":
    asyncio.run(main())