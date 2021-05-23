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
    Creeps(100, 2).spawn(pygame.Rect(160, 800, CREEP_WIDTH, CREEP_HEIGHT))
    Creeps(100, 2).spawn(pygame.Rect(160, 1200, CREEP_WIDTH, CREEP_HEIGHT))
    
    while run:

        clock.tick(FPS)
        compteur += 1
        compteur %= 5

        game.add_message('score', f"Score: {game.player.score}", (0, 0))
        game.add_message('gold',  f"Gold:  {game.player.gold}",  (0, 40))

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
