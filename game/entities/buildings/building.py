import pygame

from pygame.sprite import Group

from game.entities.generic_entity import Entity

class Building(Entity):
    hp:         int
    image_path: str

    group = Group()

    def __init__(self, *args):
        super().__init__(*args)
        Building.group.add(self)

