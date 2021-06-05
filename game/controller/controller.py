from config.constants          import *
from config.tower_config       import BUILDINGS
from game.entities.tower_types import RedTower, OrangeTower, BlueTower

class Controller:

    def __init__(self, player_list, cursor, towers_group, displayer, buildings_positions: dict=dict()):
        self.cursor = cursor
        self.player = player_list[0]
        
        self.towers_group = towers_group

        self.buildings_positions = buildings_positions
        self.selected_building   = None
        self.pending_building    = None

        self.displayer = displayer

    def set_bindings(self, dictionnary):
        self.bindings = dictionnary

    def perform_actions(self, pressed_keys):

        for key in pressed_keys.keys():

            if pressed_keys.get(key):
                try:
                    function = self.bindings[key]
                except KeyError:
                    print(f"[!] La touche {key} n'est pas associée à une action :")
                    continue

                # try:
                self.__getattribute__(function)()
                # except AttributeError as e:
                #     print(f"""[!] Dans le contrôleur, la fonction {function} correspondant
                #             à la touche {key} n'est pas définie\n""", e)

    def cursor_down(self):
        self.cursor.move_down()
    def cursor_up(self):
        self.cursor.move_up()
    def cursor_left(self):
        self.cursor.move_left()
    def cursor_right(self):
        self.cursor.move_right()
    def handle_mouse(self, pos_x, pos_y):
        self.cursor.place_at(pos_x, pos_y)

    def deselect_building(self):
        if self.selected_building != None:
            self.selected_building = None
            self.cursor.reset_image()
        self.displayer.selection_sprite.kill()

    def select_or_build(self):
        try:
            building = self.buildings_positions[(self.cursor.rect.x, self.cursor.rect.y)]
        except KeyError:
            self.build_current_tower()
            return
        
        self.pending_building = None
        self.cursor.reset_image()
 
        self.selected_building = building
        self.displayer.display_selection(building.rect.x - 3, building.rect.y - 3, building.rect.width + 6, building.rect.height + 6)

    def prepare_red_tower(self):
        self.pending_building = RedTower
        self.pending_keyword  = 'red'
        self.prepare_building()

    def prepare_orange_tower(self):
        self.pending_building = OrangeTower
        self.pending_keyword  = 'orange'
        self.prepare_building()

    def prepare_blue_tower(self):
        self.pending_building = BlueTower
        self.pending_keyword  = 'blue'
        self.prepare_building()

    def prepare_building(self):
        level                 = 0
        dictionary            = BUILDINGS[self.pending_keyword][level]
        self.cursor.image     = pygame.image.load(dictionary['image_path'])
        width, height         = dictionary['width'], dictionary['height']
        self.cursor.image     = pygame.transform.scale(self.cursor.image, (width, height))

    def build_current_tower(self):
        if self.pending_building != None:
            cost =  BUILDINGS[self.pending_keyword][0]['cost']
            if self.player.gold < cost:
                print(f"[!] Il faut {cost} gold ! Tu en as {self.player.gold}")
                return
            self.player.pay(cost)
            level = 0
            dictionary_list = BUILDINGS[self.pending_keyword]
            dictionary      = dictionary_list[level]
            width, height   = dictionary['width'], dictionary['height']
 
            rect = self.cursor.rect
            position = pygame.Rect(rect.x, rect.y, width, height)
            new_tower = self.pending_building(dictionary_list, position)
            self.buildings_positions[(position.x, position.y)] = new_tower
 
            self.pending_building = None
            self.cursor.reset_image()

    def unprepare_and_or_deselect(self):
        self.deselect_building()
        self.pending_building = None

    def upgrade(self):
        if self.selected_building == None:
            return
        self.selected_building.upgrade(self.player)


