import pygame

from pygame.sprite import Sprite, Group
from abc           import ABC, abstractmethod

from game.vector  import Vector
from .building    import Building
# from .remparts    import Rempart


class Tower(Building):
    image_path:   str
    attack_range: int
    projectile:   object
    reload_time:  int
    image:        pygame.sprite.Sprite # non
    rect:         pygame.Rect
    level:        int

    group = Group()

    def __init__(self, *args):
        super().__init__(*args)
        self.reloading_time = 0
        Tower.group.add(self)

    def set_projectile(self, projectile):
        self.projectile = projectile

    # def upgrade(self, player):
    #     super().upgrade(player)
        # self.upgrade_projectile()
    
    # @abstractmethod
    # def upgrade_projectile(self):
    #     pass

    def attack(self):
        for creep in Creeps.group:
            vector = Vector(creep.rect.x - self.rect.x, creep.rect.y - self.rect.y)
            if vector.norm() <= self.attack_range and self.reloading_time <= 0:
                self.projectile(self.rect, (1/10) * vector)
                self.reloading_time = self.reload_time
                return
