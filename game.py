import pygame
import pygame.sprite
from pygame.sprite import Sprite, Group
from constants import *
from projectiles import Projectiles
from towers      import RedTower
from player      import Player
from creeps      import Creeps
from cursor      import Cursor
from towers      import Tower
from waves       import Wave

pygame.display.set_caption('TowerDefense de PGM\nRoad to 6k MMR')

window       = pygame.display.set_mode((WIDTH, HEIGHT))
background   = pygame.image.load('images/map.jpg').convert()

class Game():

    def __init__(self):

        self.player        = Player()
        self.cursor        = Cursor()
        self.pressed_keys  = dict()
        self.messages      = dict()
        self.font          = pygame.font.SysFont(FONT, FONT_SIZE)
        self.compteur      = 0
        self.wave          = 0

    def draw(self):

        window.blit(background, (0, 0))
        window.blit(self.cursor.image, (self.cursor.rect.x % WIDTH, self.cursor.rect.y % HEIGHT))

        for tower in Tower.group:
            window.blit(tower.image, tower.rect)
            tower.attack()
            tower.reloading_time -= 1

        for message, position in self.messages.values():
            window.blit(message, position)

        for creep in Creeps.group:
            creep.move()
            window.blit(creep.image, creep.rect)

        for projectile in Projectiles.group:
            projectile.move()
            window.blit(projectile.image, projectile.rect)

        self.handle_collisions()

        pygame.display.update()

        if self.compteur % 1200 == 0:
            self.compteur = 0
            try:
                Wave(self.wave).spawn()
            except Exception:
                self.wave -= 1
                Wave(self.wave).spawn()
            self.wave += 1
        self.compteur += 1
        

    def update(self):

        self.move_cursor()
        self.update_cursor_state()

    def move_cursor(self):

        if self.pressed_keys.get(DOWN):
            self.cursor.move_down()

        if self.pressed_keys.get(UP):
            self.cursor.move_up()

        if self.pressed_keys.get(RIGHT):
            self.cursor.move_right()

        if self.pressed_keys.get(LEFT):
            self.cursor.move_left()

    def update_cursor_state(self):

        if self.pressed_keys.get(TOUR_POURPRE):
            self.cursor.current_state = RedTower(self.cursor.rect)

        if self.pressed_keys.get(CANCEL):
            self.cursor.current_state = self.cursor
            self.cursor.image = CURSOR_IMAGE

        if self.pressed_keys.get(DROP) and self.cursor.current_state != self.cursor:
            self.pop_tower()
            self.cursor.current_state = self.cursor
            self.cursor.image = CURSOR_IMAGE

        self.cursor.image = self.cursor.current_state.image

    def pop_tower(self):

        tower = self.cursor.current_state
        if self.player.gold < tower.cost:
            print("Pas assez riche")
            return

        Tower.group.add(tower)
        self.player.pay(tower.cost)
        self.cursor.current_state.rect = pygame.Rect(self.cursor.rect.x, self.cursor.rect.y, GRID_WIDTH, TOWER_HEIGHT)

    def add_message(self, key, message, position):
        message_surface = self.font.render(message, True, FONT_COLOR)
        self.messages[key] = (message_surface, position)

    def handle_collisions(self):
        collision_dict = pygame.sprite.groupcollide(Projectiles.group, Creeps.group, True, False)
        for projectile, creep in collision_dict.items():
            projectile.do_damage(creep[0], Creeps.group)



