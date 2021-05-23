import pygame
from pygame.sprite import Sprite, Group
from abc           import ABC, abstractmethod
from constants     import *
from projectiles   import Spear, Projectiles, Bomb, Shuriken
from vector        import Vector
from creeps        import Creeps

class Tower(Sprite, ABC):
    image_path:   str
    attack_range: int
    projectile:   Projectiles
    reload_time:  int
    image:        pygame.sprite.Sprite # non
    rect:         pygame.Rect

    group = Group()

    def __init__(self, properties_dict):
        super().__init__()
        for key, value in properties_dict.items():
            self.__setattr__(key, value)
        self.reloading_time = 0
        
        self.image = pygame.image.load(self.image_path).convert()
        self.image = pygame.transform.scale(self.image, (TOWER_WIDTH, TOWER_HEIGHT))
        Tower.group.add(self)

    def attack(self):
        for creep in Creeps.group:
            vector = Vector(creep.rect.x - self.rect.x, creep.rect.y - self.rect.y)
            if vector.norm() <= self.attack_range and self.reloading_time <= 0:
                self.projectile(self.rect, (1/10) * vector)
                self.reloading_time = self.reload_time
                return


class RedTower(Tower):
    def __init__(self, rectangle):
        super().__init__(TOWERS['red'])
        self.projectile = Spear
        self.rect       = self.image.get_rect()
        self.rect       = rectangle

class OrangeTower(Tower):
    def __init__(self, rectangle):
        super().__init__(TOWERS['orange'])
        self.projectile = Bomb
        self.rect       = self.image.get_rect()
        self.rect       = rectangle

class BlueTower(Tower):
    def __init__(self, rectangle):
        super().__init__(TOWERS['blue'])
        self.projectile = Shuriken
        self.rect       = self.image.get_rect()
        self.rect       = rectangle

class TowerFactory:
    def __init__(self):
        pass
    @staticmethod
    def create_tower(keyword, rectangle):
        if keyword == 'red':
            return RedTower(rectangle)
        if keyword == 'blue':
            return BlueTower(rectangle)
        if keyword == 'orange':
            return OrangeTower(rectangle)


