from __future__    import annotations
from pygame.sprite import Sprite
from typing        import Union, Tuple, List, Callable, Type, Dict
from dataclasses   import dataclass
from abc           import ABC, abstractmethod

import pygame

from helper.vector  import Vector, distance
from helper.display import Image, Rectangle, Animation, Displayer


class Attacker(ABC):
    """Abstract class meant to be an attribute of buildings and units."""
    @abstractmethod
    def attack(self, ennemy: AbstractEntity):
        pass

    @abstractmethod
    def can_attack(self, ennemy: AbstractEntity) -> bool:
        pass


class AbstractEntity(ABC):
    """
    Basic abstract class for units and buildings.
    """
    position:  Vector
    image:     Image
    attacker:  Attacker
    hp_max:    int = 100
    hp:        int = 100


class Unit(Sprite, AbstractEntity):
    """
    Basic unit class, inherits from pygame.Sprite.

    Attributes:
        image:      pygame.Surface,
        position:   Vector,
        move_speed: int,
        rect:       pygame.rect, for collisions,
        healthbar:  HealthBar,
        weapon:     Weapon.
    Methods: attack, can_attack, move, can_move, draw.
    """
    def __init__(self, position: Vector, move_speed: int, image: Image, weapon: Weapon,
                 healthbar_width=80, healthbar_height=5, healthbar_x_offset=0, healthbar_y_offset=0):
        super().__init__()
        self.position = position
        self.move_speed = move_speed
        self.weapon = weapon
        self.weapon.position = self.position
        self.image = image
        self.rect = pygame.Rect(position.x, position.y, image.width, image.height)
        self.healthbar = HealthBar(self, healthbar_width, healthbar_height, 
                x_offset=healthbar_x_offset, y_offset=healthbar_y_offset)

    def attack(self, ennemy: AbstractEntity) -> Projectile: 
        return self.weapon.attack(ennemy)

    def can_attack(self, ennemy) -> bool:
        return self.weapon.can_attack(ennemy)

    def move(self, direction: Vector):
        """direction can be non-normalized and give varying speed."""
        self.position        += self.move_speed * direction
        self.weapon.position += self.move_speed * direction
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def can_move(self) -> bool:
        """In order to prevent from moving while shooting."""
        return self.weapon._has_cooldown()

    def draw(self, displayer: Displayer):
        displayer.display(self.image.surface, self.position)
        self.healthbar.draw()


class AnimatedUnit(Unit):
    """
    Animated unit class, inherits from Unit.

    Attributes:
        image:      pygame.Surface,
        position:   Vector,
        move_speed: int,
        rect:       pygame.rect, for collisions,
        healthbar:  HealthBar,
        weapon:     Weapon.
    Methods: attack, can_attack, move, can_move, draw, change_image
    """
    def __init__(self, position: Vector, move_speed: int, anim_dict: Dict[str, Animation], weapon: Weapon,
                 healthbar_width=80, healthbar_height=5, healthbar_x_offset=0, healthbar_y_offset=0):

        super().__init__(position, move_speed, anim_dict['walk'].images[0], weapon,
             healthbar_width, healthbar_height, healthbar_x_offset, healthbar_y_offset)
        self.anim_dict = anim_dict
        self.animation = anim_dict['walk']

    def change_image(self, key):
        self.animation = self.anim_dict[key]

    def draw(self, displayer: Displayer):
        """Overrides Unit.draw() in order to add the image animation."""
        self.image = self.animation.get_next_image()
        super().draw(displayer)


@dataclass
class Weapon(Attacker):
    """
    Meant to be posessed by a unit.

    Attributes:
        attack_rate: value to which the cooldown should be set, after it becomes non-positive, 
        attack_range: distance under which the weapon should fire, 
        projectile: a class inheriting from Projectile, with a constructor taking position and speed
        position: Most likely the position of the corresponding unit/building.
        cooldown

    Methods:
        can_attack: check if in range and cooldown,
        attack.
    """
    attack_rate:               int
    attack_range:              int
    projectile:               Type
    position:               Vector
    cooldown:                  int = 0

    def attack(self, enemy: AbstractEntity) -> Projectile:
        """
        Instantiate a projectile towards the ennemy and return it.
        Reset the cooldown value to attack_rate.
        """
        self.cooldown = self.attack_rate
        enemy_center = enemy.position + Vector(enemy.image.width / 2, enemy.image.height / 2)
        vector = enemy_center - self.position
        return self.projectile(self.position, vector)

    def can_attack(self, ennemy) -> bool:
        """Check if ennemy is in range and cooldown is positive."""
        return self._is_in_range(ennemy) and self._has_cooldown()

    def _is_in_range(self, ennemy: AbstractEntity) -> bool:
        return distance(ennemy.position, self.position) <= self.attack_range

    def _has_cooldown(self) -> bool:
        return self.cooldown <= 0


class Projectile(Sprite):
    """
    To be thrown by a weapon.

    Attributes:
        position,
        image,
        effects: dictionary of functions taking as parameter arguments
            on which to apply the effect.
        vector (gives the displacement).
    Method: move, append_effect, apply_effects.
    """
    def __init__(self, position: Vector, image: Image, speed: Vector, effects=list()):
        super().__init__()
        self.position = position
        self.image = image.surface
        self.rect = pygame.Rect(position.x, position.y, image.width, image.height)
        self.effects = effects
        norm = speed.norm()
        speed = (40/norm) * speed if norm != 0 else speed
        self.speed = speed

    def append_effect(self, effect):
        self.effects.append(effect)

    def move(self):
        self.position += self.speed
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def apply_effects(self, *args):
        for effect in self.effects:
            effect(*args)

@dataclass
class HealthBar:
    """
    Attributes:
        unit: AbstractEntity whose health it represents
        bg_color: Tuple[int, int, int]
        fg_color: Tuple[int, int, int]
    Method:
        draw: draws the healthbar onto the unit.
        Must be called after the unit has been drawn on screen.
    """
    unit: AbstractEntity
    width:  int = 80
    height: int = 5
    x_offset: int = 10
    y_offset: int =  0
    bg_color = (255, 50, 50)
    fg_color = (0, 255, 50)

    def draw(self):
        """
        Updates the healthbar and draws it onto the unit.
        """
        max_hp_rectangle = Rectangle(0, 0, self.width, self.height, self.bg_color)
        proportion = self.unit.hp / self.unit.hp_max 
        proportion = max(0.0001, proportion)
        hp_rectangle = Rectangle(0, 0, proportion * self.width, self.height, self.fg_color)
        position = (self.x_offset, self.y_offset)
        self.unit.image.surface.blit(max_hp_rectangle.surface, position)
        self.unit.image.surface.blit(hp_rectangle.surface, position)


