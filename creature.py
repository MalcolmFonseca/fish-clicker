import pygame,random,util

class Creature(pygame.sprite.Sprite):
    def __init__(self,image_path):
        super().__init__()
        self.base_image = pygame.image.load(image_path).convert_alpha()
        self.base_image_flipped = pygame.transform.flip(self.base_image,True,False)
        self.image = self.base_image
        self.rect = self.image.get_rect()
        self.rect.bottom = util.window_size[1]
        self.rect.centerx = random.randrange(0,util.window_size[0])
        self.speed = 0
        self.dead = False
        self.dead_timer = 0

    def update(self):
        #randomly change direction
        if random.randint(0,100) == 0:
            self.speed *= -1

        #maintain image direction
        if self.speed < 0:
            self.image = self.base_image_flipped
        else:
            self.image = self.base_image

        #animation for slicing
        if self.dead_timer == 0:
            self.dead = False
        else:
            self.dead_timer -= 1
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] and self.dead == False:
                self.die()

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

    def die(self):
        self.dead = True
        util.gore_ob.splatter(self.rect.center)
        self.dead_timer = 200

            

class StationaryCreature(Creature):
    def __init__(self, image_path):
        super().__init__(image_path)

    #override update method to prevent movement
    def update(self):
        #animation for slicing
        if self.dead_timer == 0:
            self.dead = False
        else:
            self.dead_timer -= 1  
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] and self.dead == False:
                self.die()

class SwimmingCreature(Creature):
    def __init__(self, image_path):
        super().__init__(image_path)
        self.rect.top = random.randrange(0,util.window_size[1]-self.rect.height)
        self.speed = 5

class WalkingCreature(Creature):
    def __init__(self, image_path):
        super().__init__(image_path)
        self.speed = 2