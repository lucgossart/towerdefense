import pygame
from towers      import RedTower
from constants   import *
from game        import Game
from creeps      import Creeps
from projectiles import Spear
from vector      import Vector


def main():

    pygame.init()
    game          = Game()
    clock         = pygame.time.Clock()
    run           = True
    compteur      = 0

    
    # RedTower(pygame.Rect(80,80,40,40))
    
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
