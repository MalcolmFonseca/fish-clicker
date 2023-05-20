import pygame, util, borderedRect, math

class Shop():
    def __init__(self):
        self.shop_rect = borderedRect.bordered_rect((util.window_size[0]/3)*2,0,util.window_size[0]/3,util.window_size[1],util.window_size[0]/384,pygame.color.Color('#D08C39'),(0,0,0))
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
        pygame.draw.rect(util.screen,self.shop_rect.border_color,util.main_shop.shop_rect.border_rect)
        pygame.draw.rect(util.screen,util.main_shop.shop_rect.inner_color,util.main_shop.shop_rect.inner_rect)
        #render shop title
        util.screen.blit(self.title_text,self.title_text_rect)
        #render item buttons
        for button in util.main_shop.current_buttons:
            pygame.draw.rect(util.screen,'#FFE5AD',button.button_rect)
            #check if cost should be red
            button.check_expensive()

            util.screen.blit(button.icon_image,button.icon_image_rect)
            util.screen.blit(button.name_text,button.name_text_rect)
            util.screen.blit(button.cost_text,button.cost_text_rect)
            util.screen.blit(button.owned_text,button.owned_text_rect)
            util.screen.blit(button.sps_text,button.sps_text_rect)
        #render arrows
        util.screen.blit(self.top_arrow,self.top_arrow_rect)
        util.screen.blit(self.bottom_arrow,self.bottom_arrow_rect)