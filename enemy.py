import pygame
import math

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

