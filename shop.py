import pygame

class Shop():
    def __init__(self,window_size):
        self.shop_rect = pygame.Rect((window_size[0]/3)*2,0,window_size[0]/3,window_size[1])
        self.all_buttons = []
        self.current_buttons = []
        self.current_position = 0