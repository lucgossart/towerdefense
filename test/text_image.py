"""
Example of a piece of text and a tower.
q: lol -> mdr
s: right translation of the text
j and k: the tower moves in diagonal.
"""
import pygame

from helper.display import Displayer, Text, Rectangle, Image
from helper.unit    import Unit, Weapon
from helper.vector  import Vector

class Game:

    def __init__(self):
        self.run = True
        width, heigth = (1000, 800)
        self.displayer = Displayer(width, heigth)
        self.text = Text("lol", (200, 300), font_color=(0, 120, 255))
        self.pressed_keys = dict()
        self.mouse_position = (0,0)
        self.background = Rectangle(x=0, y=0, width=width, height=heigth, color=(0,0,255))
        tower_image = Image('images/tour_orange_3.xcf', 50, 80)
        tower_attributes = {'position': (0, 0), 'move_speed': 2}
        weapon = None
        self.tower = Unit(tower_attributes, tower_image, weapon)


    
    def loop_callback(self):
        if self.pressed_keys.get(pygame.K_q):
            self.text.set_text('mdr')
        if self.pressed_keys.get(pygame.K_j):
            self.tower.move(Vector(1,1))
        if self.pressed_keys.get(pygame.K_k):
            self.tower.move(Vector(-1,-1))
        if self.pressed_keys.get(pygame.K_s):
            x, y = self.text.position
            self.text.set_position((x+1, y))
        self.displayer.display(self.background.surface, (0,0))
        self.displayer.display(self.tower.image.surface, self.tower.attributes['position'])
        self.displayer.display(self.text.image, self.text.position)


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


