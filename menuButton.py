import pygame, util, math

class MenuButton():
    def __init__(self,name,submenu=None):
        self.name = name
        self.image = pygame.image.load('Assets/shopbutton.png').convert()
        #making a rect to use in transform for sizing
        self.rect = pygame.Rect(0,0,(util.window_size[0]/6)-util.window_size[0]/64,util.window_size[1]/16)
        self.image = pygame.transform.scale(self.image,[self.rect.width*util.scale[0],self.rect.height*util.scale[1]])
        self.rect = self.image.get_rect()

        self.font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(util.window_size[1]/20))
        self.text = self.font.render(name,True,(0,0,0))
        self.text_rect = self.text.get_rect()
        
        self.submenu = submenu

    def render(self):
        util.screen.blit(self.image,self.rect)
        util.screen.blit(self.text,self.text_rect)