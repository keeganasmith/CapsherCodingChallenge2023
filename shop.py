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

    #this function is supposed to check if any tower in shop is clicked and then calls the add tower function for that class if it is
    def checkaction(self, mouse, towers):
        #loops through each tower type in panel
        for i in range(len(self.slots)):
            #checks to see if tower type is clicked and adds tower to list if it is
            if self.slots[i].surface.get_rect(topleft = (self.slots[i].loc[0], self.slots[i].loc[1])).collidepoint(mouse[0],mouse[1]):
                coords = self.slots[i].addtower()
                #checks for tower type to know which one to add to list and passes coordinates that it gets from user click
                if i == 0:
                    #adds normal tower to list
                    towers.append(tower.Tower(coords[0],coords[1]))
                #add more if statements for other tower types in shop

        return towers

