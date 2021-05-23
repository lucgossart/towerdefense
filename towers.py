import pygame
from tower_config  import TOWERS
from waves_config  import WAVES
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

    def __init__(self, properties_dict_list, type_):
        super().__init__()
        self.level = 0
        self.properties_dict_list = properties_dict_list
        for key, value in properties_dict_list[0].items():
            self.__setattr__(key, value)

        self.reloading_time = 0
        self.type           = type_
        
        self.image = pygame.image.load(self.image_path).convert()
        self.image = pygame.transform.scale(self.image, (TOWER_WIDTH, TOWER_HEIGHT))
        Tower.group.add(self)

    def upgrade(self):
        self.level += 1
        try:
            for key, value in self.properties_dict_list[self.level].items():
                self.__setattr__(key, value)
        except Exception as e:
            print(e)
        self.upgrade_projectile()
        self.image = pygame.image.load(self.image_path).convert()
        self.image = pygame.transform.scale(self.image, (TOWER_WIDTH, TOWER_HEIGHT))
    
    @abstractmethod
    def upgrade_projectile(self):
        pass

    def attack(self):
        for creep in Creeps.group:
            vector = Vector(creep.rect.x - self.rect.x, creep.rect.y - self.rect.y)
            if vector.norm() <= self.attack_range and self.reloading_time <= 0:
                self.projectile(self.rect, (1/10) * vector)
                self.reloading_time = self.reload_time
                return


class RedTower(Tower):

    def __init__(self, rectangle):
        super().__init__(TOWERS['red'], 'red')
        self.projectile = lambda *args: Spear(*args, level=0)
        self.rect       = self.image.get_rect()
        self.rect       = rectangle

    def upgrade_projectile(self):
        self.projectile = lambda *args: Spear(*args, level=self.level)
    

class OrangeTower(Tower):

    def __init__(self, rectangle):
        super().__init__(TOWERS['orange'], 'orange')
        self.projectile = lambda *args: Bomb(*args, level=0)
        self.rect       = self.image.get_rect()
        self.rect       = rectangle

    def upgrade_projectile(self):
        self.projectile = lambda *args: Bomb(*args, level=self.level)

class BlueTower(Tower):

    def __init__(self, rectangle):
        super().__init__(TOWERS['blue'], 'blue')
        self.projectile = lambda *args: Shuriken(*args, level=0)
        self.rect       = self.image.get_rect()
        self.rect       = rectangle

    def upgrade_projectile(self):
        self.projectile = lambda *args: Shuriken(*args, level=self.level)


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


