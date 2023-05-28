import pygame, random, util

class Gore():
    def __init__(self):
        self.gore_list = []
    
    def splatter(self,pos,size=5):
        gore_group = pygame.sprite.Group()

        for n in range(0,100):
            gore_group.add(Blood(pos,size))

        self.gore_list.append(gore_group)
        
class Blood(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.rect = pygame.Rect(0,0,size,size)
        self.rect.center = pos
        self.speed = [10*(random.randint(0,20)/10-1),10*(random.randint(0,20)/10-1)]
        self.timer = random.random()

    def update(self):
        self.speed[1] += .75
        self.rect.center = [self.rect.centerx+self.speed[0],self.rect.centery+self.speed[1]]
        self.timer -= util.clock_time/1000
        if self.timer < 1/4:
            self.rect = self.rect.inflate(-1,-1)
        pygame.draw.rect(util.screen,'#D40404',self.rect)
        if self.timer <= 0:
            self.kill()