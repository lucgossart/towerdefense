from pygame.sprite import Sprite, Group
from abc import ABC, abstractmethod
from constants import *

class Projectiles(Sprite, ABC):

    group = Group()

    def __init__(self, position: pygame.Rect, speed_vector, image):

        super().__init__()
        self.image        = image
        self.rect         = self.image.get_rect()
        self.rect.x       = position.x
        self.rect.y       = position.y
        self.speed_vector = speed_vector

        Projectiles.group.add(self)

    def move(self):
        self.rect.x +=  self.speed_vector.x
        self.rect.y +=  self.speed_vector.y

    @abstractmethod
    def do_damage(self, touched_creep, creeps_group):
        pass

class Spear(Projectiles):

    def __init__(self, position, speed_vector):
        super().__init__(position, speed_vector, SPEAR_IMAGE)
        
    def do_damage(self, touched_creep, creeps_group):
        touched_creep.lose_hp(RED_TOWER_DAMAGE)

