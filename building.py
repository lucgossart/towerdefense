from constants import *
from tower_config import TOWERS
from pygame.sprite import Sprite, Group
from abc import ABC, abstractmethod

class Building(Sprite, ABC):
    hp:         int
    image_path: str

    group = Group()

    def __init__(self, properties_dict_list, type_, rectangle):

        super().__init__()
        self.level = 0
        self.properties_dict_list = properties_dict_list
        for key, value in properties_dict_list[0].items():
            self.__setattr__(key, value)

        self.hp_max = self.hp

        self.type           = type_
        
        self.image = pygame.image.load(self.image_path).convert()
        self.image = pygame.transform.scale(self.image, (BUILDING_WIDTH, BUILDING_HEIGHT))

        self.rect       = self.image.get_rect()
        self.rect       = rectangle

        Building.group.add(self)

    def update_health_bar(self, surface):
        color = (255, 50, 50)
        bar   = pygame.Rect(self.rect.x - 45, self.rect.y, 80, 5)
        pygame.draw.rect(surface, color, bar)
        color = (50, 255, 50)
        bar   = pygame.Rect(self.rect.x - 45, self.rect.y, 80 / self.hp_max * self.hp, 5)
        pygame.draw.rect(surface, color, bar)

    def upgrade(self):
        self.level += 1
        try:
            for key, value in self.properties_dict_list[self.level].items():
                self.__setattr__(key, value)
            self.hp_max = self.hp
        except Exception as e:
            print(e)
        self.image = pygame.image.load(self.image_path).convert()
        self.image = pygame.transform.scale(self.image, (TOWER_WIDTH, TOWER_HEIGHT))

    def lose_hp(self):
        self.hp -= 1
        if self.hp <= 0:
            self.kill()


class Rempart(Building):

    def __init__(self, rectangle):
        super().__init__(TOWERS['rempart'], 'rempart', rectangle)



