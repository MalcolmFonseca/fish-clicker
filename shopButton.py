import pygame

class ShopButton():   
    def __init__(self,name,cost,image_path):
        self.button_rect = pygame.Rect((1920/3)*2+15,15,(1920/3)-30,120)
        self.name = name
        self.cost = cost
        self.image = pygame.image.load(image_path)
        self.image_rect = self.image.get_rect()

        #create text
        kamalla_font = pygame.font.Font('Assets/Kamalla.ttf',70)
        self.name_text = kamalla_font.render(f'{self.name}',True,(0,0,0))
        self.name_text_rect = self.name_text.get_rect()

        self.cost_text = kamalla_font.render(f'{self.cost}',True,(0,0,0))
        self.cost_text_rect = self.cost_text.get_rect()

    def position(self, position_num):
        #15 is size of gap 120 is height of button

        #position box
        top = position_num*15 + (position_num-1)*120 + 45
        self.button_rect.top = top
        #position image
        self.image_rect.left = (1920/3)*2+15
        self.image_rect.top = top + 10
        #position name text
        self.name_text_rect.left = self.image_rect.right + 15
        self.name_text_rect.centery = self.button_rect.centery
        #position cost text
        self.cost_text_rect.right = self.button_rect.right - 15
        self.cost_text_rect.centery = self.button_rect.centery