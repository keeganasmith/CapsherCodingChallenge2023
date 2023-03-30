import pygame

class start_screen:
    def __init__(self):
        self.surface = pygame.image.load("start_screen_background.png")
        self.loc = [0,0]
        self.start_button = pygame.image.load("Start button.png")
        self.start_button_loc = [600, 350]
        self.surface.blit(self.start_button, (self.start_button_loc))