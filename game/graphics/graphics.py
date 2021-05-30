import pygame

class Displayer:

    groups_to_draw = dict()

    def __init__(self, window, background, cursor):
        self.background = background
        self.map_width  = background.get_width()
        self.map_height = background.get_height()
        self.window     = window
        self.cursor     = cursor
        pass

    def display(self):
        self.window.blit(self.background, (0, 0))
        self.window.blit(self.cursor.image, (self.cursor.rect.x % self.map_width, self.cursor.rect.y % self.map_height))
        for group in self.groups_to_draw.values():
            group.draw()
        pygame.display.update()




