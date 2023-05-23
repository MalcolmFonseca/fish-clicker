import menu, pygame, util

class MenuSystem():
    def __init__(self):
        self.enabled = False
        self.current_menu = menu.MainMenu()
        #create button for menu
        self.menu_button = pygame.image.load('Assets/menu.png').convert()
        self.menu_button_rect = self.menu_button.get_rect()
        self.menu_button_rect.top = util.window_size[1]/128
        self.menu_button_rect.left = util.window_size[1]/128

    def toggle(self):
        if self.enabled:
            self.enabled = False
            self.current_menu = menu.MainMenu()
        else:
            self.enabled = True

    def render(self):
        #draw menu box
        pygame.draw.rect(util.screen,self.current_menu.menu_rect.border_color,self.current_menu.menu_rect.border_rect)
        pygame.draw.rect(util.screen,self.current_menu.menu_rect.inner_color,self.current_menu.menu_rect.inner_rect)

        #render rects
        for rect in self.current_menu.rects:
            pygame.draw.rect(util.screen,util.sand_color,rect)

        #render buttons
        for button in self.current_menu.buttons:
            pygame.draw.rect(util.screen,util.sand_color,button.rect)
            util.screen.blit(button.text,button.text_rect)

        #render check boxes
        for box in self.current_menu.check_boxes:
            util.screen.blit(box.get_image(),box.get_rect())
            util.screen.blit(box.text,box.text_rect)

    def update_buttons(self):
        util.main_shop.current_buttons.clear()
        for i in range(util.main_shop.current_position,util.main_shop.current_position + 7):
            try:
                util.main_shop.current_buttons.append(util.main_shop.unlocked_buttons[i])
            except: #will stop adding buttons when no more are available
                break

    def position_buttons(self):
        position = 1
        for button in util.main_shop.current_buttons:
            button.position(position)
            position += 1
    
    def update_unlocks(self):
        for button in util.main_shop.all_buttons:
            if button.check_unlock():
                util.main_shop.unlocked_buttons.append(button)
                self.update_buttons()
                self.position_buttons()
