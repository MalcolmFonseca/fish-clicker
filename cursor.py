import pygame, util

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #make sure it overrides the default cursor
        pygame.mouse.set_visible(False)
        #separate image for knife active
        self.image = pygame.image.load('Assets/cursor.png').convert_alpha()
        self.knife_image = pygame.image.load('Assets/knifecursor.png').convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        if util.knife_ob.enabled:
            util.screen.blit(self.knife_image,self.rect)
        else:
            util.screen.blit(self.image,self.rect)
