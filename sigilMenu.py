import pygame,util,sigil

class SigilMenu():
    def __init__(self):
        #book menu
        self.image = pygame.image.load('Assets/temple/sigilmenu.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image,[self.rect.width*util.scale[0],self.rect.height*util.scale[1]])
        self.rect = self.image.get_rect()

        self.enabled = False
        self.all_sigils = []
        self.populate_sigils()

        #close button
        self.close_button = pygame.image.load('Assets/temple/closesigilmenu.png').convert_alpha()
        self.close_button_rect = self.close_button.get_rect()
        self.close_button = pygame.transform.scale(self.close_button,[self.close_button_rect.width*util.scale[0],self.close_button_rect.height*util.scale[1]])
        self.close_button_rect = self.close_button.get_rect()
        self.close_button_rect.center = [util.window_size[0]-util.window_size[0]/8,util.window_size[0]/12]

    def populate_sigils(self):
        self.all_sigils.append(sigil.Sigil('Blood Lightning','Assets/sigils/bloodLightningSigil.png',0,[util.window_size[0]/6,util.window_size[1]/4.5]))
        self.all_sigils.append(sigil.Sigil('Mass Hemorrhage','Assets/sigils/massHemorrhageSigil.png',0,[500,500]))
        self.all_sigils.append(sigil.Sigil('Dark Familiar','Assets/sigils/massHemorrhageSigil.png',0,[1000,500]))
        self.all_sigils.append(sigil.Sigil('Ascension','Assets/sigils/ascensionSigil.png',0,[util.window_size[0]/2,util.window_size[1]/2]))

    def render(self):
        #render menu box
        util.screen.blit(self.image,self.rect)
        #render close button
        util.screen.blit(self.close_button,self.close_button_rect)

        for sigil in self.all_sigils:
            sigil.render()