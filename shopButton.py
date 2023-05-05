import pygame

class ShopButton():
    def __init__(self,name,cost,image_path):
        self.button_rect = pygame.Rect(0,0,(1920/3)-50,200)
        self.name = name
        self.cost = cost
        self.image = pygame.image.load(image_path)