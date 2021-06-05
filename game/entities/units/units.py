import pygame
from pygame.sprite import Sprite, Group

from ..generic_entity import Entity

class Unit(Entity):
    path:   object          # Champ de vecteurs
    image:  pygame.image

    group = Group()

    def __init__(self, *args):
        super().__init__(*args)
        self.max_speed = self.speed
        self.hp_max    = self.hp

        self.slow_counter = 0

        Unit.group.add(self)

    def move(self):
        self.rect.x += self.speed * self.path(self.rect.x, self.rect.y).x
        self.rect.y += self.speed * self.path(self.rect.x, self.rect.y).y

    def spawn(self, position):
        self.rect = position

    def slow(self, duration, rate):
        self.speed *= rate
        self.slow_counter += duration

    def recover_max_speed(self):
        self.speed = self.max_speed

    def die(self):
        self.kill()

    def attack(self, entity):
        entity.lose_hp(self.damage)

    def try_to_attack(self):
        pass

class Creep(Unit):
    group = Group()

    def __init__(self, *args):
        super().__init__(*args)

class Soldier(Unit):
    group = Group()

    def __init__(self, *args):
        super().__init__(*args)
