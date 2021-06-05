import pygame

from pygame.sprite import Sprite, Group
from abc           import ABC

class Entity(Sprite, ABC):
    """
    Expects a list of dictionaries of attributes 
    """
    image_path: str
    width:      int
    height:     int
    hp:         int

    group = Group()

    def __init__(self, dictionary_list, rectangle):

        super().__init__()
        self.level = 0
        self.dictionary_list = dictionary_list

        for key, value in dictionary_list[0].items():
            self.__setattr__(key, value)

        self.hp_max = self.hp

        self.define_image()

        self.rect  = self.image.get_rect()
        self.rect  = rectangle

        Entity.group.add(self)

    def define_image(self):
        self.image = pygame.image.load(self.image_path)
        self.image.convert()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        # Affiche le noir en transparent. Un peu du bricolage...
        self.image.set_colorkey((0,0,0))

    def update_health_bar(self, surface):
        color = (255, 50, 50)
        bar   = pygame.Rect(self.rect.x - 45, self.rect.y, 80, 5)
        pygame.draw.rect(surface, color, bar)
        color = (50, 255, 50)
        bar   = pygame.Rect(self.rect.x - 45, self.rect.y, 80 / self.hp_max * self.hp, 5)
        pygame.draw.rect(surface, color, bar)

    def lose_hp(self):
        self.hp -= 1
        if self.hp <= 0:
            self.kill()

    def upgrade(self, player):
        try:
            dictionary = self.dictionary_list[self.level + 1]
        except KeyError:
            print("[!] Level max")
            return
        cost = dictionary['cost']
        if player.gold < cost:
            print(f"[!] Trop pauvre, l'amélioration coûte {dictionary['cost']} pièces, quand tu n'en as",
                  f"que {player.gold}")
            return

        player.pay(cost)
        self.level += 1
        print(f"[*] Now level {self.level}")
        for key, value in dictionary.items():
            self.__setattr__(key, value)
        self.define_image()
