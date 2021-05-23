import pygame
from pygame.sprite import Sprite, Group
from constants import *

class Creeps(Sprite):

    group = Group()

    def __init__(self, hp, speed, image=PERE_NOEL):
        super().__init__()
        self.speed  = speed
        self.hp     = hp
        self.hp_max = hp
        self.image  = image
        self.rect   = self.image.get_rect()
        Creeps.group.add(self)

    def move(self):
        self.rect.y += self.speed

    def spawn(self, position):
        self.rect = position

    def lose_hp(self, hp):
        self.hp -= hp
        if self.hp <= 0:
            self.die()

    def die(self):
        self.kill()

    
