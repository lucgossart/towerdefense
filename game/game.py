import pygame

from pygame.sprite import Sprite

from .graphics.graphics import Displayer
from .graphics.text     import Message
from .graphics.cursor   import Cursor

from .entities.generic_entity   import Entity
from .entities.units.units      import Unit
from .entities.buildings.towers import Tower
from .entities.players.player   import Player
from .controller.controller     import Controller

class Game():

    def __init__(self):

        self.pressed_keys  = dict()
        self.messages      = dict()
        self.players       = list()

    def set_cursor(self, cursor_image, grid_width, map_width, map_height):
        self.cursor = Cursor(cursor_image, grid_width, map_width, map_height)

    def set_displayer(self, window, background, selector_image):
        self.displayer   = Displayer(window, background, self.cursor, selector_image)
        self.displayer.groups_to_draw['entities'] = Entity.group

    def set_controller(self, commands):
        self.controller = Controller(self.players, self.cursor, Tower.group, self.displayer, buildings_positions=dict())
        self.controller.set_bindings(commands)

    def set_player(self, base_hp, base_gold):
        new_player = Player(base_hp, base_gold)
        self.players.append(new_player)

    def main_loop(self, fps):
        clock    = pygame.time.Clock()
        compteur = 0
        self.run      = True
        while self.run:

            clock.tick(fps)
            compteur += 1
            compteur %= 5

            self.get_events()

            if compteur == 0:
                self.controller.perform_actions(self.pressed_keys)
                for unit in Unit.group:
                    unit.move()
                    unit.try_to_attack()


            self.displayer.display()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                self.pressed_keys[event.key] = True
            if event.type == pygame.KEYUP:
                self.pressed_keys[event.key] = False
            if event.type == pygame.MOUSEMOTION:
                self.controller.handle_mouse(*event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.pressed_keys[event.button] = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.pressed_keys[event.button] = False

