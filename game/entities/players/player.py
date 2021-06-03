class Player():

    def __init__(self, base_hp, base_gold):
        self.hp    = base_hp
        self.gold  = base_gold
        self.score = 0

    def get_income(self, income):
        self.gold += income

    def pay(self, gold):
        self.gold -= gold
        print(f"[*] Payé {gold} golds, il en reste {self.gold}")
