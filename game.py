import pygame
import pygame.sprite
from pygame.sprite import Sprite, Group
from constants import *
from tower_config import TOWERS
from waves_config import WAVES
from projectiles import Projectiles
from towers      import TowerFactory, TowerTypeFactory
from player      import Player
from creeps      import Creeps
from cursor      import Cursor
from towers      import Tower
from waves       import Wave
from building    import Building

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
        for i in range(WIDTH // GRID_WIDTH):
            for j in range(8, 10):
                rect = pygame.Rect(i * GRID_WIDTH, HEIGHT - j * GRID_WIDTH, GRID_WIDTH, GRID_WIDTH)
                TowerFactory.create_tower('rempart', rect)

    def draw(self):

        window.blit(background, (0, 0))
        window.blit(self.cursor.image, (self.cursor.rect.x % WIDTH, self.cursor.rect.y % HEIGHT))

        if self.player.hp <= 0:
            window.blit(self.font.render("NOOB", True, FONT_COLOR), (300, 450))

        for key, (text, position) in self.messages.items():
            message_surface = self.font.render(text + str(self.player.__getattribute__(key)), True, FONT_COLOR)
            window.blit(message_surface, position)

        for building in Building.group:
            building.update_health_bar(window)
            window.blit(building.image, building.rect)

        for tower in Tower.group:
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
            if self.cursor.image == SELECTED_TOWER:
                self.cursor.image = CURSOR_IMAGE
            self.cursor.move_down()

        if self.pressed_keys.get(UP):
            if self.cursor.image == SELECTED_TOWER:
                self.cursor.image = CURSOR_IMAGE
            self.cursor.move_up()

        if self.pressed_keys.get(RIGHT):
            if self.cursor.image == SELECTED_TOWER:
                self.cursor.image = CURSOR_IMAGE
            self.cursor.move_right()

        if self.pressed_keys.get(LEFT):
            if self.cursor.image == SELECTED_TOWER:
                self.cursor.image = CURSOR_IMAGE
            self.cursor.move_left()

    def update_cursor_state(self):

        for key, value in TOWERS.items():
            if self.pressed_keys.get(value[0]['shortcut']):
                if self.pressed_keys.get(pygame.K_LSHIFT) or self.pressed_keys.get(pygame.K_RSHIFT):
                    self.cursor.current_state.kill()
                    self.cursor.current_state = self.cursor
                    self.cursor.image = SELECTED_TOWER
                    self.select_next_tower(TowerTypeFactory.return_type(key).group)
                elif self.cursor.current_state == self.cursor:
                    self.cursor.current_state.kill()
                    self.cursor.current_state = TowerFactory.create_tower(key, self.cursor.rect)

        if self.pressed_keys.get(CANCEL) and self.cursor.current_state != self.cursor:
            self.cursor.current_state.kill()
            self.cursor.current_state = self.cursor
            self.cursor.image = CURSOR_IMAGE

        if self.pressed_keys.get(DROP) and self.cursor.current_state != self.cursor:
            self.pop_tower()

        if self.pressed_keys.get(SELECT_NEXT_TOWER):
            self.select_next_tower(Tower.group)
            self.cursor.current_state.kill()
            self.cursor.image = SELECTED_TOWER

        if self.pressed_keys.get(UPGRADE_TOWER):
            try:
                cost = TOWERS[self.selected_tower.type][self.selected_tower.level + 1]['cost']
                if self.player.gold >= cost:
                    self.player.pay(cost)
                    self.selected_tower.upgrade()
                else:
                    print("Il faut", cost, "gold pour l'upgrade")
            except Exception as e:
                print(e)

    def select_next_tower(self, group):

        minimal_abscissa_difference = 10_000
        minimal_ordinate_difference = 10_000

        for tower in group:

            ordinate_difference = ((tower.rect.y - self.cursor.rect.y) - 5)
            abscissa_difference = ((tower.rect.x - self.cursor.rect.x) - 5) % WIDTH
            minimal_ordinate = 10_000

            if abscissa_difference == 0 and 0 < ordinate_difference < minimal_ordinate_difference:
                minimal_abscissa_difference = 0
                minimal_ordinate_difference = ordinate_difference
                self.selected_tower = tower

            if 0 < abscissa_difference <= minimal_abscissa_difference and tower.rect.y <= minimal_ordinate:
                minimal_abscissa_difference = abscissa_difference
                minimal_ordinate = tower.rect.y
                self.selected_tower = tower

        self.cursor.image     = SELECTED_TOWER
        self.cursor.rect.x    = self.selected_tower.rect.x - 5
        self.cursor.rect.y    = self.selected_tower.rect.y - 5

    def pop_tower(self):

        tower = self.cursor.current_state
        if self.player.gold < tower.cost:
            print("Pas assez riche, il faut", tower.cost)
            return

        self.player.pay(tower.cost)
        self.cursor.current_state.rect = pygame.Rect(self.cursor.rect.x, self.cursor.rect.y, GRID_WIDTH, TOWER_HEIGHT)

        self.cursor.current_state = self.cursor
        self.cursor.image = CURSOR_IMAGE

    def add_message(self, key, text, position):
        # message_surface = self.font.render(message, True, FONT_COLOR)
        self.messages[key] = (text, position)

    def handle_collisions(self):
        collision_dict = pygame.sprite.groupcollide(Projectiles.group, Creeps.group, True, False)
        for projectile, creep in collision_dict.items():
            projectile.do_damage(creep[0], Creeps.group)

        collision_dict = pygame.sprite.groupcollide(Building.group, Creeps.group, False, False)
        for building, creep_list in collision_dict.items():
            for creep in creep_list:
                building.lose_hp()
                creep.lose_hp(1_000 * creep.damage)

