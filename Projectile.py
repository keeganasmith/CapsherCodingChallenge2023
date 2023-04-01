import pygame
import math
class Projectile:
    def __init__(self, angle,x_direction, y_direction, loc, damage = 50, shot_speed = 20, sprite = pygame.Surface((20, 20))):
        self.damage = damage
        self.shot_speed = shot_speed
        self.sprite = sprite
        self.angle = angle
        self.loc = loc
        self.sprite.fill('Yellow')
        self.rect = self.sprite.get_rect(topleft = self.loc)
        self.x_dir = x_direction
        self.y_dir = y_direction
    def update(self):
        self.loc = (self.loc[0] + self.x_dir * self.shot_speed*math.cos(self.angle), self.loc[1] + self.y_dir * self.shot_speed*math.sin(self.angle))
        self.rect = self.sprite.get_rect(topleft = self.loc)
    def draw(self, scr):
        scr.blit(self.sprite, self.loc);

class flame(Projectile):
    def __init__(self, angle, x_direction, y_direction, loc):
        super().__init__(angle, x_direction, y_direction, loc)
        self.WIDTH = 150;
        self.HEIGHT = 100
        self.sprite = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        pygame.draw.polygon(self.sprite, "Orange", [[0,0],[0,self.HEIGHT],[self.WIDTH,self.HEIGHT//2]])
        #print(self.angle)
        self.angle = math.degrees(self.angle)
        self.center = loc
        #print(self.angle)
        if(x_direction == -1 and y_direction == 1): #enemy is in bottom left quadrant 
            self.angle = self.angle
        elif(x_direction == 1 and y_direction == 1): #enemy is in bottom right quadrant
            self.angle = 180 - self.angle
        elif(x_direction == 1 and y_direction == -1): #enemy is in top right quadrant
            self.angle = 180 + self.angle
        elif(x_direction == -1 and y_direction == -1): #enemy is in top left quadrant
            self.angle = 360 - self.angle
        #print(self.angle)
        self.sprite = self.rotate(self.sprite, self.angle)
        rect = self.sprite.get_rect(center = loc)
        self.loc = rect.topleft;
    def rotate(self, image,angle):
        img2 = pygame.Surface((image.get_width()*2, image.get_height()*2), pygame.SRCALPHA)
        img2.blit(image, (0, image.get_height()-image.get_height()//2))
        return pygame.transform.rotate(img2, angle)

    def hits(self, enemy):
        angle_to_enemy = self.calcAngle(enemy)
        lowerbound_angle = self.angle - math.degrees(math.atan((.5 * self.WIDTH)/(self.HEIGHT)))
        upperbound_angle = self.angle + math.degrees(math.atan((.5 * self.WIDTH)/(self.HEIGHT)))
        max_distance = (self.HEIGHT**2 + .25 * self.WIDTH**2) ** .5
        if(angle_to_enemy >= lowerbound_angle and angle_to_enemy <= upperbound_angle and self.distance_to(enemy) <= max_distance):
            return True
        return False
    def calcAngle(self, enemy):
        
        centp = enemy.get_Center()
        bot = abs(self.center[0]- centp[0])
        degrs = 0
        top = abs(self.center[1]-centp[1])
        horizontal_coefficient = 1
        vertical_coefficient = 1
        if(top == 0):
            top = .00001
        if(bot == 0):
            bot = .00001
        if(self.center[0] > centp[0]):
            horizontal_coefficient = -1

        if(self.center[1] > centp[1]):
            vertical_coefficient = -1
        
        degrs = math.degrees(math.atan(top/bot))
        if(horizontal_coefficient == -1 and vertical_coefficient == 1): #enemy is in bottom left quadrant 
            degrs = degrs
        elif(horizontal_coefficient == 1 and vertical_coefficient == 1): #enemy is in bottom right quadrant
            degrs = 180 - degrs
        elif(horizontal_coefficient and vertical_coefficient == -1): #enemy is in top right quadrant
            degrs = 180 + degrs
        elif(horizontal_coefficient == -1 and vertical_coefficient == -1): #enemy is in top left quadrant
            degrs = 360 - degrs
        return degrs
    def distance_to(self, enemy):
        enemy_center = enemy.calcCenter();
        dist = ((enemy_center[0] - self.center[0])**2 + (enemy_center[1] - self.center[1])**2) ** .5
        return dist