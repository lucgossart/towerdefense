"""Used to display the cursor."""
import pygame 

from pygame.surface import Surface
from typing         import Type, Optional, Callable
from dataclasses    import dataclass

from helper.unit    import Building, AbstractEntity
from helper.display import Image, Displayer
from helper.vector  import Vector

MaybeBuildingClass = Optional[Callable] 

@dataclass
class Cursor:
    """
    Cursor class.

    Always positioned on a vertex of the lattice. 
    A building image can be put on top of it to indicate a currently selected
    building to place.
    Attributes: 
        surface: pygame.surface, 
        grid_width, grid_height: int, int
        position: Vector
        current_building: None or class of Building,
        selected_entity: None or AbstractEntity
    Methods:
        set_current_building, 
        place_current_building,
        set_surface,
        draw,
        draw_selected_building,
        place_on_grid,
        move.
    """
    surface:          Surface
    grid_width:       int
    grid_height:      int
    position:         Vector                   = Vector(0, 0)
    current_building: MaybeBuildingClass       = None
    building_image:   Optional[Image]          = None
    selected_entity:  Optional[AbstractEntity] = None

    def set_current_building(self, building_class: MaybeBuildingClass) -> None:
        """
        Select the current building that will be drawn on the cursor
        when draw() is called. 

        Can be None.
        The method place_current_building will put this building
        on the map at the position of the cursor.
        """
        if building_class == None:
            self.building_image = None
            self.current_building = None
            return
        self.current_building = building_class
        self.building_image   = self.current_building.image

    def place_current_building(self, *args) -> Optional[Building]:
        """
        Create current building at current position and return it, if 
        a current building is selected.

        Then deselects current building.
        """
        if self.current_building == None:
            return
        building = self.current_building(self.position, *args)
        self.set_current_building(None)
        return building

    def draw(self, displayer: Displayer) -> None:
        displayer.display(self.surface, self.position)

    def draw_selected_building(self, displayer) -> None:
        if self.building_image != None:
            displayer.display(self.building_image, self.position)

    def set_surface(self, surface: Surface, transparency: int=255) -> None:
        """
        Define the appearance of the cursor. 

        Can be created as a colored Rectangle.
        Transparency goes from 0 (transparent) to 255 (opaque).
        """
        self.surface = surface
        self.surface.set_alpha(transparency)

    def select_entity(self, entity: Optional[AbstractEntity]):
        """
        Select an entity. If entity is None, unselect.

        Sets the cursor at this position and scales its image 
        to the proper size and removes transparency if entity is not None.
        If entity is None, transparency is set to zero but no rescaling
        of the surface is done.
        """
        self.selected_entity = entity 
        if entity:
            self.surface = Image.resize(self.surface, entity.surface.get_width(), entity.surface.get_height())
            self.surface.set_alpha(255)
            self.position = entity.position
        else: 
            self.surface.set_alpha(0)
        
    def place_on_grid(self, position: Vector) -> None:
        """Sets the cursor at the required position modulo the grid."""
        x = position.x - (position.x % self.grid_width)
        y = position.y - (position.y % self.grid_height)
        self.position = Vector(x, y)

    def move(self, nb_case_x: int, nb_case_y: int) -> None:
        """Shift position by the number of cases passed in arguments."""
        self.position += Vector(nb_case_x * self.grid_width, nb_case_y * self.grid_height)
