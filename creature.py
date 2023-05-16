import pygame,random,util

class Creature(pygame.sprite.Sprite):
    def __init__(self,image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = util.window_size[1]
        self.rect.centerx = random.randrange(0,util.window_size[0])
        self.speed = 0

    def update(self):
        #randomly change direction
        if random.randint(0,100) == 0:
            self.speed *= -1
            self.image = pygame.transform.flip(self.image,True,False)
        #keep creature in bounds
        if self.rect.left < 0:
            self.rect.left = 0
            self.speed *= -1
            self.image = pygame.transform.flip(self.image,True,False)
        elif self.rect.right > util.window_size[0]:
            self.rect.right = util.window_size[0]
            self.speed *= -1
            self.image = pygame.transform.flip(self.image,True,False)

        #move
        self.rect.centerx += self.speed
            

class StationaryCreature(Creature):
    def __init__(self, image_path):
        super().__init__(image_path)

    #override update method to prevent movement
    def update(self):
        pass

class SwimmingCreature(Creature):
    def __init__(self, image_path):
        super().__init__(image_path)
        self.rect.top = random.randrange(0,util.window_size[1]-self.rect.height)
        self.speed = 5

class WalkingCreature(Creature):
    def __init__(self, image_path):
        super().__init__(image_path)
        self.speed = 2