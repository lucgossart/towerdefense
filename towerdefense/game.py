"""
Two armies comming to the center of the map and fighting.
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

def get_anim_dict(class_, reverse) -> Dict[str, Animation]:
    if class_ == Santa:
        return AnimDict.santa_anims
    else:
        return AnimDict.reverse_archer_anims


class Game:

    def __init__(self):
        self.weapons = list()
        self.run = True
        self.width, self.height = (1200, 1000)

        self.setup_display_and_keys()

        self.left_group:  Group = self.setup_units(Santa, 10, 0)
        self.right_group: Group = self.setup_units(Archer, 12, self.width, reverse=True)

        # The key is the enemy group of the projectiles
        self.projectiles = {self.left_group: Group(), self.right_group: Group()}

    def setup_display_and_keys(self):
        self.displayer = Displayer(self.width, self.height)
        self.pressed_keys = dict()
        self.background = Rectangle(x=0, y=0, width=self.width, height=self.height, color=(0,0,255))

    def setup_units(self, class_, number: int, abscissa: int, reverse: bool=False) -> Group:
        group = Group()
        for i in range(number):
            position = Vector(abscissa, i / number * self.height)
            anim_dict = get_anim_dict(class_, reverse)
            unit = class_(position, anim_dict)
            group.add(unit)
        return group

    def unit_actions(self, unit: AnimatedUnit, enemy_group: Group) -> None:
        if unit.hp <= 0:
            unit.kill()
        for enemy in enemy_group:
            if not unit.weapon._has_cooldown():
                break
            if unit.can_attack(enemy):
                self.projectiles[enemy_group].add(unit.attack(enemy))
                break
        if unit.can_move():
            unit.change_image('walk')
            unit.move(self.vector_field(enemy_group))
        else:
            unit.change_image('fire')
        unit.weapon.cooldown -= 1
        unit.draw(self.displayer)

    def projectile_actions(self, projectile, enemy_group):
        projectile.move()
        self.displayer.display(projectile.image, projectile.position)
        collision_list = pygame.sprite.spritecollide(projectile, enemy_group, False)
        for enemy in collision_list:
            projectile.apply_effects(enemy, enemy_group)
            projectile.kill()

    def vector_field(self, group) -> Vector:
        return Vector(1, 0) if group == self.right_group else Vector(-1, 0)

    def loop_callback(self):

        self.displayer.display(self.background.surface, Vector(0,0))
        for santa in self.left_group:
            self.unit_actions(santa, self.right_group)
        for archer in self.right_group:
            self.unit_actions(archer, self.left_group)
        for enemies, projectiles in self.projectiles.items():
            for projectile in projectiles:
                self.projectile_actions(projectile, enemies)

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                self.pressed_keys[event.key] = True
            if event.type == pygame.KEYUP:
                self.pressed_keys[event.key] = False
            if event.type == pygame.MOUSEMOTION:
                self.mouse_position = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.pressed_keys[event.button] = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.pressed_keys[event.button] = False


