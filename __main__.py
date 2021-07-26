import pygame
pygame.init()
from towerdefense.game import Game

def main():
    game = Game()

    clock = pygame.time.Clock()
    fps = 60

    while game.run:
        clock.tick(fps)
        game.get_events()
        game.loop_callback()
        pygame.display.update()

main()

