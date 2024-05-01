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
        try:
            self.on = util.settings[name]
        except:
            self.on = False

        self.image = pygame.image.load('Assets/shopbutton.png').convert()
        #making a rect to use in transform for sizing
        self.rect = pygame.Rect(0,0,self.text_rect.width + self.on_rect.width + 100,self.text_rect.height + 20)
        self.image = pygame.transform.scale(self.image,[self.rect.width*util.scale[0],self.rect.height*util.scale[1]])
        self.rect = self.image.get_rect()

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
        
    def render(self):
        util.screen.blit(self.image,self.rect)
        util.screen.blit(self.get_image(),self.get_rect())
        util.screen.blit(self.text,self.text_rect)