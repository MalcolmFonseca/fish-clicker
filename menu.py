import pygame, util, borderedRect, menuButton, save, checkBox, bloodtemple

class Menu():
    def __init__(self):
        self.menu_rect = borderedRect.bordered_rect(0,0,util.window_size[0]/6,util.window_size[1]/4,util.window_size[0]/384,pygame.color.Color('#D08C39'),(0,0,0))
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
        self.buttons.append(menuButton.MenuButton('Save'))
        self.buttons.append(menuButton.MenuButton('Options',submenu=OptionsMenu())) 
        self.buttons.append(menuButton.MenuButton('Save and Exit')) 

        for i,button in enumerate(self.buttons):
            button.rect.centerx = self.menu_rect.border_rect.centerx
            button.rect.top = self.menu_rect.border_rect.top + (i+1)*(util.window_size[1]/56) + i*button.rect.height
            button.text_rect.center = button.rect.center

    def press(self,button):
        if button.name == 'Save and Exit':
            save.save_data()
            bloodtemple.running = False
            util.running = False
        elif button.name == 'Save':
            save.save_data()
        else:
            util.menu_system.current_menu = button.submenu
        
class OptionsMenu(Menu):
    def __init__(self):
        super().__init__()

        #add lighter box
        self.rects.append(pygame.Rect(self.menu_rect.inner_rect.left + 10,self.menu_rect.inner_rect.top +10,self.menu_rect.inner_rect.width-20,self.menu_rect.inner_rect.height-20))

        #add checkboxes
        self.check_boxes.append(checkBox.CheckBox('Shop In Front'))

        for i,box in enumerate(self.check_boxes):
            box.on_rect.right = self.rects[0].right - 10
            box.on_rect.top = self.menu_rect.border_rect.top + (i+1)*(util.window_size[1]/56) + i*box.get_rect().height + 20
            box.off_rect.right = self.rects[0].right - 10
            box.off_rect.top = self.menu_rect.border_rect.top + (i+1)*(util.window_size[1]/56) + i*box.get_rect().height + 20
            box.text_rect.right = box.get_rect().left - 10
            box.text_rect.centery = box.get_rect().centery