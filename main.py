import pygame
from graphics  import Game
from constants import *
import towers


def main():

    pygame.init()
    game          = Game()
    clock         = pygame.time.Clock()
    run           = True
    compteur      = 0

    
    test = towers.RedTower(pygame.Rect(80,80,40,40))
    game.towers.add(test)

    while run:
        clock.tick(FPS)
        compteur += 1
        compteur %= 5

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                game.pressed_keys[event.key] = True
            if event.type == pygame.KEYUP:
                game.pressed_keys[event.key] = False
        if compteur == 0:
            game.update()
        game.draw()

    pygame.quit()


if __name__ == '__main__':
    main()
