import pygame

class Sigil():
    def __init__(self,image_path):
        self.base_image = pygame.image.load(image_path).convert_alpha()
        self.on_image = None
        self.image = self.base_image
        self.bought = False