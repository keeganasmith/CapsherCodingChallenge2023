import pygame
import math
class Projectile:
    def __init__(self, angle, loc, damage = 10, shot_speed = 20, sprite = pygame.Surface((20, 20))):
        self.damage = damage
        self.shot_speed = shot_speed
        self.sprite = sprite
        self.angle = angle
        self.loc = loc
        self.sprite.fill('Yellow')
        
    def update(self):
        self.loc = (self.loc[0] + self.shot_speed*math.cos(self.angle), self.loc[1] + self.shot_speed*math.sin(self.angle))
        
    def draw(self, scr):
        scr.blit(self.sprite, self.loc);