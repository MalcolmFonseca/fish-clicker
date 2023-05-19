import pygame, util

def init():
    #load default background
    global image
    image = pygame.image.load('Assets/background.png').convert()
    image = pygame.transform.scale(image,util.window_size)
    global rect
    rect = image.get_rect()
    update()

def update():
    pass
    #make background more red