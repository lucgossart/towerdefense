

class Controller:

    def __init__(self, player_list, cursor, building_positions: dict=dict()):
        self.cursor = cursor
        self.player = player_list[0]

        self.building_positions = building_positions
        self.selected_building  = None
        pass

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

                try:
                    self.__getattribute__(function)()
                except AttributeError as e:
                    print(f"[!] Dans le contrôleur, la fonction {function} correspondant\
                            à la touche {key} n'est pas définie\n", e)

    def cursor_down(self):
        self.cursor.move_down()
    def cursor_up(self):
        self.cursor.move_up()
    def cursor_left(self):
        self.cursor.move_left()
    def cursor_right(self):
        self.cursor.move_right()

    def select_or_build(self):
        try:
            building = self.building_positions[(self.cursor.rect.x, self.cursor.rect.y)]
        except KeyError:
            self.build_current_tower()
            return
        
        self.selected_building    = building
        self.cursor.current_state = 



