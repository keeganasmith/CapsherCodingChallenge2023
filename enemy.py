import pygame
import math

class Enemy:
    def __init__(self):
        # How fast enemy goes
        self.speed = 5
        # Waypoints enemy follows
        self.path = [[125, 0], [125, 335], [1105, 335], [1105, 680]]    
        # Current index in path enemy is heading to
        self.spot = 1
        # Starting point
        self.loc = self.path[0]
        self.surface = pygame.Surface((50,50))
        self.surface.fill('Blue')
        next_point = self.path[self.spot]
        old_point = self.path[self.spot-1]
        if(next_point[0] < old_point[0]):
            self.direction = "Left"
        elif(next_point[0] > old_point[0]):
            self.direction = "Right"
        elif(next_point[1] > old_point[1]):
            self.direction = "Down"
        elif(next_point[1] < old_point[1]):
            self.direction = "Up"
        self.escaped = False
        self.health = 1
        
        self.cp = self.calcCenter()
        
    def move(self):
        # If enemy is at waypoint advance to next waypoint
        if self.spot < len(self.path) and ((self.direction == "Down" and self.loc[1] >= self.path[self.spot][1]) or (self.direction == "Up" and self.loc[1] <= self.path[self.spot][1]) or (self.direction == "Left" and self.loc[0] <= self.path[self.spot][0]) or (self.direction == "Right" and self.loc[0] >= self.path[self.spot][0])):
            self.spot += 1
            if(self.spot < len(self.path)):
                next_point = self.path[self.spot]
                old_point = self.path[self.spot-1]
                if(next_point[0] < old_point[0]):
                    self.direction = "Left"
                elif(next_point[0] > old_point[0]):
                    self.direction = "Right"
                elif(next_point[1] > old_point[1]):
                    self.direction = "Down"
                elif(next_point[1] < old_point[1]):
                    self.direction = "Up"
            if(self.spot == len(self.path)):
                self.escaped = True
        if(self.spot < len(self.path)):
            # Finding angle towards next waypoint
            # bot = self.loc[0]-self.path[self.spot][0]
            # degrs = 0
            # top = self.loc[1]-self.path[self.spot][1]
            
            # If path is horizontal
            # if top == 0:
            #     # To the right
            #     if self.loc[0] < self.path[self.spot][0]:
            #         degrs = math.radians(-90)
            #     #To the left
            #     else:
            #         degrs = math.radians(-90)
            # Else
            # elif bot != 0:
            #     degrs = math.tan(top/bot)
            #print("Degrees: ", degrs)
            #print(self.loc)
            #print("Spot: ", self.spot)
            # Creates new location
            if(self.direction == 'Up'):
                self.loc[1] -= self.speed
                self.cp[1] -= self.speed
            if(self.direction == 'Down'):
                self.loc[1] += self.speed
                self.cp[1] += self.speed
            if(self.direction == 'Left'):
                self.loc[0] -= self.speed
                self.cp[0] -= self.speed
            if(self.direction == 'Right'):
                self.loc[0] += self.speed
                self.cp[0] += self.speed
            #self.loc = (self.loc[0] - self.speed*math.sin(degrs), self.loc[1] + self.speed*math.cos(degrs))
            #print("New Loc: ", self.loc)
        return self.loc
    def out_of_bounds(self, x, y):
        if(self.loc[0] < 0 or self.loc[1] < 0 or self.loc[0] > x or self.loc[1] > y):
            return True
        return False
    def to_string(self):
        return str(self.loc)
    
    def calcCenter(self):
        return [pygame.Surface.get_width(self.surface)//2 + self.loc[0], pygame.Surface.get_height(self.surface)//2 + self.loc[1]]
    
    def get_Center(self):
        return self.cp
    
class Fast_enemy(Enemy):
    def __init__(self):
        super().__init__()
        self.speed = 7
        self.surface = pygame.Surface((50,50))
        self.surface.fill('White')
class Tank_enemy(Enemy):
    def __init__(self):
        super().__init__()
        self.speed = 2
        self.surface = pygame.Surface((50, 50))
        self.surface.fill('Purple')
        self.health = 5
