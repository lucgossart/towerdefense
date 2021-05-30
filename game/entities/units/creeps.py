import pygame
from pygame.sprite import Sprite, Group
from constants import *
from chemin    import Path

class Creeps(Sprite):
    path: Path

    group = Group()

    def __init__(self, param_dict, image=PERE_NOEL):
        super().__init__()
        for key, value in param_dict.items():
            self.__setattr__(key, value)
        self.max_speed = self.speed
        self.hp_max    = self.hp
        self.path      = self.path.path
        self.image     = image
        self.rect      = self.image.get_rect()

        self.slow_counter = 0

        Creeps.group.add(self)

    def move(self):
        self.rect.x += self.speed * self.path(self.rect.x, self.rect.y).x
        self.rect.y += self.speed * self.path(self.rect.x, self.rect.y).y

    def spawn(self, position):
        self.rect = position

    def lose_hp(self, hp):
        self.hp -= hp
            
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

    
