import pygame
from pygame.sprite import Sprite
from constants import *

class Cursor(Sprite):

    def __init__(self):
        super().__init__()
        self.image = CURSOR_IMAGE
        self.image = pygame.transform.scale(self.image, (GRID_WIDTH, GRID_WIDTH))
        self.rect  = self.image.get_rect()

        # Change quand on sélectionne une tour 
        self.current_state = self

    def move_right(self):
        self.rect.x += GRID_WIDTH

    def move_left(self):
        self.rect.x -= GRID_WIDTH

    def move_up(self):
        self.rect.y -= GRID_WIDTH

    def move_down(self):
        self.rect.y += GRID_WIDTH




