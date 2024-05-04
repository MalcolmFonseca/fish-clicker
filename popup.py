import pygame, math, util

class Popups():
    def __init__(self):
        self.popup_group = pygame.sprite.Group()

    def create_popup(self,text):
        self.popup_group.add(Popup(text))

class Popup(pygame.sprite.Sprite):
    def __init__(self,text):
        super().__init__()
        self.box_image = pygame.image.load('Assets/board.png').convert()
        self.box_rect = self.box_image.get_rect()

        self.font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(util.window_size[1]/20))
        self.text = self.font.render(text,True,(0,0,0))
        self.text_rect = self.text.get_rect()
        
        self.box_rect.center = [util.window_size[0]/2,util.window_size[1]/2]
        self.text_rect.center = self.box_rect.center

        #allegedly the average person can read a character every ~70ms, this number feels right from testing
        TIME_PER_CHARACTER = .07
        self.timer = len(text)*TIME_PER_CHARACTER

    def update(self):
        self.timer -= util.clock_time/1000

        util.screen.blit(self.box_image,self.box_rect)
        util.screen.blit(self.text,self.text_rect)

        if self.timer <= 0:
            self.kill()