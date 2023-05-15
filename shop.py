import pygame, util, borderedRect

class Shop():
    def __init__(self):
        self.shop_rect = borderedRect.bordered_rect((util.window_size[0]/3)*2,0,util.window_size[0]/3,util.window_size[1],util.window_size[0]/384,pygame.color.Color('#D08C39'),(0,0,0))
        self.all_buttons = []
        self.unlocked_buttons = []
        self.current_buttons = []
        self.current_position = 0
        self.minimize = False