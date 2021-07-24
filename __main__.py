from towerdefense.game import Game

import pygame

def main():
    pygame.init()
    game = Game()
    clock = pygame.time.Clock()
    fps = 60

    while game.run:
        clock.tick(fps)
        game.get_events()
        game.loop_callback()
        pygame.display.update()

main()

