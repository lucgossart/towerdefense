import pygame

from pygame.sprite import Group, Sprite

class Displayer:

    groups_to_draw = {"selection": Group()}

    def __init__(self, window, background, cursor, selector_image):
        self.background = background
        self.map_width  = background.get_width()
        self.map_height = background.get_height()
        self.window     = window
        self.cursor     = cursor

        self.selector_image = selector_image
        self.create_selection_sprite()

    def create_selection_sprite(self):
        self.selection_sprite       = Sprite()
        self.selection_sprite.image = self.selector_image
        self.selection_sprite.rect  = self.selection_sprite.image.get_rect()

    def display(self):
        self.window.blit(self.background, (0, 0))
        self.groups_to_draw['selection'].draw(self.window)
        self.blit(self.cursor)
        for group in self.groups_to_draw.values():
            for entity in group:
                self.blit(entity)
        pygame.display.update()

    def blit(self, sprite):
        self.window.blit(sprite.image, (sprite.rect.x % self.map_width, sprite.rect.y % self.map_height))

    def display_selection(self, x, y, width, height):
        self.selection_sprite.image = pygame.transform.scale(self.selection_sprite.image, (width, height))
        self.selection_sprite.rect  = pygame.Rect(x, y, width, height)
        self.groups_to_draw['selection'].add(self.selection_sprite)
