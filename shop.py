import pygame, settings

class Shop():
    def __init__(self):
        self.shop_rect = pygame.Rect((settings.window_size[0]/3)*2,0,settings.window_size[0]/3,settings.window_size[1])
        self.all_buttons = []
        self.current_buttons = []
        self.current_position = 0
        self.minimize = False