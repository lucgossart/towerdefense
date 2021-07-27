"""
Create a casern with the mouse and pop units from it.
"""
import pygame

from pygame.sprite import Group

from helper.display import Displayer, Text, Rectangle, Image, Animation
from helper.unit    import AnimatedUnit, Projectile, Weapon, HealthBar, AbstractEntity
from helper.vector  import Vector, distance

from towerdefense.cursor    import Cursor
from towerdefense.buildings import Casern, basic_casern_image

from typing import Dict, Optional

LEFT_CLICK = 1

class Game:

    def __init__(self):
        self.run = True
        self.width, self.height = 1200, 1000
        self.grid_width, self.grid_height = 80, 80
        self.entities = Group()

        basic_cursor_surface = Rectangle(0, 0, 2 * self.grid_width, 2 * self.grid_height, 
                                        (255, 180, 0)).surface
        self.cursor = Cursor(basic_cursor_surface, self.grid_width, self.grid_height)
        self.cursor.surface.set_alpha(0)
        self.casern_class = lambda position: Casern(position, position + Vector(0, -self.grid_width),
                hp=500, image_width=2*self.grid_width, image_height=2*self.grid_height)
        self.casern_class.image = basic_casern_image.get(2 * self.grid_width, 2 * self.grid_height)

        self.casern_group = Group()

        self.setup_display_and_keys()

        # The key is the enemy group of the projectiles

    def setup_display_and_keys(self):
        self.mouse_position = (0, 0)
        self.displayer = Displayer(self.width, self.height)
        self.pressed_keys = dict()
        self.background = Rectangle(x=0, y=0, width=self.width, height=self.height, color=(0,0,255))


    def loop_callback(self):
        self.displayer.display(self.background.surface, Vector(0,0))
        if not self.cursor.selected_entity:
            self.cursor.place_on_grid(Vector(*self.mouse_position))
        if self.pressed_keys.get(pygame.K_c):
            self.cursor.set_current_building(self.casern_class)
            self.cursor.select_entity(None)
        if self.pressed_keys.get(pygame.K_ESCAPE):
            self.cursor.set_current_building(None)
            self.cursor.select_entity(None)
        if self.pressed_keys.get(LEFT_CLICK):
            self.find_entity_to_select()
            self.place_building_if_needed()

        self.cursor.draw(self.displayer)
        for casern in self.casern_group:
            casern.draw(self.displayer)
        self.cursor.draw_selected_building(self.displayer)

    def find_entity_to_select(self) -> None:
        if self.cursor.current_building != None:
            self.cursor.select_entity(None)
            return
        for entity in self.entities:
            rect = pygame.Rect(entity.position.x, entity.position.y, entity.surface.get_width(), 
                               entity.surface.get_height())
            if rect.collidepoint(*self.mouse_position):
                self.cursor.select_entity(entity)
                return
        self.cursor.select_entity(None)

    def place_building_if_needed(self) -> None:
        casern = self.cursor.place_current_building()
        if casern:
            rect = self.cursor.surface
            self.entities.add(casern)
            self.casern_group.add(casern)
            self.cursor.set_current_building(None)

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                self.pressed_keys[event.key] = True
            if event.type == pygame.KEYUP:
                self.pressed_keys[event.key] = False
            if event.type == pygame.MOUSEMOTION:
                self.mouse_position = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.pressed_keys[event.button] = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.pressed_keys[event.button] = False


