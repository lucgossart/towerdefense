import pygame

from .graphics.graphics import Displayer
from .graphics.text     import Message
from .graphics.cursor   import Cursor

from .entities.players.player import Player

from .controller.controller   import Controller

class Game():

    def __init__(self):

        self.pressed_keys  = dict()
        self.messages      = dict()
        self.players       = list()

    def set_cursor(self, cursor_images, grid_width, map_width, map_height):
        self.cursor = Cursor(cursor_images, grid_width, map_width, map_height)

    def set_displayer(self, window, background):
        self.displayer = Displayer(window, background, self.cursor)

    def set_controller(self, commands):
        self.controller = Controller(self.players, self.cursor)
        self.controller.set_bindings(commands)

    def set_player(self, base_hp, base_gold):
        new_player = Player(base_hp, base_gold)
        self.players.append(new_player)

    def main_loop(self, fps):
        clock    = pygame.time.Clock()
        compteur = 0
        run      = True
        while run:

            clock.tick(fps)
            compteur += 1
            compteur %= 5

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    self.pressed_keys[event.key] = True
                if event.type == pygame.KEYUP:
                    self.pressed_keys[event.key] = False
                if event.type == pygame.MOUSEMOTION:
                    self.cursor.place_at(*event.pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pressed_keys[event.button] = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.pressed_keys[event.button] = False


            if compteur == 0:
                self.controller.perform_actions(self.pressed_keys)

            self.displayer.display()

