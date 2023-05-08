import pygame,random

class Creature(pygame.sprite.Sprite):
    def __init__(self,image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.bottom = 1055
        self.timer = 0
        self.speed = 0

    def update(self):
        timer += 1
        #randomly change direction
        if random.randint(0,100) == 0:
            self.speed *= -1
        if timer == 120:
            self.rect.move(self.speed,0)
            

class StationaryCreature(Creature):
    def __init__(self, image_path):
        super().__init__(image_path)

    #override update method to prevent movement
    def update(self):
        pass

class SwimmingCreature():
    def __init__(self, image_path):
        super().__init__(image_path)
        self.rect.centery = random.randrange(0,1055)

class WalkingCreature():
    def __init__(self, image_path):
        super().__init__(image_path)