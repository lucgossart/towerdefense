import pygame
from pygame.sprite import Sprite, Group
from constants import *
from towers import RedTower
from player import Player



pygame.display.set_caption('TowerDefense de PGM')


# CURSOR = pygame.image.load('images/cursor')

window       = pygame.display.set_mode((WIDTH, HEIGHT))
background   = pygame.image.load('images/map.jpg').convert()

class Game():

    def __init__(self):
        self.player       = Player()
        self.cursor       = Cursor()
        self.pressed_keys = dict()
        self.towers       = Group()

    def draw(self):
        window.blit(background, (0, 0))
        window.blit(self.cursor.image, (self.cursor.rect.x % WIDTH, self.cursor.rect.y % HEIGHT))
        self.towers.draw(window)
        pygame.display.update()

    def update(self):
        self.move_cursor()
        self.update_cursor_state()

    def move_cursor(self):

        if self.pressed_keys.get(DOWN):
            self.cursor.move_down()

        if self.pressed_keys.get(UP):
            self.cursor.move_up()

        if self.pressed_keys.get(RIGHT):
            self.cursor.move_right()

        if self.pressed_keys.get(LEFT):
            self.cursor.move_left()

    def update_cursor_state(self):

        if self.pressed_keys.get(TOUR_POURPRE):
            self.cursor.current_state = RedTower(self.cursor.rect)

        if self.pressed_keys.get(CANCEL):
            self.cursor.current_state = self.cursor
            self.cursor.image = CURSOR_IMAGE

        if self.pressed_keys.get(DROP) and self.cursor.current_state != self.cursor:
            self.pop_tower()
            self.cursor.current_state = self.cursor
            self.cursor.image = CURSOR_IMAGE

        self.cursor.image = self.cursor.current_state.image

    def pop_tower(self):

        tower = self.cursor.current_state
        if self.player.gold < tower.cost:
            print("Pas assez riche")
            return

        self.towers.add(tower)
        self.player.pay(tower.cost)
        self.cursor.current_state.rect = pygame.Rect(self.cursor.rect.x, self.cursor.rect.y, GRID_WIDTH, TOWER_HEIGHT)
    


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




