import pygame
pygame.init()
from towerdefense.game import Game, AnimDict

def main():
    game = Game()
    fire = AnimDict.reverse_archer_anims['fire']
    for image in fire.images:
        image.surface = image.surface.convert()

    clock = pygame.time.Clock()
    fps = 60

    while game.run:
        clock.tick(fps)
        game.get_events()
        game.loop_callback()
        pygame.display.update()

main()

