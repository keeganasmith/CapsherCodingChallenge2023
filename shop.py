import pygame
import shop_item
import tower
import money

class Shop:
    #default x_coord and y_coord of top left of shop box
    def __init__(self, x_coord = 300, y_coord = 450):
        self.slots = []

        #this line changes the (width, height) of the shop box
        self.surface = pygame.Surface((700,260))

        self.rect = self.surface.get_rect()
        self.surface.fill('Gray')
        self.rect.topleft = (x_coord, y_coord)

        self.slots.append(shop_item.Shop_Item((320, 470)))
        slow_tower_loc = 320 + tower.Tower().surface.get_width() + 10;
        self.slots.append(shop_item.Shop_Item((slow_tower_loc, 470), "slow"))
        aoe_tower_loc = slow_tower_loc + tower.slow_tower().surface.get_width() + 10
        self.slots.append(shop_item.Shop_Item((aoe_tower_loc, 470), "aoe"))
        sniper_tower_loc = aoe_tower_loc + tower.aoe_tower().surface.get_width() + 10
        self.slots.append(shop_item.Shop_Item((sniper_tower_loc, 470), "sniper"))
        
    def render(self, display):
        display.blit(self.surface, self.rect) 
        for slot in self.slots:
            slot.render(display)
            
    def checkPlacement(self, screen, path_surfaces, coords, width, height, towers):
        rec = pygame.Rect(coords[0]- (width/2), coords[1] - (height/2), width, height)
        bounds = pygame.display.get_surface().get_rect()
        for surface in path_surfaces:
            path = pygame.Rect(surface[1],surface[0].get_size())
            if(rec.colliderect(path)):
                return False;
        for tower in towers:
            if(rec.colliderect(tower.surface.get_rect(topleft = tower.loc))):
                return False
        return bounds.contains(rec)
    
    #check if user is hovering over tower then calls towers show_description function
    def checkhover(self,mouse, screen):
        for i in range(len(self.slots)):

            if self.slots[i].surface.get_rect(topleft = (self.slots[i].loc[0], self.slots[i].loc[1])).collidepoint(mouse[0],mouse[1]):
                self.slots[i].show_description(mouse, screen)


    #this function is supposed to check if any tower in shop is clicked and then calls the add tower function for that class if it is
    def checkaction(self, mouse, towers, screen, wall_surfaces, enemies, path_surfaces, cash, sniper_number, slow_tower_id):
        #loops through each tower type in panel
        for i in range(len(self.slots)):
            #checks to see if tower type is clicked and adds tower to list if it is
            if self.slots[i].surface.get_rect(topleft = (self.slots[i].loc[0], self.slots[i].loc[1])).collidepoint(mouse[0],mouse[1]):
                if(cash.money < self.slots[i].cost):
                    return "notexit"
                rec = self.slots[i].surface.get_rect(topleft = (self.slots[i].loc[0], self.slots[i].loc[1]))
                coords = self.slots[i].addtower(screen, wall_surfaces, enemies, towers)
                if(coords == [-2, -2]):
                    return "notexit"
                if(coords == [-1, -1]):
                    return "exit"
                #checks for tower type to know which one to add to list and passes coordinates that it gets from user click
                if i == 0:
                    #adds normal tower to list
                    if self.checkPlacement(screen, path_surfaces, coords, rec.width, rec.height, towers) and cash.money >= self.slots[i].cost:
                        tow = tower.Tower(center_coord= coords)
                        towers.append(tow)
                        cash.money -= tow.getCost()
                        
                #add more if statements for other tower types in shop
                if i == 1:
                    if self.checkPlacement(screen, path_surfaces, coords, rec.width, rec.height, towers):
                        tow = tower.slow_tower(center_coords = coords, tower_id = slow_tower_id[0])
                        towers.append(tow)
                        cash.money -= tow.getCost()
                        slow_tower_id[0] += 1
                if i ==2:
                    if self.checkPlacement(screen, path_surfaces, coords, rec.width, rec.height, towers):
                        tow = tower.aoe_tower(center_coords= coords)
                        towers.append(tow)
                        cash.money -= tow.getCost()
                if i==3:
                    if self.checkPlacement(screen, path_surfaces, coords, rec.width, rec.height, towers):
                        tow = tower.sniper_tower(center_coords = coords, sniper_number = sniper_number[0])
                        sniper_number[0] += 1
                        towers.append(tow)
                        cash.money -= tow.getCost()

                return "notexit"
        return "notexit"
        #return towers
            
            

