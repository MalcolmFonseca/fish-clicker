import pygame,random

class Creature(pygame.sprite.Sprite):
    def __init__(self,image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.bottom = 1055
        self.rect.centerx = random.randrange(100,1820)
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
        elif self.rect.right > 1920:
            self.rect.right = 1920
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
        self.rect.centery = random.randrange(0,950)
        self.speed = 5

class WalkingCreature(Creature):
    def __init__(self, image_path):
        super().__init__(image_path)
        self.speed = 2