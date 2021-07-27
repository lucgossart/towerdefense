from typing import Tuple, List
from pygame.surface import Surface
from pygame.font    import SysFont
from pygame.display import set_mode
from pygame.sprite  import Sprite

import pygame
import pygame.image
import pygame.transform

from helper.vector import Vector

class Displayer:
    """
    Display surfaces on screen.

    Defines the main window when initialized.
    Attribute: window.
    Method:    display.
    """
    def __init__(self, width, height): 
        """Creates the main window, of width @width and height @heigth."""
        self.window = set_mode((width, height))

    def display(self, surface: Surface, position: Vector):
        """ Display a surface on screen."""
        self.window.blit(surface, (position.x, position.y))


class Text(Surface):
    """
    Text object.

    Inherits from pygame.Surface.
    Is displayed by a Displayer object using its image attribute:
    displayer.display(text.image)

    Attributes:
        font, font_color, image: pygame.Surface, position: Tuple[int, int].

    Methods:
        set_text, set_position.
    """
    def __init__(self, text: str, position: Tuple[int, int]=(0, 0), 
                 font="Verdana", fontsize=60, font_color=(0, 0, 0)):
        self.font  = SysFont(font, fontsize)
        self.font_color = font_color
        self.image = self.font.render(text, True, self.font_color)
        self.position = position

    def set_text(self, text: str):
        """Change text."""
        self.text = text
        self.image = self.font.render(text, True, self.font_color)
    
    def set_position(self, position):
        self.position = position


class Image:
    """
    To get surfaces from images.

    For each image file, the constructor should be called once only.
    The surface is then obtained via the get method.
    Attribute: surface,
    Methods:   get, resize.
    """
    def __init__(self, path: str):
        self.surface = pygame.image.load(path)

    def get(self, width: int, height: int, reverse: bool=False) -> Surface:
        if reverse:
            self.surface = pygame.transform.flip(self.surface, True, False)
        self.width  = width
        self.height = height
        return self.resize(self.surface, width, height)

    @staticmethod
    def resize(surface, width: int, height: int):
        return pygame.transform.scale(surface, (width, height))

        
class Rectangle:
    """
    Colored rectangle class.

    Attributes:
        surface, position.
    """
    def __init__(self, x, y, width, height, color):
        self.surface = Surface((width, height))
        self.surface.fill(color)
        self.position = (x, y)


class Animation(Sprite):
    """
    Class for animated surfaces.

    surfaces are pygame.Surface objects accessed via get_next_surface().
    Attributes:
        surfaces: List[Surface]
        index_current_surface: int
    Methods: get_next_surface, _load_surfaces
    """
    def __init__(self, path_list: List[str], width: int, height:int, reverse=False, period=70):
        super().__init__()
        self.surfaces = self._load_surfaces(path_list, width, height, reverse)
        self.index_current_surface = 0
        self._counter = 0
        self.period = period

    def _load_surfaces(self, path_list, width, height, reverse) -> List[Surface]:
        surfaces = list()
        for path in path_list:
            surfaces.append(Image(path).get(width, height, reverse))
        return surfaces

    def get_next_surface(self) -> Surface:
        self._counter += 1
        if self._counter >= self.period:
            length = len(self.surfaces)
            self.index_current_surface += 1
            self.index_current_surface %= length
            self._counter = 0
        return self.surfaces[self.index_current_surface]

