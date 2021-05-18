import pygame

from pygame.sprite import Sprite
from abc import ABC
from constants import *

class Tower(Sprite, ABC):
    cost: int
    
    def __init__(self):
        super().__init__()


class RedTower(Tower):

    def __init__(self, rectangle):
        super().__init__()
        self.image  = pygame.image.load('images/tour_pourpre.png').convert()
        self.image  = pygame.transform.scale(self.image, (TOWER_WIDTH, TOWER_HEIGHT))
        self.rect   = self.image.get_rect()
        self.rect   = rectangle
        self.cost   = RED_TOWER_COST


