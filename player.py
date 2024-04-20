import pygame, util, math

class Player():
    def __init__(self):
        self.score = 15
        self.total_score = 15
        self.sps = .1
        self.bought = pygame.sprite.Group()
        self.kills = 0
        self.blood = 0
        self.ascensions = 0
        #score text
        self.score_font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(util.window_size[1]/13.5))
        self.score_text = self.score_font.render(f'Chum: {util.num_to_word(math.trunc(self.score))}',True,(0,0,0))
        self.score_text_rect = self.score_text.get_rect()
        self.score_text_rect.centerx = util.window_size[0]/3
        #create text for sps
        self.sps_font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(util.window_size[1]/20))
        self.sps_text = self.sps_font.render(f'Cps: {util.num_to_word(self.sps)}',True,(0,0,0))
        self.sps_text_rect = self.sps_text.get_rect()
        self.sps_text_rect.centerx = self.score_text_rect.centerx
        self.sps_text_rect.top = self.score_text_rect.bottom

    def add_score(self,change):
        self.score += change
        if change > 0:
            self.total_score += change
        self.score_text = self.score_font.render(f'Chum: {util.num_to_word(math.trunc(self.score))}',True,(0,0,0))
        self.score_text_rect = self.score_text.get_rect()
        #position score text
        if util.main_shop.minimize:
            self.score_text_rect.centerx = util.window_size[0]/2
        else:
            self.score_text_rect.centerx = util.window_size[0]/3
    
    def add_sps(self,change):
        self.sps += change
        self.update_sps_text()

    def update_sps_text(self):
        self.sps_text = self.sps_font.render(f'Cps: {util.num_to_word(self.sps)}',True,(0,0,0))
        self.sps_text_rect = self.sps_text.get_rect()
        self.sps_text_rect.centerx = self.score_text_rect.centerx
        self.sps_text_rect.top = self.score_text_rect.bottom

    def ascend(self):
        self.ascensions += 1
        #clear all purchases
        for button in util.main_shop.all_buttons:
            button.reset()
        for sigil in util.sigil_menu.all_sigils:
            sigil.reset()

        self.bought = pygame.sprite.Group()
        #clear score
        self.score = 15
        self.sps = .1
        self.update_sps_text()
        self.blood = 0