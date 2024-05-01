import menu, pygame, util

class MenuSystem():
    def __init__(self):
        self.enabled = False
        self.current_menu = menu.MainMenu()
        #create button for menu
        self.menu_button = pygame.image.load('Assets/menuButton.png').convert()
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
        util.screen.blit(self.current_menu.image,self.current_menu.rect)

        #render rects
        for rect in self.current_menu.rects:
            pygame.draw.rect(util.screen,'#FFE5AD',rect)

        #render buttons
        for button in self.current_menu.buttons:
            button.render()

        #render check boxes
        for box in self.current_menu.check_boxes:
            box.render()