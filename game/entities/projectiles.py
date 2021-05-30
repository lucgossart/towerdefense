from pygame.sprite import Sprite, Group
from tower_config  import TOWERS
from waves_config  import WAVES
from abc import ABC, abstractmethod
from vector import Vector
from constants import *

class Projectiles(Sprite, ABC):

    group = Group()

    def __init__(self, position: pygame.Rect, speed_vector, image, level):

        super().__init__()
        self.image        = image
        self.rect         = self.image.get_rect()
        self.rect.x       = position.x
        self.rect.y       = position.y
        self.speed_vector = speed_vector
        self.level        = level

        Projectiles.group.add(self)

    def move(self):
        self.rect.x +=  self.speed_vector.x
        self.rect.y +=  self.speed_vector.y

    @abstractmethod
    def do_damage(self, touched_creep, creeps_group):
        pass


class Spear(Projectiles):

    def __init__(self, position, speed_vector, level):
        super().__init__(position, speed_vector, SPEAR_IMAGE, level)
        
    def do_damage(self, touched_creep, creeps_group):
        touched_creep.lose_hp(TOWERS['red'][self.level]['damage'])


class Bomb(Projectiles):

    def __init__(self, position, speed_vector, level):
        super().__init__(position, speed_vector, BOMB_IMAGE, level)
        
    def do_damage(self, touched_creep, creeps_group):
        for creep in creeps_group:
            vector = Vector(self.rect.x - creep.rect.x, self.rect.y - creep.rect.y)
            if vector.norm() <= TOWERS['orange'][self.level]['splash radius']:
                creep.lose_hp(TOWERS['orange'][self.level]['damage'])


class Shuriken(Projectiles):

    def __init__(self, position, speed_vector, level):
        super().__init__(position, speed_vector, SHURIKEN_IMAGE, level)
        
    def do_damage(self, touched_creep, creeps_group):
        for creep in creeps_group:
            vector = Vector(self.rect.x - creep.rect.x, self.rect.y - creep.rect.y)
            if vector.norm() <= TOWERS['blue'][self.level]['splash radius']:
                creep.lose_hp(TOWERS['blue'][self.level]['damage'])
                duration = TOWERS['blue'][self.level]['slow_duration']
                rate     = TOWERS['blue'][self.level]['slow_rate']
                creep.slow(duration, rate)
