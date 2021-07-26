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


class Image(Surface):
    """
    Wrapper inheriting from pygame.Surface.

    Attribute: surface,
    Method:    resize.
    """
    def __init__(self, path: str, width: int, height: int, reverse: bool=False):
        self.surface = pygame.image.load(path)
        if reverse:
            self.surface = pygame.transform.flip(self.surface, True, False)
        self.width  = width
        self.height = height
        self.resize(width, height)

    def resize(self, width: int, height: int):
        self.surface = pygame.transform.scale(self.surface, (width, height))

        
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
    Class for animated images.

    Images are pygame.Surface objects accessed get_next_image().
    Attributes:
        images: List[Image]
        index_current_image: int
    Methods: get_next_image, _load_images
    """
    def __init__(self, path_list: List[str], width: int, height:int, reverse=False, period=70):
        super().__init__()
        self.images = self._load_images(path_list, width, height, reverse)
        self.index_current_image = 0
        self._counter = 0
        self.period = period

    def _load_images(self, path_list, width, height, reverse) -> List[Image]:
        images = list()
        for path in path_list:
            images.append(Image(path, width, height, reverse))
        return images

    def get_next_image(self) -> Image:
        self._counter += 1
        if self._counter >= self.period:
            length = len(self.images)
            self.index_current_image += 1
            self.index_current_image %= length
            self._counter = 0
        return self.images[self.index_current_image]

