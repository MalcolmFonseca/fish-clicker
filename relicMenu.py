import pygame,util

class RelicMenu():
    def __init__(self):
        #book menu
        self.image = pygame.image.load('Assets/temple/relicmenu.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,[self.rect.width*util.scale[0],self.rect.height*util.scale[1]])
        self.rect = self.image.get_rect()

        self.enabled = False

        #close button
        self.close_button = pygame.image.load('Assets/temple/closerelicmenu.png').convert_alpha()
        self.close_button_rect = self.close_button.get_rect()
        self.close_button = pygame.transform.scale(self.close_button,[self.close_button_rect.width*util.scale[0],self.close_button_rect.height*util.scale[1]])
        self.close_button_rect = self.close_button.get_rect()
        self.close_button_rect.center = [util.window_size[0]-util.window_size[0]/8,util.window_size[0]/12]

    def render(self):
        #render menu box
        util.screen.blit(self.image,self.rect)
        #render close button
        util.screen.blit(self.close_button,self.close_button_rect)