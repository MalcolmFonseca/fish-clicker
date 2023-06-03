import pygame, random, util

class Gore():
    def __init__(self):
        self.gore_list = []
    
    def splatter(self,pos,size=10):
        gore_group = pygame.sprite.Group()

        for n in range(0,50):
            gore_group.add(Blood(pos,size))

        self.gore_list.append(gore_group)
        
class Blood(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.pos = pos
        self.size = size
        self.speed = [10*(random.randint(0,20)/10-1),10*(random.randint(0,20)/10-1)]
        self.timer = random.random()

    def update(self):
        self.speed[1] += .75
        self.pos = [self.pos[0]+self.speed[0],self.pos[1]+self.speed[1]]
        self.timer -= util.clock_time/1000
        pygame.draw.circle(util.screen,'#D40404',self.pos,self.timer*self.size)
        if self.timer <= 0:
            self.kill()