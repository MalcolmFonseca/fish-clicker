import pygame,util

class HellFire():
    def __init__(self):
        self.position = [0,util.window_size[1]]
        self.time = 10
        self.flame_group = pygame.sprite.Group()
        self.direction = 1

    def render(self):
        self.time -= 1
        if self.time <= 0:
            self.time = 10
            if self.position[0] >= util.window_size[0] or self.position[0] < 0:
                self.direction *= -1
            self.position[0] += 60*self.direction
            self.flame_group.add(Flame(self.position))

        self.flame_group.update()

class Flame(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('Assets/sigilpowers/hellfire.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.timer = 60

    def update(self):
        self.timer -= 1

        if self.timer <= 0:
            self.kill()
        elif self.timer <= 10:
            self.rect.bottom = util.window_size[1] + 25
        elif self.timer <= 20:
            self.rect.bottom = util.window_size[1] + 20
        elif self.timer <= 30:
            self.rect.bottom = util.window_size[1] + 15
        elif self.timer <= 40:
            self.rect.bottom = util.window_size[1] + 10
        elif self.timer <= 50:
            self.rect.bottom = util.window_size[1] + 5
        else:
            self.rect.bottom = util.window_size[1]

        util.screen.blit(self.image,self.rect)

        #check fish in range to burn
        for creature in util.player_ob.bought:
            if creature.rect.colliderect(self):
                creature.die()