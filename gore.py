import pygame, util, random

class Gore():
    def __init__(self):
        self.gore_list = []
    
    def splatter(self,pos):
        gore_group = pygame.sprite.Group()

        for n in range(0,100):
            gore_group.add(Blood(pos))

        self.gore_list.append(gore_group)
        
class Blood(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.rect = pygame.Rect(0,0,4,4)
        self.rect.center = pos
        self.speed = [10*(random.randint(0,20)/10-1),10*(random.randint(0,20)/10-1)]
        self.timer = 20

    def update(self):
        self.speed[1] += .5
        self.rect.center = [self.rect.centerx+self.speed[0],self.rect.centery+self.speed[1]]
        self.timer -= 1
        if self.timer < 7:
            self.rect = self.rect.inflate(-1,-1)
        if self.timer == 0:
            self.kill()