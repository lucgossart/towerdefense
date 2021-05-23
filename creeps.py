import pygame
from pygame.sprite import Sprite, Group
from constants import *

class Creeps(Sprite):

    group = Group()

    def __init__(self, hp, speed, image=PERE_NOEL):
        super().__init__()
        self.speed     = speed
        self.max_speed = speed
        self.hp        = hp
        self.hp_max    = hp
        self.image     = image
        self.rect      = self.image.get_rect()

        self.slow_counter = 0
        self.is_slowed = False

        Creeps.group.add(self)

    def move(self):
        self.rect.y += self.speed

    def spawn(self, position):
        self.rect = position

    def lose_hp(self, hp):
        self.hp -= hp
        if self.hp <= 0:
            self.die()
            
    def update_health_bar(self, surface):
        color = (255, 50, 50)
        bar   = pygame.Rect(self.rect.x + 10, self.rect.y, 80, 5)
        pygame.draw.rect(surface, color, bar)
        color = (50, 255, 50)
        bar   = pygame.Rect(self.rect.x + 10, self.rect.y, 80 / self.hp_max * self.hp, 5)
        pygame.draw.rect(surface, color, bar)

    def slow(self, duration, rate):
        self.speed *= rate
        self.slow_counter += duration

    def recover_max_speed(self):
        self.speed = self.max_speed

    def die(self):
        self.kill()

    
