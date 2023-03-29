import pygame
import tower

#this represents an indivual tower that could be in the shop so we would have a different class for each shop_tower
class Shop_Item:
    def __init__(self, pos, tower_type = "norm"):
        #size of tower in shop
        self.tower = tower.Tower()
        
        #if(tower_type == "blah"):
        #   self.tower = tower.blah()
        self.surface = self.tower.surface
        self.rect = self.surface.get_rect()
        self.rect.topleft = pos
        self.loc = [self.rect.topleft[0], self.rect.topleft[1]]
        self.cost = 50

    def render(self, display):
        display.blit(self.surface, self.rect.topleft)

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
                    #print(mouse)
                    return mouse
            
            for surface in wall_surfaces: #draw map
                screen.blit(surface[0], surface[1])
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
            screen.blit(text, (600, 200))
            pygame.display.flip()


