import pygame, util, random

class DarkFamiliar():
    def __init__(self):
        self.image = pygame.image.load('Assets/sigilpowers/darkFamiliar.png').convert_alpha()
        self.image_right = self.image
        self.image_left = pygame.transform.flip(self.image,True,False)
        self.rect = self.image.get_rect()
        self.rect.center = [util.window_size[0]/2,util.window_size[1]/2]
        self.speed = 2.5
        self.dragging = False

    def render(self):
        #randomly change direction
        if random.randint(0,100) == 0:
            self.speed *= -1

        #check if grabbed
        if self.dragging :
            mouse_pos = pygame.mouse.get_pos()
            self.rect.center = mouse_pos
        else:
            #maintain image direction
            if self.speed < 0:
                self.image = self.image_left
            else:
                self.image = self.image_right

            #keep creature in bounds
            if self.rect.left < 0:
                self.rect.left = 0
                self.speed *= -1
            elif self.rect.right > util.window_size[0]:
                self.rect.right = util.window_size[0]
                self.speed *= -1

            #move
            self.rect.centerx += self.speed

        #check fish in range to eat
        for creature in util.player_ob.bought:
            if creature.rect.colliderect(self) and self.dragging == False:
                creature.die()

        util.screen.blit(self.image,self.rect)