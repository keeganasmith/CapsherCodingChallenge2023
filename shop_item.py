import pygame


#this represents an indivual tower that could be in the shop so we would have a different class for each shop_tower
class Shop_Item:
    def __init__(self, pos):
        #size of tower in shop
        self.surface = pygame.Surface((70,70))
        self.surface.fill('Orange')
        self.rect = self.surface.get_rect()
        self.rect.topleft = pos
        self.loc = [self.rect.topleft[0], self.rect.topleft[1]]


    def render(self, display):
        display.blit(self.surface, self.rect.topleft)

    def addtower(self):

        #here we need to wait for user to click so we know coordinates to pass back through of where to place tower
        while True:
            for event in pygame.event.get():
                selected = False

                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    selected = True
                
                if selected:
                    print(mouse)
                    return mouse
                
