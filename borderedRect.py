import pygame

class bordered_rect():
    def __init__(self,left,top,width,height,border_size,inner_color,border_color):
        self.outline_rect = pygame.Rect(left,top,width,height)
        self.inner_rect = pygame.Rect(left-border_size,top-border_size,width-border_size,height-border_size)
        self.inner_color = inner_color
        self.border_color = border_color