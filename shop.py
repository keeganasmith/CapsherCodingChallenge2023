import pygame
import shop_item
import tower

class Shop:
    #default x_coord and y_coord of top left of shop box
    def __init__(self, x_coord = 300, y_coord = 450):
        self.slots = []

        #this line changes the (width, height) of the shop box
        self.surface = pygame.Surface((700,260))

        self.rect = self.surface.get_rect()
        self.surface.fill('Gray')
        self.rect.topleft = (x_coord, y_coord)

        #self.slots.append(shop_item("Images/coinIcon.png", (10, 360)))
        #self.slots.append(shop_item("Images/manapotionIcon.png", (110, 360)))
        self.slots.append(shop_item.Shop_Item((320, 470)))

        
    def render(self, display):
        display.blit(self.surface, self.rect) 
        for slot in self.slots:
            slot.render(display)
            
    def checkPlacement(self, screen, path_surfaces, coords, width, height):
        rec = pygame.Rect(coords[0]- (width/2), coords[1] - (height/2), width, height)
        bounds = pygame.display.get_surface().get_rect()
        for surface in path_surfaces:
            path = pygame.Rect(surface[1],surface[0].get_size())
            if(rec.colliderect(path)):
                return False;
        return bounds.contains(rec)

    #this function is supposed to check if any tower in shop is clicked and then calls the add tower function for that class if it is
    def checkaction(self, mouse, towers, screen, wall_surfaces, enemies, path_surfaces):
        #loops through each tower type in panel
        for i in range(len(self.slots)):
            #checks to see if tower type is clicked and adds tower to list if it is
            if self.slots[i].surface.get_rect(topleft = (self.slots[i].loc[0], self.slots[i].loc[1])).collidepoint(mouse[0],mouse[1]):
                rec = self.slots[i].surface.get_rect(topleft = (self.slots[i].loc[0], self.slots[i].loc[1]))
                coords = self.slots[i].addtower(screen, wall_surfaces, enemies, towers)
                if(coords == [-2, -2]):
                    return "notexit"
                if(coords == [-1, -1]):
                    return "exit"
                #checks for tower type to know which one to add to list and passes coordinates that it gets from user click
                if i == 0:
                    #adds normal tower to list
                    if self.checkPlacement(screen, path_surfaces, coords, rec.width, rec.height):
                        towers.append(tower.Tower(center_coord= coords))
                #add more if statements for other tower types in shop
                return "notexit"
        return "notexit"
        #return towers
            
            

