import pygame, settings, math, borderedRect

class Menu():
    def __init__(self):
        self.menu_rect = borderedRect.bordered_rect(0,0,settings.window_size[0]/3,settings.window_size[1]/2,settings.window_size[0]/384,pygame.color.Color('#D08C39'),(0,0,0))
        self.enabled = False

class MainMenu(Menu):
    def __init__(self):
        super().__init__()

        #make buttons for each submenu and exiting game
        self.font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(settings.window_size[1]/16.6))

        #exit button
        self.exit_button_rect = pygame.Rect((settings.window_size[0]/3)*2+settings.window_size[0]/128,settings.window_size[0]/128,(settings.window_size[0]/3)-settings.window_size[0]/16,settings.window_size[1]/8)
        self.exit_button_rect.centerx = self.menu_rect.border_rect.centerx
        self.exit_button_rect.bottom = self.menu_rect.border_rect.bottom - settings.window_size[1]/28
        self.exit_text = self.font.render(f'Exit Game',True,(0,0,0))
        self.exit_text_rect = self.exit_text.get_rect()
        self.exit_text_rect.center = self.exit_button_rect.center

class SoundSettingsMenu(Menu):
    def __init__(self):
        super().__init__()

class VideoSettingsMenu(Menu):
    def __init__(self):
        super().__init__()