from pygame.sprite import Sprite
from math import floor

class Cursor(Sprite):

    def __init__(self, cursor_images, grid_width, map_width, map_height):
        super().__init__()
        self.image  = cursor_images['usual']
        self.images = cursor_images
        self.rect   = self.image.get_rect()

        self.grid_width = grid_width
        self.map_width  = map_width
        self.map_height = map_height

        # Change quand on sélectionne une tour 
        self.current_state = self

    def move_right(self):
        self.rect.x += self.grid_width
        self.rect.x %= self.map_width

    def move_left(self):
        self.rect.x -= self.grid_width
        self.rect.x %= self.map_width

    def move_up(self):
        self.rect.y -= self.grid_width
        self.rect.y %= self.map_height

    def move_down(self):
        self.rect.y += self.grid_width
        self.rect.y %= self.map_height

    def select_tower(self, tower_generator):
        tower = next(tower_generator)
        self.rect = tower.rect
        return tower

    def place_at(self, x, y):
        self.rect.x = self.grid_width * floor(x // self.grid_width)
        self.rect.y = self.grid_width * floor(y // self.grid_width)

    def set_image(self, key):
        self.image = self.images[key]





