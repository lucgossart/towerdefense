from typing import Type

from helper.unit    import Building, Unit
from helper.display import Image
from helper.vector  import Vector

    
basic_casern_image = Image('images/tavern/medieval-tavern_60000.png', width=160, height=160)
def casern_image(image_width, image_height): 
    basic_casern_image.resize(image_width, image_height)
    return basic_casern_image

class Casern(Building):
    """
    Building that can pop units. 

    Inherits from Building.
    Attributes:
        position:  Vector, 
        image:     Image, 
        healthbar: HealthBar,
        hp:        int,
        hp_max:    int,
        rect: pygame.Rect for collisions
    Method:
        draw,
        pop_unit.
    """ 
    def __init__(
        self, 
        position: Vector, 
        popping_position: Vector, 
        hp: int, 
        image_width: int, 
        image_height: int, 
        healtbar_width=120, 
        healtbar_height=6, 
        healtbar_x_offset=40, 
        healtbar_y_offset=0
    ):

        self.popping_position = popping_position
        image = casern_image(image_width, image_height)
        super().__init__(position, hp, image, healtbar_width, healtbar_height, 
                         healtbar_x_offset, healtbar_y_offset)

    def pop_unit(self, unit_class) -> Unit:
        """
        Takes a concrete unit class as argument and creates one of its 
        representents at popping_position.
        """
        return unit_class(self.popping_position)

