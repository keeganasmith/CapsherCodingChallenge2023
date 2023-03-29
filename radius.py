import pygame

def tower_is_selected(screen, tow):
    IMAGE = pygame.Surface((2*tow.range, 2*tow.range), pygame.SRCALPHA)
    pygame.draw.circle(IMAGE, "Blue", (IMAGE.get_width()//2, IMAGE.get_height() //2), tow.range)
    alpha_surface = pygame.Surface(IMAGE.get_size(), pygame.SRCALPHA)
    alpha_surface.fill((255, 255, 255, 90))
    IMAGE.blit(alpha_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    screen.blit(IMAGE, (tow.loc[0] - (tow.range - tow.surface.get_width()//2), tow.loc[1] - (tow.range - tow.surface.get_height()//2)))
    #print("got here")