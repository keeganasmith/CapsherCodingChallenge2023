import pygame

class start_screen:
    def __init__(self):
        self.surface = pygame.image.load("start_screen_background.png")
        self.surface = pygame.transform.scale(self.surface, (1280,720))
        self.loc = [0,0]
        self.start_button = pygame.image.load("Start_button.png")
        self.start_button = pygame.transform.scale(self.start_button, (1280,720))
        self.start_button_loc = [-15, 30]
        self.surface.blit(self.start_button, (self.start_button_loc))