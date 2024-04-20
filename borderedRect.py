#an artifact from when i needed to test out functionalities before I designed the UI

import pygame

class bordered_rect():
    def __init__(self,left,top,width,height,border_size,inner_color,border_color):
        self.border_rect = pygame.Rect(left,top,width,height)
        self.inner_rect = pygame.Rect(left+border_size,top+border_size,width-border_size*2,height-border_size*2)
        self.inner_color = inner_color
        self.border_color = border_color