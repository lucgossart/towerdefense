from constants import *

class Player():

    def __init__(self):
        self.hp    = BASE_HP
        self.gold  = BASE_GOLD
        self.score = 0

    def get_income(self, income):
        self.gold += income

    def pay(self, gold):
        self.gold -= gold
