import pygame, util

def init():
    #load default background
    global image
    image = pygame.image.load('Assets/backgrounds/background.png').convert()
    image = pygame.transform.scale(image,util.window_size)
    global blood_images
    blood_images = [pygame.image.load('Assets/backgrounds/back_blood0.png').convert(),
                    pygame.image.load('Assets/backgrounds/back_blood1.png').convert(),
                    pygame.image.load('Assets/backgrounds/back_blood2.png').convert(),
                    pygame.image.load('Assets/backgrounds/back_blood3.png').convert(),
                    pygame.image.load('Assets/backgrounds/back_blood4.png').convert()]
    global rect
    rect = image.get_rect()

def update():
    global image
    global rect
    #make background more red
    if util.player_ob.kills < 20_000:
        pass
    elif util.player_ob.kills > 100_000:
        image = blood_images[4]
        image = pygame.transform.scale(image,util.window_size)
    elif util.player_ob.kills > 80_000:
        image = blood_images[3]
        image = pygame.transform.scale(image,util.window_size)
    elif util.player_ob.kills > 60_000:
        image = blood_images[2]
        image = pygame.transform.scale(image,util.window_size)
    elif util.player_ob.kills > 40_000:
        image = blood_images[1]
        image = pygame.transform.scale(image,util.window_size)
    else:
        image = blood_images[0]
        image = pygame.transform.scale(image,util.window_size)

    rect = image.get_rect()
    