import pygame, util

class Sigil():
    def __init__(self,name,image_path,cost,loc):
        self.name = name
        self.base_image = pygame.image.load(image_path).convert_alpha()
        self.on_image = None
        self.rect = self.base_image.get_rect()
        self.rect.center = loc
        self.bought = False
        self.cost = cost

    def render(self):
        if self.bought:
            pass
        else:
            util.screen.blit(self.base_image,self.rect)

    def buy(self):
        if util.player_ob.score >= self.cost and self.bought == False:
            util.player_ob.add_score(-self.cost)
            self.bought = True