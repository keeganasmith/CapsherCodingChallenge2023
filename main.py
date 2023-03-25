import pygame
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

enemies = []


class Enemy:
    def __init__(self):
        # How fast enemy goes
        self.speed = 5
        # Waypoints enemy follows
        self.path = [(125, 0), (125, 335), (1105, 335), (1105, 680)]    
        # Current index in path enemy is heading to
        self.spot = 1
        # Starting point
        self.loc = self.path[0]
        
    def move(self):
        # If enemy is at waypoint advance to next waypoint
        if self.spot < len(self.path) and self.loc == self.path[self.spot]:
            self.spot += 1
        if(self.spot < len(self.path)):
            # Finding angle towards next waypoint
            bot = self.loc[0]-self.path[self.spot][0]
            degrs = 0
            top = self.loc[1]-self.path[self.spot][1]
            
            # If path is horizontal
            if top == 0:
                # To the right
                if self.loc[0] < self.path[self.spot][0]:
                    degrs = math.radians(-90)
                #To the left
                else:
                    degrs = math.radians(-90)
            # Else
            elif bot != 0:
                degrs = math.tan(top/bot)
            print("Degrees: ", degrs)
            print(self.loc)
            print("Spot: ", self.spot)
            # Creates new location
            self.loc = (self.loc[0] - self.speed*math.sin(degrs), self.loc[1] + self.speed*math.cos(degrs))
            print("New Loc: ", self.loc)
        return self.loc


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
enemies.append(Enemy())
while running:
    # resets screen
    screen.fill(0)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Does for all enimies
    for enemy in enemies:
       # for xy in enemy.path:
        #    screen.blit(help_surface, xy);
        coords = enemy.move()
        
    # Red Walss
    screen.blit(wall_surface, (0, 0));
    screen.blit(wall_surface2, (200, 0));
    screen.blit(wall_surface, (1180, 0));
    screen.blit(wall_surface2, (100, 410));
    
    screen.blit(enemy_surface, coords);

    # flip() the display to put your work on screen
    pygame.display.flip()
    
    clock.tick(60)  # limits FPS to 60

pygame.quit()