import pygame, util, math

class MenuButton():
    def __init__(self,name,submenu=None):
        self.name = name
        self.rect = pygame.Rect(0,0,(util.window_size[0]/6)-util.window_size[0]/64,util.window_size[1]/16)
        self.font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(util.window_size[1]/20))
        self.text = self.font.render(name,True,(0,0,0))
        self.text_rect = self.text.get_rect()
        self.submenu = submenu