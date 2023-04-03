import pygame


class shop_button:
    def __init__(self, x_coord = 150, y_coord = 600):
        self.surface = pygame.image.load("assets/tower_shop_button.png");

        self.loc = [x_coord, y_coord]