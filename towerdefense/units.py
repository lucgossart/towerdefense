"""
Concrete units, weapons, projectiles, buildings...
"""
import pygame

from pygame.sprite import Group

from helper.display import Displayer, Text, Rectangle, Image, Animation
from helper.unit    import AnimatedUnit, Projectile, Weapon, HealthBar
from helper.vector  import Vector, distance

from typing import Dict

def inflict_damage(damage, enemy):
    enemy.hp -= damage

def splash_damage(damage, splash_range, enemy, group):
    for other_enemy in group:
        if distance(enemy.position, other_enemy.position) <= splash_range:
            other_enemy.hp -= damage


class Spear(Projectile):

    def __init__(self, position: Vector, speed: Vector, damage: int):
        spear_image = Image('images/lance.png', width=50, height=50)
        super().__init__(position, spear_image, speed, 
                effects=[lambda enemy, group: inflict_damage(damage, enemy)])

class Bomb(Projectile):

    def __init__(self, position: Vector, speed: Vector, damage: int, splash_range: int):
        spear_image = Image('images/bomb.png', width=50, height=50)
        super().__init__(position, spear_image, speed, 
                effects=[lambda enemy, group: splash_damage(damage, splash_range, enemy, group)])

class AnimDict:
        walking_santa  = [f'images/santa/Walk ({i}).png' for i in range(1, 12)]
        standing_santa = [f'images/santa/Idle ({i}).png' for i in range(1, 12)]
        santa_anims = {
                'walk': Animation(walking_santa,  100, 100), 
                'fire': Animation(standing_santa, 100, 100)
        }
        reverse_santa_anims = {
                'walk': Animation(walking_santa,  100, 100, reverse=True),
                'fire': Animation(standing_santa, 100, 100, reverse=True)
        }
        walking_archer  = [f'images/archer/adventurer-run-0{i}.png' for i in range(6)]
        shooting_archer = [f'images/archer/adventurer-bow-0{i}.png' for i in range(9)]
        archer_anims = {
                'walk': Animation(walking_archer,  100, 100), 
                'fire': Animation(shooting_archer, 100, 100)
        }
        reverse_archer_anims = {
                'walk': Animation(walking_archer,  70, 70, reverse=True),
                'fire': Animation(shooting_archer, 70, 70, reverse=True)
        }

class NormalWeapon(Weapon):
    """
    Basic weapon throwing spears, inherits from Weapon.

    Attributes:
        damage, 
        attack_rate: value to which the cooldown should be set, after it becomes non-positive, 
        attack_range: distance under which the weapon should fire, 
        projectile: spear
        position: Most likely the position of the corresponding unit/building.
        cooldown

    Methods:
        can_attack: check if in range and cooldown,
        attack.
    """
    def __init__(self, attack_rate, attack_range, position, damage):
        projectile_class = lambda position, speed: Spear(position, speed, damage)
        super().__init__(attack_rate, attack_range, projectile_class, position)


class BombWeapon(Weapon):
    """
    Weapon throwing bombs with splash damage, inherits from Weapon.

    Attributes:
        attack_rate: value to which the cooldown should be set, after it becomes non-positive, 
        attack_range: distance under which the weapon should fire, 
        projectile: Spear class
        position: Most likely the position of the corresponding unit/building.
        cooldown

    Methods:
        can_attack: check if in range and cooldown,
        attack.
    """
    def __init__(self, attack_rate, attack_range, position, damage, splash_range):
        projectile_class = lambda position, speed: Bomb(position, speed, damage, splash_range)
        super().__init__(attack_rate, attack_range, projectile_class, position)


class Santa(AnimatedUnit):
    """
    Santa inheriting from AnimatedUnit.

    Attributes:
        image:      pygame.Surface,
        position:   Vector,
        move_speed: int,
        rect:       pygame.rect, for collisions,
        healthbar:  HealthBar,
        weapon:     Weapon.
    Methods: attack, can_attack, move, can_move, draw, change_image
    """
    def __init__(self, position, anim_dict: Dict[str, Animation]):
        attack_rate = 30
        attack_range = 300
        damage = 10
        splash_range = 100
        weapon = BombWeapon(attack_rate, attack_range, position, damage, splash_range)
        super().__init__(position, move_speed=3, anim_dict=anim_dict, weapon=weapon)
        self.anim_dict = anim_dict
        self.animation = anim_dict['walk']


class Archer(AnimatedUnit):
    """
    Archer inheriting from AnimatedUnit.

    Attributes:
        image:      pygame.Surface,
        position:   Vector,
        move_speed: int,
        rect:       pygame.rect, for collisions,
        healthbar:  HealthBar,
        weapon:     Weapon.
    Methods: attack, can_attack, move, can_move, draw, change_image
    """
    def __init__(self, position, anim_dict: Dict[str, Animation]):
        attack_rate = 40
        attack_range = 500
        damage = 15
        weapon = NormalWeapon(attack_rate, attack_range, position, damage)
        super().__init__(position, move_speed=3, anim_dict=anim_dict, weapon=weapon,
            healthbar_x_offset=0, healthbar_y_offset=0)
        self.anim_dict = anim_dict
        self.animation = anim_dict['walk']

