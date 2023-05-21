import pygame, math, util

class CheckBox():
    def __init__(self,name):
        self.name = name
        self.font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(util.window_size[1]/20))
        self.text = self.font.render(name,True,(0,0,0))
        self.text_rect = self.text.get_rect()

        self.on_image = pygame.image.load('Assets/onbox.png').convert()
        self.on_rect = self.on_image.get_rect()
        self.off_image = pygame.image.load('Assets/offbox.png').convert()
        self.off_rect = self.off_image.get_rect()
        self.on = util.settings[name]

    def get_image(self):
        if self.on:
            return self.on_image
        else:
            return self.off_image
        
    def get_rect(self):
        if self.on:
            return self.on_rect
        else:
            return self.off_rect 