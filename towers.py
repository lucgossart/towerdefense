import pygame

from pygame.sprite import Sprite, Group
from abc           import ABC, abstractmethod
from constants     import *
from projectiles   import Spear
from vector        import Vector
from creeps        import Creeps

class Tower(Sprite, ABC):
    image: pygame.sprite.Sprite
    rect:  pygame.Rect

    group = Group()

    def __init__(self, attack_range, attack_rate, projectile):
        super().__init__()
        self.attack_range   = attack_range
        self.attack_rate    = attack_rate
        self.projectile     = projectile
        self.reloading_time = 0
        
        Tower.group.add(self)

    def attack(self):
        for creep in Creeps.group:
            vector = Vector(creep.rect.x - self.rect.x, creep.rect.y - self.rect.y)
            if vector.norm() <= self.attack_range and self.reloading_time <= 0:
                self.projectile(self.rect, (1/20) * vector)
                self.reloading_time = self.attack_rate
                return



class RedTower(Tower):

    def __init__(self, rectangle):
        super().__init__(600, 30, Spear)
        self.image  = pygame.image.load('images/tour_pourpre.png').convert()
        self.image  = pygame.transform.scale(self.image, (TOWER_WIDTH, TOWER_HEIGHT))
        self.rect   = self.image.get_rect()
        self.rect   = rectangle
        self.cost   = RED_TOWER_COST






