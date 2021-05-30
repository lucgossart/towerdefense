import pygame

from game.game        import Game
from config.constants import *
from config.controls  import commands


def main():

    pygame.init()
    window      = pygame.display.set_mode((WIDTH, HEIGHT))
    game        = Game()

    game.set_cursor(CURSOR_IMAGE, GRID_WIDTH, WIDTH, HEIGHT)
    game.set_displayer(window, BACKGROUND)
    game.set_player(BASE_HP, BASE_GOLD)
    game.set_controller(commands)

    
    game.main_loop(FPS)
    
    pygame.quit()


if __name__ == '__main__':
    main()
