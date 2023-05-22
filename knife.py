import pygame,util

class Knife():
    def __init__(self):
        self.off_image = pygame.image.load('Assets/knifeBox.png').convert()
        self.on_image = pygame.image.load('Assets/knifeBoxOn.png').convert()
        self.rect = self.off_image.get_rect()
        self.rect.bottomleft = [util.window_size[0]/128,util.window_size[1] - 2*util.window_size[0]/128 - self.rect.height]
        self.enabled = False

    def get_image(self):
        if self.enabled:
            return self.on_image
        else:
            return self.off_image