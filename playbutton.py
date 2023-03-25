import pygame


class play_button:
    def __init__(self, x_coord = 20, y_coord = 600):
        self.surface = pygame.image.load("wave_start.png");

        self.loc = [x_coord, y_coord]