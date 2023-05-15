import pygame

class Player():
    def __init__(self):
        self.score = 15
        self.total_score = 15
        self.sps = .1
        self.bought = pygame.sprite.Group()