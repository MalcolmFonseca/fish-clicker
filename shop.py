import pygame, util, math

class Shop():
    def __init__(self):
        self.image = pygame.image.load('Assets/shop.png').convert()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,[self.rect.width*util.scale[0],self.rect.height*util.scale[1]])
        self.rect = self.image.get_rect()
        self.rect.bottomright = [util.window_size[0],util.window_size[1]]
        self.all_buttons = []
        self.unlocked_buttons = []
        self.current_buttons = []
        self.current_position = 0
        self.minimize = False
        #create text for shop
        self.title_font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(util.window_size[1]/22))
        self.title_text = self.title_font.render('Shop',True,(0,0,0))
        self.title_text_rect = self.title_text.get_rect()
        self.title_text_rect.top = 5
        #create arrows for shop scrolling
        self.top_arrow = pygame.image.load('Assets/arrow.png').convert_alpha()
        self.top_arrow_rect = self.top_arrow.get_rect()

        self.bottom_arrow = pygame.transform.rotate(self.top_arrow,180)
        self.bottom_arrow_rect = self.bottom_arrow.get_rect()

    def render(self):
        #render shop box
        util.screen.blit(self.image,self.rect)
        #render shop title
        util.screen.blit(self.title_text,self.title_text_rect)
        #render item buttons
        for button in util.main_shop.current_buttons:
            util.screen.blit(button.button_image,button.button_rect)
            #check if cost should be red
            button.check_expensive()

            util.screen.blit(button.icon_image,button.icon_image_rect)
            util.screen.blit(button.name_text,button.name_text_rect)
            util.screen.blit(button.cost_text,button.cost_text_rect)
            util.screen.blit(button.owned_text,button.owned_text_rect)
            util.screen.blit(button.sps_text,button.sps_text_rect)
        #render arrows
        if self.current_position != 0:
            util.screen.blit(self.top_arrow,self.top_arrow_rect)
        if util.main_shop.current_position + 7 < len(util.main_shop.unlocked_buttons):
            util.screen.blit(self.bottom_arrow,self.bottom_arrow_rect)
    
    def update_buttons(self):
        self.current_buttons.clear()
        for i in range(self.current_position,self.current_position + 7):
            try:
                self.current_buttons.append(self.unlocked_buttons[i])
            except: #will stop adding buttons when no more are available
                break

    def position_buttons(self):
        position = 1
        for button in self.current_buttons:
            button.position(position)
            position += 1
    
    def update_unlocks(self):
        for button in self.all_buttons:
            if button.check_unlock():
                self.unlocked_buttons.append(button)
                self.update_buttons()
                self.position_buttons()
    
    #make function for scrolling through shop
    def move_shop(self,direction):
        if direction == "UP":
            #check if fully scrolled up
            if self.current_position != 0 :
                self.current_position -= 7
        elif direction == "DOWN":
            #check if fully scrolled down
            if self.current_position + 7 < len(self.unlocked_buttons) :
                self.current_position += 7
        self.update_buttons()
        self.position_buttons()