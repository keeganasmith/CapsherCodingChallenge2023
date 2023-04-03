import pygame
class sell_panel:
    def __init__(self, loc = [1000, 150]):
        self.surface = pygame.image.load("assets/sell_button.png")
        self.loc= loc
    def draw_sell_panel(self, screen, tower):
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.text = self.font.render(f'Refund: {tower.getCost()//2}', True, 'black')
        screen.blit(self.surface, self.loc)
        screen.blit(self.text, (self.loc[0], self.loc[1] + self.surface.get_height()))