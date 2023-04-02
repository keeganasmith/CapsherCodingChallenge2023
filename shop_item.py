import pygame
import tower
background_surface = pygame.image.load("roadmap-new.png")
background_surface = pygame.transform.scale(background_surface, (1280,720))

#this represents an indivual tower that could be in the shop so we would have a different class for each shop_tower
class Shop_Item:
    def __init__(self, pos, tower_type = "norm"):
        #size of tower in shop
        self.tower = tower.Tower()
        
        if(tower_type == "slow"):
            self.tower = tower.slow_tower()
        if(tower_type == "aoe"):
            self.tower = tower.aoe_tower() 
        if(tower_type == "sniper"):
            self.tower = tower.sniper_tower()
        self.cost = self.tower.getCost()
        #if(tower_type == "blah"):
        #   self.tower = tower.blah()
        self.surface = self.tower.surface
        self.rect = self.surface.get_rect()
        self.rect.topleft = pos
        self.loc = [self.rect.topleft[0], self.rect.topleft[1]]

        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.text = self.font.render(f'Cost: {self.cost}', True, 'black')

        self.description = self.font.render(f'Normal Tower: Shoots projectiles at first enemy to come in range', True, 'black')
        if tower_type == "slow":
            self.description = self.font.render(f'Slow Tower: Slows all enemies within range. Slow affect cannot be stacked', True, 'black')
        if tower_type == "aoe":
            self.description = self.font.render(f'Flame Thrower: Shoots a cone of flame at first enemy to come in range', True, 'black')
        if tower_type == "sniper":
            self.description = self.font.render(f'Sniper Tower: Shoots a projectile at the strongest enemy on the screen', True, 'black')
        

    def render(self, display):
        display.blit(self.surface, self.rect.topleft)
        #this line displays cost underneath tower and should auto scale by towers height
        display.blit(self.text, [self.loc[0], self.loc[1]+self.rect.height])

    def show_description(self, mouse,display):
        temp_surface = pygame.Surface(self.description.get_size())
        temp_surface.fill(color='White')
        temp_surface.blit(self.description, (0,0))
        display.blit(temp_surface, [self.loc[0], self.loc[1]-20])


    def addtower(self, screen, wall_surfaces, enemies, towers):

        #here we need to wait for user to click so we know coordinates to pass back through of where to place tower
        
        while True:
            screen.fill(0);

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return [-1, -1]
                selected = False
                if event.type == pygame.KEYDOWN: #they canceled
                    return [-2, -2]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    selected = True
                
                if selected:
                    return mouse
            
             #draw map
            screen.blit(background_surface, (0,0))

            i = 0
            while(i < len(towers)):
                screen.blit(towers[i].surface, towers[i].loc)
                i += 1
            i = 0
            while(i < len(enemies)):
                screen.blit(enemies[i].surface, enemies[i].loc)
                i += 1
            screen.blit(self.tower.surface, (pygame.mouse.get_pos()[0] - (self.tower.surface.get_width() //2 ), pygame.mouse.get_pos()[1] - self.tower.surface.get_height() //2))
            #pygame.draw.circle(screen, "Blue", pygame.mouse.get_pos(), self.tower.range)
            IMAGE = pygame.Surface((2*self.tower.range, 2*self.tower.range), pygame.SRCALPHA)
            pygame.draw.circle(IMAGE, "Blue", (IMAGE.get_width()//2, IMAGE.get_height() //2), self.tower.range)

            alpha_surface = pygame.Surface(IMAGE.get_size(), pygame.SRCALPHA)
            alpha_surface.fill((255, 255, 255, 90))
            
            IMAGE.blit(alpha_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

            screen.blit(IMAGE, (pygame.mouse.get_pos()[0] - IMAGE.get_width()//2, pygame.mouse.get_pos()[1] - IMAGE.get_height()//2))
            font = pygame.font.Font('freesansbold.ttf', 32);
            text = font.render('Press any key to cancel', True, 'black')
            screen.blit(text, (500, 0))
            pygame.display.flip()


