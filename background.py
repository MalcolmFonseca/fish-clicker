import pygame, util

class Background():
    def __init__(self):
        self.image = None
        self.blood_images = [pygame.image.load('Assets/backgrounds/background.png').convert(),
                        pygame.image.load('Assets/backgrounds/back_blood0.png').convert(),
                        pygame.image.load('Assets/backgrounds/back_blood1.png').convert(),
                        pygame.image.load('Assets/backgrounds/back_blood2.png').convert(),
                        pygame.image.load('Assets/backgrounds/back_blood3.png').convert(),
                        pygame.image.load('Assets/backgrounds/back_blood4.png').convert()]
        for image in self.blood_images:
            image = pygame.transform.scale(image,util.window_size)
        self.rect = image.get_rect()

    def render(self):
        #make background more red
        if util.player_ob.kills < 10_000:
            self.image = self.blood_images[0]
        elif util.player_ob.kills < 20_000:
            self.image = self.blood_images[1]
        elif util.player_ob.kills < 30_000:
            self.image = self.blood_images[2]
        elif util.player_ob.kills < 40_000:
            self.image = self.blood_images[3]
        elif util.player_ob.kills < 50_000:
            self.image = self.blood_images[4]
        else:
            self.image = self.blood_images[5]

        util.screen.blit(self.image,self.rect)