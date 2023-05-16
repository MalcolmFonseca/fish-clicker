import pygame, util, math, borderedRect

class Menu():
    def __init__(self):
        self.menu_rect = borderedRect.bordered_rect(0,0,util.window_size[0]/6,util.window_size[1]/4,util.window_size[0]/384,pygame.color.Color('#D08C39'),(0,0,0))
        self.enabled = False

class MainMenu(Menu):
    def __init__(self):
        super().__init__()

        #make buttons for each submenu and exiting game
        self.font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(util.window_size[1]/20))
        default_button = pygame.Rect(0,0,(util.window_size[0]/6)-util.window_size[0]/64,util.window_size[1]/16)
        default_button.centerx = self.menu_rect.border_rect.centerx

        #exit button
        self.exit_button_rect = pygame.Rect(default_button)
        self.exit_button_rect.bottom = self.menu_rect.border_rect.bottom - util.window_size[1]/28
        self.exit_text = self.font.render('Save and Exit',True,(0,0,0))
        self.exit_text_rect = self.exit_text.get_rect()
        self.exit_text_rect.center = self.exit_button_rect.center

        #options button
        self.options_button_rect = pygame.Rect(default_button)
        self.options_button_rect.bottom = self.exit_button_rect.top - util.window_size[1]/28
        self.options_text = self.font.render('Options',True,(0,0,0))
        self.options_text_rect = self.options_text.get_rect()
        self.options_text_rect.center = self.options_button_rect.center