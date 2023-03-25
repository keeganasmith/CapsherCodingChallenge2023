import pygame
class Lives:
    def __init__(self, x, y):
        self.loc = (x, y);
        self.font = pygame.font.Font('freesansbold.ttf', 32);
        self.lives = 10
        self.text = self.font.render(f'Lives: {self.lives}', True, 'black')
    def update(self):
        self.text = self.font.render(f'Lives: {self.lives}', True, 'black')

