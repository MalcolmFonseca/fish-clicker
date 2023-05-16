import pygame, creature, math, util

class ShopButton():
    def __init__(self,name,cost,sps,creature_type,image_path,icon_image_path): #creature type is either walking, swimming or stationary
        self.button_rect = pygame.Rect((util.window_size[0]/3)*2+util.window_size[0]/128,util.window_size[0]/128,(util.window_size[0]/3)-util.window_size[0]/64,util.window_size[1]/9)
        self.name = name
        self.base_cost = cost
        self.cost = cost
        self.sps = sps
        self.owned = 0
        self.creature_type = creature_type
        self.unlocked = False

        #image attributes
        self.image_path = image_path

        self.icon_image_path = icon_image_path
        self.icon_image = pygame.image.load(icon_image_path).convert()
        self.icon_image_rect = self.icon_image.get_rect()

        #fonts
        self.big_font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(util.window_size[1]/16.6))
        self.small_font = pygame.font.Font('Assets/Kamalla.ttf',math.trunc(util.window_size[1]/27))

        #create text
        self.name_text = self.big_font.render(f'{self.name}',True,(0,0,0))
        self.name_text_rect = self.name_text.get_rect()

        self.cost_text = self.small_font.render(f'{util.num_to_word(self.cost)}',True,(0,0,0))
        self.cost_text_rect = self.cost_text.get_rect()

        self.owned_text = self.small_font.render(f'Owned: {self.owned}',True,(0,0,0))
        self.owned_text_rect = self.owned_text.get_rect()

        self.sps_text = self.small_font.render(f'Cps: {util.num_to_word(self.sps)}',True,(0,0,0))
        self.sps_text_rect = self.sps_text.get_rect()

        #add self to all_buttons in shop
        util.main_shop.all_buttons.append(self)

    def position(self, position_num):
        #position box
        self.button_rect.top = position_num*util.window_size[0]/105 + (position_num-1)*self.button_rect.height + util.window_size[1]/24 #last term for arrow size
        #position image
        self.icon_image_rect.left = self.button_rect.left + util.window_size[0]/170
        self.icon_image_rect.centery = self.button_rect.centery
        #position name text
        self.name_text_rect.left = self.icon_image_rect.right + util.window_size[0]/128
        self.name_text_rect.top = self.icon_image_rect.top
        #position cost text
        self.cost_text_rect.right = self.button_rect.right - util.window_size[0]/128
        self.cost_text_rect.top = self.button_rect.top
        #position owned text
        self.owned_text_rect.right = self.cost_text_rect.right
        self.owned_text_rect.centery = self.button_rect.centery + util.window_size[1]/27
        #position sps text
        self.sps_text_rect.left = self.name_text_rect.left
        self.sps_text_rect.bottom = self.owned_text_rect.bottom
    
    def check_expensive(self,player_score):
        if player_score < self.cost:
            self.cost_text = self.small_font.render(f'{util.num_to_word(self.cost)}',True,(255,0,0))
        else:
            self.cost_text = self.small_font.render(f'{util.num_to_word(self.cost)}',True,(0,0,0))

    def check_unlock(self,player_total_score):
        if player_total_score >= self.cost and self.unlocked == False:
            self.unlocked = True
            return True
        else:
            return False

    def buy(self):
        #update cost and owned #
        self.owned += 1
        self.cost = math.ceil(self.base_cost * math.pow(1.15,self.owned))

        #update text
        self.cost_text = self.small_font.render(f'{util.num_to_word(self.cost)}',True,(0,0,0))
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
    
    #for use loading data
    def add(self):
        #update cost
        self.cost = math.ceil(self.base_cost * math.pow(1.15,self.owned))

        #update text
        self.cost_text = self.small_font.render(f'{util.num_to_word(self.cost)}',True,(0,0,0))
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