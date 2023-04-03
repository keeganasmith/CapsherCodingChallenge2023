import pygame
class round_display:
    def __init__(self, x, y):
        self.loc = (x, y)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.rounds = 10
        self.text = self.font.render(f'Round: {self.rounds}', True, 'black')
    def update(self):
        self.text = self.font.render(f'Round: {self.rounds}', True, 'black')