class Displayer:

    groups_to_draw = dict()

    def __init__(self, window, background, cursor):
        self.background = background
        self.window     = window
        self.cursor     = cursor
        pass

    def display(self):
        self.window.blit(self.background)
        self.window.blit(self.cursor)
        for group in self.groups_to_draw.values():
            group.draw()


