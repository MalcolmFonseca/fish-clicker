import pygame, util, menuButton, save, checkBox, bloodtemple

class Menu():
    def __init__(self):
        self.image = pygame.image.load('Assets/menu.png').convert()
        self.rect = self.image.get_rect()
        self.enabled = False
        self.buttons = []
        self.check_boxes = []
        self.rects = []
    
    def press(self,button):
        util.menu_system.current_menu = button.submenu
    
    #for checkboxes
    def check(self,box):
        box.on = not box.on
        util.settings[box.name] = not util.settings[box.name]

class MainMenu(Menu):
    def __init__(self):
        super().__init__()

        #make buttons for each submenu and exiting game
        self.buttons.append(menuButton.MenuButton('Options',submenu=OptionsMenu())) 
        self.buttons.append(menuButton.MenuButton('Save'))
        self.buttons.append(menuButton.MenuButton('Save + Exit')) 

        for i,button in enumerate(self.buttons):
            button.rect.centerx = self.rect.centerx
            button.rect.top = self.rect.top + (i+1)*(util.window_size[1]/56) + i*button.rect.height
            button.text_rect.center = button.rect.center

    def press(self,button):
        if button.name == 'Save + Exit':
            try:
                save.save_data()
                bloodtemple.running = False
                util.running = False
            except:
                return
        elif button.name == 'Save':
            save.save_data()
        else:
            #default button handling is to enter submenu
            util.menu_system.current_menu = button.submenu
        
class OptionsMenu(Menu):
    def __init__(self):
        super().__init__()

        #add checkboxes
        self.check_boxes.append(checkBox.CheckBox('Shop In Front'))

        for i,box in enumerate(self.check_boxes):
            box.rect.centerx = self.rect.centerx
            box.rect.top = self.rect.top + (i+1)*(util.window_size[1]/56) + i*box.get_rect().height + 20
            box.on_rect.right = box.rect.right - 10
            box.on_rect.centery = box.rect.centery
            box.off_rect.right = box.on_rect.right
            box.off_rect.top = box.on_rect.top
            box.text_rect.left = box.rect.left + 10
            box.text_rect.centery = box.rect.centery + 5