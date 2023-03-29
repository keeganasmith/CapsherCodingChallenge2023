import pygame

class Money:
    def __init__(self, x, y):
        self.loc = (x, y);
        self.font = pygame.font.Font('freesansbold.ttf', 32);
        self.money = 100
        self.text = self.font.render(f'Money: {self.money}', True, 'black')
    def update(self):
        self.text = self.font.render(f'Money: {self.money}', True, 'black')
