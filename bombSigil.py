import pygame,util

class BombSigil():
    def __init__(self):
        self.image = pygame.image.load('Assets/bombBox.png').convert()
        self.rect = self.image.get_rect()
        self.rect.bottomleft = [util.window_size[0]/128,util.window_size[1] - 3*util.window_size[0]/128 - 2*self.rect.height]
        self.cooldown = 100
        self.current_time = 0

    def render(self):
        util.screen.blit()

    def press(self):
        if self.current_time == 0:
            for creature in util.player_ob.bought:
                creature.die()
        else:
            pass