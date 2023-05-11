import pygame, creature, math, settings

class ShopButton():
    def __init__(self,name,cost,sps,image_path,creature_type): #creature type is either walking, swimming or stationary
        self.button_rect = pygame.Rect((settings.window_size[0]/3)*2+settings.window_size[0]/128,settings.window_size[0]/128,(settings.window_size[0]/3)-settings.window_size[0]/64,settings.window_size[1]/9)
        self.name = name
        self.cost = cost
        self.sps = sps
        self.owned = 0
        self.creature_type = creature_type

        #image attributes
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.image_rect = self.image.get_rect()

        #fonts
        self.big_font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(settings.window_size[1]/16.6))
        self.small_font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(settings.window_size[1]/27))

        #create text
        self.name_text = self.big_font.render(f'{self.name}',True,(0,0,0))
        self.name_text_rect = self.name_text.get_rect()

        self.cost_text = self.small_font.render(f'{self.cost}',True,(0,0,0))
        self.cost_text_rect = self.cost_text.get_rect()

        self.owned_text = self.small_font.render(f'Owned: {self.owned}',True,(0,0,0))
        self.owned_text_rect = self.owned_text.get_rect()

        self.sps_text = self.small_font.render(f'CPS: {self.sps}',True,(0,0,0))
        self.sps_text_rect = self.sps_text.get_rect()

    def position(self, position_num):
        #position box
        self.button_rect.top = position_num*settings.window_size[0]/128 + (position_num-1)*settings.window_size[1]/9 + settings.window_size[1]/24 #last term for arrow size
        #position image
        self.image_rect.left = self.button_rect.left
        self.image_rect.centery = self.button_rect.centery
        #position name text
        self.name_text_rect.left = self.image_rect.right + settings.window_size[0]/128
        self.name_text_rect.centery = self.button_rect.centery
        #position cost text
        self.cost_text_rect.right = self.button_rect.right - settings.window_size[0]/128
        self.cost_text_rect.top = self.button_rect.top
        #position owned text
        self.owned_text_rect.right = self.cost_text_rect.right
        self.owned_text_rect.centery = self.button_rect.centery + settings.window_size[1]/27
        #position sps text
        self.sps_text_rect.left = self.name_text_rect.left
        self.sps_text_rect.bottom = self.owned_text_rect.bottom
    
    def check_expensive(self,player_score):
        if player_score < self.cost:
            self.cost_text = self.small_font.render(f'{self.cost}',True,(255,0,0))
        else:
            self.cost_text = self.small_font.render(f'{self.cost}',True,(0,0,0))

    def buy(self):
        #update cost and owned #
        self.owned += 1
        self.cost += math.ceil(self.cost*.15)

        #update text
        self.cost_text = self.small_font.render(f'{self.cost}',True,(0,0,0))
        self.cost_text_rect = self.cost_text.get_rect()

        self.owned_text = self.small_font.render(f'Owned: {self.owned}',True,(0,0,0))
        self.owned_text_rect = self.owned_text.get_rect()
        
        #create correct creature
        if self.creature_type == 'swimming':
            return creature.SwimmingCreature(self.image_path)
        elif self.creature_type == 'walking':
            return creature.WalkingCreature(self.image_path)
        else:
            return creature.StationaryCreature(self.image_path)