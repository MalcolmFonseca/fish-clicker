import pygame,util,bloodtemple

class SceneButton():
    def __init__(self):
        self.state = 'Ocean'
        self.ocean_image = pygame.image.load('Assets/oceanBox.png').convert()
        self.temple_image = pygame.image.load('Assets/templeBox.png').convert()
        self.image = self.temple_image
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [util.window_size[0]/128,util.window_size[1] - util.window_size[0]/128]
    
    def press(self):
        if self.state == 'Ocean':
            self.state = 'Temple'
            self.image = self.ocean_image
            bloodtemple.enter()
        else:
            self.state = 'Ocean'
            self.image = self.temple_image