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
        
