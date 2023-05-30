import pygame,util,random

class BloodLightning():
    def __init__(self):
        self.image = pygame.image.load('Assets/bloodlightning.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0,util.window_size[0])
        self.timer = 1.5

    def render(self):
        if self.timer <= 0:
            self.timer = 1.5
            self.rect.centerx = random.randrange(0,util.window_size[0])
        elif self.timer <= .5:
            util.screen.blit(self.image,self.rect)
            self.timer -= util.clock_time/1000
            self.shock()
        else:
            self.timer -= util.clock_time/1000

    def shock(self):
        for creature in util.player_ob.bought:
            if creature.rect.colliderect(self):
                creature.die()