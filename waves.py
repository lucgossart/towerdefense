from creeps import Creeps
from random import randint
from constants import *
import pygame


class Wave:

    def __init__(self, index):
        self.index = index

    def spawn(self):
        param_dict = WAVES[self.index]
        for _ in range(param_dict['number_of_creeps']):
            hp    = param_dict['hp']
            speed = param_dict['speed']
            position = pygame.Rect(randint(0, WIDTH), -randint(0, 1000), GRID_WIDTH, GRID_WIDTH)
            Creeps(hp, speed).spawn(position)
