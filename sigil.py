import pygame,util

class Sigil():
    def __init__(self,name,image_path,cost,description,center):
        self.base_image = pygame.image.load(image_path).convert_alpha()
        self.on_image = pygame.image.load(image_path).convert_alpha()
        util.color_image(self.on_image,(0,0,0),(212,4,4))
        self.rect = self.base_image.get_rect()
        self.rect.center = center

        self.name = name
        self.bought = False
        self.cost = cost
        self.description = description

    def render(self):
        if self.bought:
            util.screen.blit(self.on_image,self.rect)
        else:
            util.screen.blit(self.base_image,self.rect)

    def buy(self):
        if util.player_ob.score >= self.cost and self.bought == False:
            #ascension is handled with other sigils, this is its clause
            if self.name == "Ascension":
                if util.player_ob.blood >= 50_000:
                    util.player_ob.ascend()
                else:
                    return

            util.player_ob.add_score(-self.cost)
            self.bought = True
            util.gore_ob.splatter(self.rect.center,size = 15)

    def reset(self):
        self.bought = False