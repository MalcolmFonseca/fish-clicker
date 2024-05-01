import pygame,math,util

class SigilInfoBox():
    def __init__(self):
        self.image = pygame.image.load('Assets/shopbutton.png').convert()
        self.rect = self.image.get_rect()

        self.font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(util.window_size[1]/27))

        self.name = ''
        self.description = ''
        self.description_2 = ''
        self.cost = ''

        self.name_text = self.font.render(f'{self.name}',True,(0,0,0))
        self.name_text_rect = self.name_text.get_rect()

        self.description_text = self.font.render(f'{self.description}',True,(0,0,0))
        self.description_text_rect = self.description_text.get_rect()
        self.description_text_2 = self.font.render(f'{self.description_2}',True,(0,0,0))
        self.description_text_2_rect = self.description_text.get_rect()

        self.cost_text = self.font.render(f'{self.cost}',True,(0,0,0))
        self.cost_text_rect = self.cost_text.get_rect()
        self.update_text()

    def render(self, name, description, cost):
        self.name = name
        self.description = description
        self.description_2 = ''
        self.cost = cost

        INFOBOX_MAX_CHAR = 50
        if len(self.description)>INFOBOX_MAX_CHAR:
            wrap_position = self.description.rfind(" ",0,INFOBOX_MAX_CHAR)
            self.description_2 = self.description[wrap_position+1:]
            self.description = self.description[:wrap_position]

        self.update_text()
        self.position()

        util.screen.blit(self.image,self.rect)
        util.screen.blit(self.name_text,self.name_text_rect)
        util.screen.blit(self.description_text,self.description_text_rect)
        util.screen.blit(self.description_text_2,self.description_text_2_rect)
        util.screen.blit(self.cost_text,self.cost_text_rect)

    def position(self):
        self.rect.topleft = pygame.mouse.get_pos()
        if self.rect.right > util.window_size[0]:
            self.rect.bottomright = pygame.mouse.get_pos()

        self.name_text_rect.left = self.rect.left + util.window_size[0]/128
        self.name_text_rect.top = self.rect.top + 5
        self.description_text_rect.left = self.rect.left + util.window_size[0]/128
        self.description_text_rect.top = self.name_text_rect.bottom + 5
        self.description_text_2_rect.left = self.rect.left + util.window_size[0]/128
        self.description_text_2_rect.top = self.description_text_rect.bottom
        self.cost_text_rect.right = self.rect.right - util.window_size[0]/128
        self.cost_text_rect.top = self.rect.top + 5

    def update_text(self):
        self.name_text = self.font.render(f'{self.name}',True,(0,0,0))
        self.name_text_rect = self.name_text.get_rect()

        self.description_text = self.font.render(f'{self.description}',True,(0,0,0))
        self.description_text_rect = self.description_text.get_rect()

        self.description_text_2 = self.font.render(f'{self.description_2}',True,(0,0,0))
        self.description_text_2_rect = self.description_text.get_rect()

        self.cost_text = self.font.render(f'{self.cost}',True,(0,0,0))
        self.cost_text_rect = self.cost_text.get_rect()