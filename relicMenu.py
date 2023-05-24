import pygame,util

class RelicMenu():
    def __init__(self):
        self.image = pygame.image.load('Assets/temple/relicmenu.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.enabled = False
        self.close_button = pygame.image.load('Assets/temple/closerelicmenu.png').convert_alpha()
        self.close_button_rect = self.close_button.get_rect()
        self.close_button_rect.center = [util.window_size[0]-util.window_size[0]/8,util.window_size[0]/12]

    def render(self):
        #render menu box
        util.screen.blit(self.image,self.rect)
        #render close button
        util.screen.blit(self.close_button,self.close_button_rect)