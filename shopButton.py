import pygame

class ShopButton():
    def __init__(self,name,cost,image_path):
        self.button_rect = pygame.Rect((1920/3)*2+15,15,(1920/3)-30,120)
        self.name = name
        self.cost = cost
        self.image = pygame.image.load(image_path)
        self.image_rect = self.image.get_rect()

    def position(self, position_num):
        #15 is size of gap 120 is height of button
        top = position_num*15 + (position_num-1)*120 + 45
        self.button_rect.top = top
        self.image_rect.left = (1920/3)*2+15
        self.image_rect.top = top