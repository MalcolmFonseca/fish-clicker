import pygame, settings, math, borderedRect

class Menu():
    def __init__(self):
        self.menu_rect = borderedRect.bordered_rect(settings.window_size[0]/3,settings.window_size[1]/80,settings.window_size[0]/3,settings.window_size[1]-settings.window_size[1]/80,settings.window_size[0]/128,pygame.color.Color('#D08C39'),(0,0,0))
        self.enabled = False

class MainMenu(Menu):
    def __init__(self):
        super().__init__()

        #make buttons for each submenu and exiting game
        self.font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(settings.window_size[1]/16.6))

        #exit button
        self.exit_button_rect = pygame.Rect((settings.window_size[0]/3)*2+settings.window_size[0]/128,settings.window_size[0]/128,(settings.window_size[0]/3)-settings.window_size[0]/64,settings.window_size[1]/9)
        self.exit_text = self.font.render(f'Exit Game',True,(0,0,0))
        self.exit_text_rect = self.exit_text.get_rect()

class SoundSettingsMenu(Menu):
    def __init__(self):
        super().__init__()

class VideoSettingsMenu(Menu):
    def __init__(self):
        super().__init__()