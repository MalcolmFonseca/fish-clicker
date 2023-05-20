import pygame, util, borderedRect, menuButton, save

class Menu():
    def __init__(self):
        self.menu_rect = borderedRect.bordered_rect(0,0,util.window_size[0]/6,util.window_size[1]/3.5,util.window_size[0]/384,pygame.color.Color('#D08C39'),(0,0,0))
        self.enabled = False
        self.buttons = []
        self.text = {}
    
    def press(self,button):
        util.menu_system.current_menu = button.submenu

class MainMenu(Menu):
    def __init__(self):
        super().__init__()

        #make buttons for each submenu and exiting game
        self.buttons.append(menuButton.MenuButton('Save and Exit')) 
        self.buttons.append(menuButton.MenuButton('Options',submenu=OptionsMenu())) 
        self.buttons.append(menuButton.MenuButton('Save'))

        for i,button in enumerate(self.buttons):
            button.rect.centerx = self.menu_rect.border_rect.centerx
            button.rect.bottom = self.menu_rect.border_rect.bottom - (i+1)*(util.window_size[1]/56) - i*button.rect.height
            button.text_rect.center = button.rect.center

    def press(self,button):
        if button.name == 'Save and Exit':
            save.save_data(util.player_ob,util.main_shop)
            util.running = False
        elif button.name == 'Save':
            save.save_data(util.player_ob,util.main_shop)
        else:
            util.menu_system.current_menu = button.submenu
        
class OptionsMenu(Menu):
    def __init__(self):
        super().__init__()