"""
Example of two units, one mobile and the other one static. 

The mobile tower moves with vim keys, shoots with q and
loses hp with c.
"""
import pygame

from pygame.sprite import Group

from helper.display import Displayer, Text, Rectangle, Image
from helper.unit    import Unit, Projectile, Weapon, HealthBar
from helper.vector  import Vector


def inflict_damage(damage, enemy):
    enemy.hp -= damage

class Spear(Projectile):
    def __init__(self, position: Vector, speed: Vector):
        spear_image = Image('images/lance.png', width=100, height=100)
        super().__init__(position, spear_image, speed, effects=[lambda enemy: inflict_damage(10, enemy)])


class NormalWeapon(Weapon):
    """
    Basic weapon throwing spears, inherits from Weapon.

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
    def __init__(self, attack_rate, attack_range, position):
        super().__init__(attack_rate, attack_range, Spear, position)


class SpearTower(Unit):
    def __init__(self, position):
        attack_rate = 30
        attack_range = 600
        weapon = NormalWeapon(attack_rate, attack_range, position)
        orange_tower = Image('images/tour_orange.xcf', 150, 200)
        super().__init__(position, move_speed=5, image=orange_tower, weapon=weapon)


class Game:

    def __init__(self):
        self.weapons = list()
        self.run = True
        width, heigth = (1200, 1000)

        self.displayer = Displayer(width, heigth)
        self.pressed_keys = dict()
        self.background = Rectangle(x=0, y=0, width=width, height=heigth, color=(0,0,255))

        self.tower = SpearTower(Vector(0,0))
        self.weapons.append(self.tower.weapon)
        self.target = SpearTower(Vector(500, 700))
        self.towers = Group()
        self.towers.add(self.target)
        self.towers.add(self.tower)
        self.ennemy_group = Group()
        self.ennemy_group.add(self.target)

        self.healthbars = list()
        self.healthbars.append(HealthBar(self.tower,  width=160, height=10))
        self.healthbars.append(HealthBar(self.target, width=160, height=10))

        self.projectiles = Group()

    def loop_callback(self):
        if self.pressed_keys.get(pygame.K_q):
            if self.tower.can_attack(self.target):
                self.projectiles.add(self.tower.attack(self.target))
        if self.pressed_keys.get(pygame.K_j):
            self.tower.move(Vector(0,1))
        if self.pressed_keys.get(pygame.K_k):
            self.tower.move(Vector(0,-1))
        if self.pressed_keys.get(pygame.K_l):
            self.tower.move(Vector(1,0))
        if self.pressed_keys.get(pygame.K_h):
            self.tower.move(Vector(-1,0))
        if self.pressed_keys.get(pygame.K_c):
            self.tower.hp -= 1

        self.displayer.display(self.background.surface, Vector(0,0))
        for tower in self.towers:
            if tower.hp == 0:
                tower.kill()
            self.displayer.display(tower.image, tower.position)
        for healthbar in self.healthbars:
            healthbar.draw()
        for weapon in self.weapons:
            weapon.cooldown -= 1
        for projectile in self.projectiles:
            projectile.move()
            self.displayer.display(projectile.image, projectile.position)
            collision_list = pygame.sprite.spritecollide(projectile, self.ennemy_group, False)
            print(collision_list)
            for ennemy in collision_list:
                projectile.apply_effects(ennemy)
                projectile.kill()


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


