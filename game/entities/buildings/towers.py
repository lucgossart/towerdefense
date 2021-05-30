import pygame
from tower_config  import TOWERS
from waves_config  import WAVES
from pygame.sprite import Sprite, Group
from abc           import ABC, abstractmethod
from constants     import *
from projectiles   import Spear, Projectiles, Bomb, Shuriken
from vector        import Vector
from creeps        import Creeps
from building      import Building, Rempart


class Tower(Building):
    image_path:   str
    attack_range: int
    projectile:   object
    reload_time:  int
    image:        pygame.sprite.Sprite # non
    rect:         pygame.Rect
    level:        int

    group = Group()

    def __init__(self, properties_dict_list, type_, rectangle):
        super().__init__(properties_dict_list, type_, rectangle)
        self.reloading_time = 0
        self.image = pygame.transform.scale(self.image, (TOWER_WIDTH, TOWER_HEIGHT))
        Tower.group.add(self)

    def upgrade(self):
        super().upgrade()
        self.upgrade_projectile()
    
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

    group = Group()
    def __init__(self, rectangle):
        super().__init__(TOWERS['red'], 'red', rectangle)
        self.projectile = lambda *args: Spear(*args, level=0)
        RedTower.group.add(self)

    def upgrade_projectile(self):
        self.projectile = lambda *args: Spear(*args, level=self.level)
    

class OrangeTower(Tower):

    group = Group()
    def __init__(self, rectangle):
        super().__init__(TOWERS['orange'], 'orange', rectangle)
        self.projectile = lambda *args: Bomb(*args, level=0)
        OrangeTower.group.add(self)

    def upgrade_projectile(self):
        self.projectile = lambda *args: Bomb(*args, level=self.level)


class BlueTower(Tower):

    group = Group()
    def __init__(self, rectangle):
        super().__init__(TOWERS['blue'], 'blue', rectangle)
        self.projectile = lambda *args: Shuriken(*args, level=0)
        BlueTower.group.add(self)

    def upgrade_projectile(self):
        self.projectile = lambda *args: Shuriken(*args, level=self.level)

class YellowTower(Tower):

    group = Group()
    def __init__(self, rectangle, player):
        super().__init__(TOWERS['yellow'], 'yellow', rectangle)
        YellowTower.group.add(self)
        self.player = player

    def upgrade_projectile(self):
        pass

    def attack(self):
        self.player.get_income(self.income)


class TowerTypeFactory:
    def __init__(self):
        pass
    @staticmethod
    def return_type(keyword):
        if keyword == 'red':
            return RedTower
        if keyword == 'blue':
            return BlueTower
        if keyword == 'orange':
            return OrangeTower
        if keyword == 'yellow':
            return YellowTower
        if keyword == 'rempart':
            return Rempart



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
        if keyword == 'rempart':
            return Rempart(rectangle)


