import pygame
import math
class Projectile:
    def __init__(self, angle,x_direction, y_direction, loc, damage = 10, shot_speed = 20, sprite = pygame.Surface((20, 20))):
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
        self.sprite = pygame.Surface((150, 100), pygame.SRCALPHA)
        pygame.draw.polygon(self.sprite, "Orange", [[0,0],[0,100],[150,75],[150,25]])
        #print(self.angle)
        self.angle = math.degrees(self.angle)
        #print(self.angle)
        if(x_direction == -1 and y_direction != -1):
            self.angle = 360 - self.angle
        elif(x_direction == 1 and y_direction == 1):
            self.angle = 180 + self.angle
        elif(x_direction == 1 and y_direction == -1):
            self.angle = 180 - self.angle
        print(self.angle)
        self.sprite = self.rotate(self.sprite, self.angle)
        self.loc = [self.loc[0] - 150, self.loc[1] - 100]
    def rotate(self, image,angle):
        img2 = pygame.Surface((image.get_width()*2, image.get_height()*2), pygame.SRCALPHA)
        img2.blit(image, (0, image.get_height()-image.get_height()//2))
        return pygame.transform.rotate(img2, angle)
