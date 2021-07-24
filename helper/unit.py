from __future__    import annotations
from pygame.sprite import Sprite
from typing        import Union, Tuple, List, Callable, Type
from dataclasses   import dataclass
from abc           import ABC, abstractmethod

import pygame

from helper.vector  import Vector, distance
from helper.display import Image, Rectangle


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


# @dataclass
# class Displacer(ABC):
#     """Handles diplacement of units aand buildings."""
#     position:   Vector
#     move_speed: int

#     @abstractmethod
#     def move(self, vector: Vector):
#         """Move in the direction given by vector."""


# @dataclass
# class BasicDisplacer(Displacer):
#     """
#     Implements Displacer.

#     Attributes:
#         position,
#         move_speed
#     Method:
#         move.
#     """


class Unit(Sprite, AbstractEntity):
    """
    Basic unit class, inherits from pygame.Sprite.

    Attributes:
        image:     Image,
        displacer: Displacer
        weapon:    Weapon.

    Attacking and moving are performed via self.weapon.attack(ennemy) and 
    self.displacer.move(vector).
    """
    def __init__(self, position: Vector, move_speed: int, image: Image, weapon: Weapon):
        super().__init__()
        self.position = position
        self.move_speed = move_speed
        self.weapon = weapon
        self.weapon.position = self.position
        self.image = image.surface
        self.rect = pygame.Rect(position.x, position.y, image.width, image.height)

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


@dataclass
class Weapon(Attacker):
    """
    Meant to be posessed by a unit.

    Attributes:
        attack_rate: value to which the cooldown should be set, after it becomes non-positive, 
        attack_range: distance under which the weapon should fire, 
        projectile: a class inheriting from Projectile,
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

    def attack(self, ennemy: AbstractEntity) -> Projectile:
        """
        Instantiate a projectile towards the ennemy and return it.
        Reset the cooldown value to attack_rate.
        """
        self.cooldown = self.attack_rate
        vector = ennemy.position - self.position
        return self.projectile(self.position + Vector(100, 100), vector)

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
        effects: dictionary of functions taking as parameter a group
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
        speed = (40/norm) * speed
        self.speed = speed

    def append_effect(self, effect):
        self.effects.append(effect)

    def move(self):
        self.position += self.speed
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def apply_effects(self, group):
        for effect in self.effects:
            effect(group)

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
    fg_color = (50, 255, 50)

    def draw(self):
        """
        Updates the healthbar and draws it onto the unit.
        """
        max_hp_rectangle = Rectangle(0, 0, self.width, self.height, self.bg_color)
        proportion = self.unit.hp / self.unit.hp_max 
        proportion = max(0.0001, proportion)
        hp_rectangle = Rectangle(0, 0, proportion * self.width, self.height, self.fg_color)
        position = (self.x_offset,self.y_offset)
        self.unit.image.blit(max_hp_rectangle.surface, position)
        self.unit.image.blit(hp_rectangle.surface, position)


