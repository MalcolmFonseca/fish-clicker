import pygame,util,math

class BombSigil():
    def __init__(self):
        self.image = pygame.image.load('Assets/sigilpowers/bombBox.png').convert()
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [util.window_size[0]/128,util.window_size[1] - 3*util.window_size[0]/128 - 2*self.rect.height]
        self.cooldown = 60
        self.current_time = 0

        self.font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(util.window_size[1]/27))
        self.time_text = self.font.render(f'{int(self.current_time)}',True,(0,0,0))
        self.time_text_rect = self.time_text.get_rect()
        self.time_text_rect.center = self.rect.center

    def render(self):
        util.screen.blit(self.image,self.rect)
        if self.current_time > 0:
            self.time_text = self.font.render(f'{int(self.current_time)}',True,(0,0,0))
            self.time_text_rect = self.time_text.get_rect()
            self.time_text_rect.center = self.rect.center
            util.screen.blit(self.time_text,self.time_text_rect)
        self.current_time -= util.clock_time/1000

    def press(self):
        if self.current_time <= 0:
            self.current_time = self.cooldown
            for creature in util.player_ob.bought:
                if creature.dead == False:
                    creature.die()