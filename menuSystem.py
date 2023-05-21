import menu, pygame, util

class MenuSystem():
    def __init__(self):
        self.enabled = False
        self.current_menu = menu.MainMenu()

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
