from pygame.sprite import Sprite, Group
from pygame.font   import SysFont


class Message(Sprite):

    messages = Group()

    def init(self, text: str, position: tuple[int, int], font=("Verdana", 60), font_color = (0, 0, 0)):
        
        super().__init__()

        self.font     = SysFont(*font)
        self.image    = self.font.render(text, True, font_color)
        self.position = position

        Message.messages.add(self)

    def display(self, surface):
        surface.blit(self.image, self.position)



        
