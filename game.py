import pygame
import pygame.sprite
from pygame.sprite import Sprite, Group
from constants import *
from projectiles import Projectiles
from towers      import TowerFactory
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

        self.add_message('score', "Score:", (0, 0))
        self.add_message('gold',  "Gold: ", (0, 40))
        self.add_message('hp',    "HP:   ", (0, 80))

    def draw(self):

        window.blit(background, (0, 0))
        window.blit(self.cursor.image, (self.cursor.rect.x % WIDTH, self.cursor.rect.y % HEIGHT))

        if self.player.hp <= 0:
            window.blit(self.font.render("NOOB", True, FONT_COLOR), (300, 450))

        for key, (text, position) in self.messages.items():
            message_surface = self.font.render(text + str(self.player.__getattribute__(key)), True, FONT_COLOR)
            window.blit(message_surface, position)

        for tower in Tower.group:
            window.blit(tower.image, tower.rect)
            tower.attack()
            tower.reloading_time -= 1

        # for message, position in self.messages.values():
        #     window.blit(message, position)

        for creep in Creeps.group:
            if creep.rect.y > HEIGHT:
                self.player.hp -= 1
                creep.kill()
            if creep.slow_counter <= 0:
                creep.recover_max_speed()
            else:
                creep.slow_counter -= 1
            if creep.hp <= 0:
                self.player.get_income(creep.creep_income)
                creep.die()
            creep.move()
            creep.update_health_bar(window)
            window.blit(creep.image, creep.rect)

        for projectile in Projectiles.group:
            projectile.move()
            window.blit(projectile.image, projectile.rect)

        self.handle_collisions()


        if self.compteur % 1200 == 600:
            self.compteur = 0
            try:
                Wave(self.wave).spawn()
                self.player.get_income(WAVES[self.wave]['start_income'])
            except Exception:
                self.wave -= 1
                Wave(self.wave).spawn()
            self.wave += 1
        self.compteur += 1

        pygame.display.update()
        

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

        for key, value in TOWERS.items():
            if self.pressed_keys.get(value['shortcut']) and self.cursor.current_state == self.cursor:
                self.cursor.current_state = TowerFactory.create_tower(key, self.cursor.rect)

        if self.pressed_keys.get(CANCEL) and self.cursor.current_state != self.cursor:
            self.cursor.current_state.kill()
            self.cursor.current_state = self.cursor
            self.cursor.image = CURSOR_IMAGE

        if self.pressed_keys.get(DROP) and self.cursor.current_state != self.cursor:
            self.pop_tower()
            self.cursor.current_state = self.cursor
            self.cursor.image = CURSOR_IMAGE

    def pop_tower(self):

        tower = self.cursor.current_state
        if self.player.gold < tower.cost:
            print("Pas assez riche")
            return

        Tower.group.add(tower)
        self.player.pay(tower.cost)
        self.cursor.current_state.rect = pygame.Rect(self.cursor.rect.x, self.cursor.rect.y, GRID_WIDTH, TOWER_HEIGHT)

    def add_message(self, key, text, position):
        # message_surface = self.font.render(message, True, FONT_COLOR)
        self.messages[key] = (text, position)

    def handle_collisions(self):
        collision_dict = pygame.sprite.groupcollide(Projectiles.group, Creeps.group, True, False)
        for projectile, creep in collision_dict.items():
            projectile.do_damage(creep[0], Creeps.group)



